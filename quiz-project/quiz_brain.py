class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_question_text = current_question.text
        self.question_number += 1
        u_answer = input(f"Q. {self.question_number} : {current_question_text} (True/False)").lower()
        self.check_correct_answer(u_answer, current_question.answer)
        
    def get_score(self):
        return self.score
        

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        # or just return self.question_number < len(self.question_list):

    def check_correct_answer(self, u_answer, correct_choice):
        if u_answer.lower() == correct_choice.lower():
            self.score += 1
            print("That's right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_choice}")
        print(f"Current score is: {self.score}/{self.question_number}")
        print("\n")