from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Implementing the for loop to append the Question_Bank List

question_bank = []

for x in question_data:
    qtext= x["text"]
    answer = x["answer"]
    
    question = Question(qtext, answer)
    
    question_bank.append(question)
    

quiz_brain1 = QuizBrain(question_bank)

#loop until the questions finsish
while quiz_brain1.still_has_questions:
      quiz_brain1.next_question()

print("questions over")