from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

def result(query):

    messages = [
        (
            "system",
            "You are a helpful telegram bot that will talk as a friend",
        ),
        ("human", query),
    ]
    ai_msg = llm.invoke(messages)
    # print(ai_msg.content)
    return ai_msg.content

if __name__=="__main__":
    chat_msg = result("hello")
    print(chat_msg)

