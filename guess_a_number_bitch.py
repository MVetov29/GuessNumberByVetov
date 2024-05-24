import random
computer_number = random.randint(1, 100)

while True:
    number = int(input("Vuvedi nomer:"))
    if computer_number > number:
        print("The number you entered is lower than the desire number")
    elif computer_number < number:
        print("The number you entered is greater than the desire number")
    else:
        print("Congratulation, you guess the number! You win Bitch!!!")
        exit()
