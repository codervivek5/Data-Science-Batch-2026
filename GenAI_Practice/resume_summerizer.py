from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os
# import logging

# logging.basicConfig(level=logging.INFO) 
load_dotenv()  # Load environment variables from .env file


api_key = os.getenv("GOOGLE_API_KEY")



text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)

# Data path
docs_path = "data/vivek.pdf"

# Document loader
loder = PyPDFLoader(docs_path)
dakument = loder.load()

# Text splitting
texts = text_splitter.split_documents(dakument)

# print("🧨 Texts: ", texts) #done
print("--------------------------------------------------------------")

# Embedding model using Google GenAI
embedding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", api_key=api_key)
# embeddings = embedding.embed_documents(texts)

# Vector Store initialization
vector_store = FAISS.from_documents(texts,embedding)

# retrival
retrival  = vector_store.as_retriever(search_type="mmr",search_kwargs={"k": 6})

# LLm Initialization
llm = GoogleGenerativeAI(model="gemini-2.5-flash")

# query to ask
query = "let me know about the experience of vivek in the field of data science and machine learning"

# Get relevant documents
relevant_docs = retrival.invoke(query)

# print("🧨 Relevant documents: ", relevant_docs[2].page_content)

context = "\n".join([doc.page_content for doc in relevant_docs]) # "".join([doc.page_content for doc in relevant_docs])

# Prompt for LLM
prompt = f"""
    Based on the following information, answer the question: 
    {query}
    using the following context:
    {context}

"""

# Generate response using LLM
response = llm.invoke(prompt)

print("🧨 Response: ", response)