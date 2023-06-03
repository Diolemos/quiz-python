from question_model import Question
import requests as rq


def get_data():
    params = {
        "amount":10,
        "type":"boolean",
        "category":18,
    }
    response = rq.get('https://opentdb.com/api.php', params=params) 
    response.raise_for_status()

    question_data = response.json()['results']
    
    questions = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        questions.append(new_question)
    return questions    