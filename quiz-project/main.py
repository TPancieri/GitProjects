from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain 

question_bank = []

for quest in question_data:
    quest_text = quest["text"]
    quest_answer = quest["answer"]
    new_question = Question(quest_text, quest_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question
    
print("Quiz completed!")
print(f"Final score : {quiz.score} / {quiz.question_number}")