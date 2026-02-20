from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    # other params...
)
messages = [

    ("human", "I fuck you"),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)