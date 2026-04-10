from pydoc_data.topics import topics

from langchain_classic.chains.question_answering.map_reduce_prompt import messages
from langchain_ollama import ChatOllama,OllamaEmbeddings
from Prompts.question_prompt import question_prompt

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import PromptTemplate

# LLM Configuration
llm = ChatOllama(
    model="llama3.2",
    temperature=0.5,
)


prompt = PromptTemplate(
    template="Write a summery about the {topic} in 50 lines only",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({
    "topic": "mahatma gandhi",
})

print(result)

#
# # Format the prompt
# formatted_prompt = message.format(topic="world war 3")
# print(formatted_prompt)
#
# result = llm.invoke(formatted_prompt)
# print(result.content)