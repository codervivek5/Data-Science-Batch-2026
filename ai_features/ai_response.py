import asyncio
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.memory import ConversationBufferMemory
from langchain.messages import HumanMessage, SystemMessage

llm = ChatOllama(
    model="llama3.2",
    temperature=0.7,
)

async def result(query):
    prompt_template = PromptTemplate(
        template=""""
                You are a helpful telegram bot.
                Talk like a friendly human in Hinglish.
                Your name is {name}.
                
                User: {query}
                Bot:
                """,
        input_variables=["name","query"],
    )
    prompt = prompt_template.format(
        name="Lol Ritu",
        query=query,
    )

    ai_msg = await llm.ainvoke(prompt)
    return ai_msg.content

if __name__=="__main__":
    chat_msg = asyncio.run(result("hello"))
    print(chat_msg)

