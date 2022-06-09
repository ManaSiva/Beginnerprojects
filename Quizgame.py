
print("welcome to game *")

entry = input("do you wanna play?\n> ")
if entry.lower() != "yes":
    quit()

print("lets play")

score = 0

question1 = input("who are you?\n> ")
ans1 = "siva"
if ans1 == question1:
    score += 1
    
ans2 = "far from you"
question2 = input("where did you go?\n> ")
if ans2 == question2:
    score += 1

ans3 = "in you"
question3 = input("where can i find you?\n> ")
if ans3 == question3:
    score += 1

print(f"you got {score} crct")
