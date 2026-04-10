from Prompts.question_prompt import question_prompt
from Prompts.evaluation_prompt import evaluation_prompt
from models.llm import llm
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# In models/generator.py
question_chain = question_prompt | llm | parser
evaluation_chain = evaluation_prompt | llm | parser


