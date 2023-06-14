'''https://www.udemy.com/course/100-days-of-code/learn/lecture/19964886#overview'''



from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q = question['question']
    a = question['correct_answer']
    question_bank.append(Question(q, a))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")