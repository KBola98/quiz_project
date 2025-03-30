
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        
        return self.question_number < len(self.question_list)
        
        
    #Input for Next question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        
        self.question_number +=1
        user_answer = input(f"Q : {self.question_number} {current_question.text}(True or False)?")
        self.check_answer(current_question.answer, user_answer, self.question_number)
        
        
    def check_answer(self, correct_question, user_answer, question_number):
        if correct_question.lower() == user_answer:
            print("Answer is correct")
            self.score+=1
            
        else:
            print("Ansser is false")
            
        print(f"The Correct answer is {correct_question}")
        print(f"Current Score is {self.score}/{question_number}")
        print("\n")