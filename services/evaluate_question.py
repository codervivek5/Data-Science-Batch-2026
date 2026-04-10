# Evaluate Answer
from models.generator import evaluation_chain


def evaluate_answer(question, options, correct_answer, user_answer):
    response = evaluation_chain.invoke({
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "user_answer": user_answer
    })
    return response