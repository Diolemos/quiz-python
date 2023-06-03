from gui import QuizzUi
from data import question_data
from quiz_brain import QuizBrain
from get_data import get_data as gt
question_bank = gt()



quiz = QuizBrain(question_bank)
quizz_ui = QuizzUi(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
