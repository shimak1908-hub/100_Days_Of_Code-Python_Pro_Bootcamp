from quiz_brain import QuizBrain


class Question:
    def __init__(self , q_text , q_answer):
        self.text = q_text
        self.answer = q_answer

from data import question_data
question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_questions = Question(question_text , question_answer)
    question_bank.append(new_questions)
quiz =QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"\n\nYour final score is {quiz.score}/{quiz.question_number}")

