from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="llama3.2", temperature=0.3)

prompt1 = PromptTemplate(
    template='look at this {text} and reply only "Positive" or "Negative"',
    input_variables=["text"]
)

positive_prompt = PromptTemplate(
    template="If the sentiment of {text} is positive then give me congratulations",
    input_variables=["text"],
)

negative_prompt = PromptTemplate(
    template="If the sentiment of {text} is negative then give me 3 improvement points",
    input_variables=["text"],
)

parser = StrOutputParser()

condition_chain = prompt1 | llm | parser # check sentiment

positive_chain = positive_prompt | llm | parser # thynos vali chain
negative_chain = negative_prompt | llm | parser # caption america

# FIX: prepare dict
prepare = RunnableLambda(
    lambda x: {
    "text": x["text"],
    "sentiment": condition_chain.invoke({"text": x["text"]})
})

# FIX: correct branch + default,test
branch_chain = RunnableBranch(
    (lambda x: "Positive" in x["sentiment"], positive_chain),
    (lambda x: "Negative" in x["sentiment"], negative_chain),
    negative_chain  # ✅ default required
)

final_chain = prepare | branch_chain

result = final_chain.invoke({
    "text": "Ravi had been working hard for months on his startup, often staying up late and sacrificing time with his family. When he finally launched his product, the initial response was disappointing, and he felt frustrated and anxious about his future. However, a few days later, positive reviews started coming in, and customers began appreciating his effort. Slowly, his confidence returned, and he felt proud and motivated to keep improving. By the end, Ravi realized that success comes with patience, and even small wins can bring great happiness."
})

print(result)