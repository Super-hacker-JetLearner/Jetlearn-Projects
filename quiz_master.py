import random



# with open("questions.txt", "w") as f:
#     f.write("What is the longest river in the world?,The Nile,Amazon River,Missispi River,Atlantic Ocean,1\n")
#     f.write("What country has the most people?,USA,China,India,Antarctica,3")
    
questions = []
with open("questions.txt", "r") as f:
    for i in f.readlines():
        questions.append(i.strip().split(","))
        
random.shuffle(questions)


def draw_questions(question):
    print(f"Question:  {question[0]}")
    for i in range (1,5):
        print(f"{i}. {question[i]}")
        
for i in range(len(questions)):
    draw_questions(questions[i])


    guess = int(input("Enter a number between 1 and 4: "))

    # print(questions)

    if guess == int(questions[i][5]):
        print("correct")
    else:
        print(f"incorrect! The correct answer was {questions[i][int(questions[i][5])]}")
        
