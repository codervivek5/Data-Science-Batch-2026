from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# LLM Configuration
llm = ChatOllama(
    model="llama3.2",
    temperature=0.5,
)


prompt1 = PromptTemplate(
    template="Write a summery about the {topic} in 20 lines only",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write 5 points on {text} in short with bullet points",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | llm | parser | prompt2 | llm | parser

result = chain.invoke({
    "topic": "cat",
})
print(result)

# chain.get_graph().print_ascii()