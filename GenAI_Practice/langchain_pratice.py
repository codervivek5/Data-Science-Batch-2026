import os   
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv



load_dotenv()

api_key = os.environ["GOOGLE_API_KEY"]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.3,  # Gemini 3.0+ defaults to 1.0
    max_tokens=1000,
)

response = [
    
    ("human", "I love programming."),
]

ai_msg = model.invoke(response)
print(ai_msg.content)