from models.generator import question_chain

# Generate Question
def easy(difficulty="easy"):
    response = question_chain.invoke({
        "difficulty": difficulty
    })
    return response

def medium(difficulty="medium"):
    response = question_chain.invoke({
        "difficulty": difficulty
    })
    return

def hard(difficulty="hard"):
    response = question_chain.invoke({
        "difficulty": difficulty
    })
    return response

print(easy())
# print(medium())
# print(hard())


