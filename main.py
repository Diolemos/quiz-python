from question_model import Question
from get_data import get_data as gt
from quiz_brain import QuizBrain
from gui import QuizzUi

# new_question = Question(random.choice(data.question_data))
question_bank = gt()



quiz = QuizBrain(question_bank)
quiz_ui = QuizzUi()

# while quiz.still_has_questions():

    
print("You've completed the Quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")    