from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from typing import Literal, Optional
load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Initialize Gemini chat Model
model1 = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model="gemini-2.5-flash",
    temperature=0.3,
)

# LLM Configuration
model2 = ChatOllama(
    model="llama3.2",
    temperature=0.3,
)



prompt1 = PromptTemplate(
    template="Summerize this: {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Analysis the sentiment of this {text}",
    input_variables=["text"]
)


prompt3 = PromptTemplate(
    template="Generate story based on {text} in bullet points",
    input_variables=["text", "sentiment"],

)

parser = StrOutputParser()

summary_chain = prompt1 | model2 | parser
quiz_chain = prompt2 | model2 | parser
merge_chain = prompt3 | summary_chain | quiz_chain | model2 | parser

parallel_chain = RunnableParallel(
   summary = summary_chain,
   quiz = quiz_chain,
   merge = merge_chain,
)


result = parallel_chain.invoke(
    {
        "text": "Liquefied Petroleum Gas (LPG)** is a commonly used fuel that plays an important role in daily life. It is a mixture of hydrocarbon gases, mainly propane and butane, which are stored in liquid form under pressure. When released, it converts into gas and is widely used for cooking, heating, and even as a fuel in vehicles. LPG is considered a clean and efficient source of energy because it produces less smoke and pollution compared to other fuels. It is easy to store, transport, and provides instant heat control, making it very convenient for household use. However, LPG is highly flammable and requires careful handling and proper storage to avoid accidents. Since it is naturally odorless, a strong-smelling chemical is added to detect leaks easily. Overall, LPG is an efficient and reliable energy source used worldwide.",

    }
)

print(result)




