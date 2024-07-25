print("Welcome To My Computer Quize Game !")

playing = input("Do You Want To Play? (Yes / No) ")

if playing.lower() != "yes":
    quit()

print("Okay ! Let's Play :) ")
score = 0

answer = input("What Dose CPU Stand For? ")
if answer.lower() == "central processing unit":
    print('Correct !')
    score += 1
else:
    print("Incorrect !") 


answer = input("What Dose GPU Stand For? ")
if answer.lower() == "graphics processing unit" :
    print('Correct !')
    score += 1
else:
    print("Incorrect !") 


answer = input("What Dose PSU Stand For? ")
if answer.lower() == "power supply":
    print('Correct !')
    score += 1
else:
    print("Incorrect !") 


answer = input("What Dose RAM Stand For? ")
if answer.lower() == "random access memory" :
    print('Correct !')
    score += 1
else:
    print("Incorrect !") 

print("You Got " + str(score) + " Question Correct !")
print("You Got " + str((score / 4) * 100) + " %.")
