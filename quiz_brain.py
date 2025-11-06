class QuizBrain:
    def __init__(self , list_q):
        self.question_number = 0
        self.score = 0
        self.question_list = list_q

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        blah = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(blah ,  current_question.answer)

    def check_answer(self , blah , correct_answer):
        if blah.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong.\nThe correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")