from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
import os
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# load env package
load_dotenv()

# Load gemini api key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Initialize Gemini chat Model
model = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model="gemini-2.5-flash",
    temperature=1.0,
    max_tokens=50,
)

# google embedding model
googal_embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-002",

)

# # huggingface embedding
# huggingface_embeddings = HuggingFaceEmbeddings(
#     model="sentence-transformers/all-MiniLM-l6-v2"
# )

query = "hello world  my name is anthony"
numbers_embeddings = googal_embeddings.embed_query(query[:50])
print(numbers_embeddings)


#numbers_embeddings Sample prompt message
# messages = [
#     (
#         "system",
#         "You are a helpful Girlfriend. Propose Vijay",
#     ),
#     ("human", "I love vijay."),
# ]
#
# # Invoke the model for response
# ai_msg = model.invoke(messages)
#
# # Print the response
# print(ai_msg.content)