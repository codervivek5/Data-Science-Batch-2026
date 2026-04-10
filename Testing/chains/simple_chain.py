from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# LLM Configuration
llm = ChatOllama(
    model="llama3.2",
    temperature=0.3,
)

prompt1 = PromptTemplate(
    template="write a summery about {topic} in 200 characters in a story form",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="write a 5 pointer summery about {text} in the bullet points",
    input_variables=["text"]
)

parser = StrOutputParser()

dummy_chain = prompt1 | llm | parser

chain = prompt1 | llm | parser | prompt2 | llm | parser

# chain.get_graph().print_ascii()

dummy_result = dummy_chain.invoke({
        "topic": "cat"
})

result = chain.invoke({
    "topic": "cat"
})

print(dummy_result)
# print(result.content)
print(result)
