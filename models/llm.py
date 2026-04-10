from langchain_ollama import ChatOllama,OllamaEmbeddings
from Prompts.question_prompt import question_prompt

# LLM Configuration
llm = ChatOllama(
    model="llama3.2",
    temperature=0.5,
)


# Embedding Configuration
embeddings = OllamaEmbeddings(model="llama3.2")

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
ai_msg