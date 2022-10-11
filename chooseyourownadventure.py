# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

name = input("Type your name: ")
print("Welcome", name, "to this adventure.")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')


elif answer =="right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back)? ")

    if answer == "back":
        print("You go back and lose! ")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. Do you talk to them? (yes/no) ")

        if answer == "yes":
            print("You talked to the stranger and they give you gold and you WIN!. ")
        elif answer == "no":
            print("You ignored the stranger and they are offended and you lost!. ")
    else:
        print('Not a valid option. You lose.')


else:
    print('Not a valid option, you lose.')

print("Thank you trying", name)



