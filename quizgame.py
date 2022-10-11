# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Everyone')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Welcome to the Quiz Game")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :) ")
score = 0



answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")







