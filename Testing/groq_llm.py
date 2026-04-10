from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from Prompts.question_prompt import question_prompt

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
)

# messages = [
#     (
#         "system",
#         "You are a helpful Girlfriend. Propose Vijay",
#     ),
#     ("human", "I love vijay."),
# ]
mcq_questions = model.invoke(question_prompt)
print(mcq_questions.content)
