questions = [ "who is siva?", "where can you find him?", "who is he slave to?"]
answers = [ "a boy", "in love", "to love"]
score = 0

def func():
    
    for i in range(len(questions)):
        print(questions[i])
        user = input("type your answer: ")
        if user == answers[i]:
            global score
            score +=1
        else:
            print('')

    print(f"your total score is: {score} ")

func()




