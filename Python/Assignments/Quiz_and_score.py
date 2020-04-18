questions = [
    "who created Python?\n(a) Guido Rossum\n(b) Brad Pitt\n(c) what is Python\n(d) Bill Gates\nYour Answer: ",
    "Which on is not a Python Data Type?\n(a) int\n(b) list\n(c) tuple\n(d) map\nYour Answer: ",
    "How do you take user input in Python?\n(a) give() \n(b) intake()\n(c) input()\n(d) Scanner()\nYour Answer: "
]
questions
answers = {
    0:'a',
    1:'d',
    2:'c'
}
score = 0
question_number = 0
while question_number < 3:
    answer = input(questions[question_number])
    if answer == answers[question_number]:
        score += 1
    question_number += 1
print('\n', f'Your score is {score}.', sep = '')