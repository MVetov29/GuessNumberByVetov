import random
computer_number = random.randint(1, 100)

counter = 0

while True:
    number = int(input("Enter number bitch: "))
    if computer_number > number:
        counter += 1
        print("The number you entered is lower than the desire number")
    elif computer_number < number:
        counter += 1
        print("The number you entered is greater than the desire number")

    if counter == 3:
        if computer_number == number:
            print("Congratulation, you guess the number! You win Bitch!!!")
            exit()
        else:
            print("Try again.... Ha-Ha-Ha!!!")
            exit()
