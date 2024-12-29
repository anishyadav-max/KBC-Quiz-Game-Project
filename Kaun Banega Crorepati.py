# KBC

import random
import time


questions = [
    ['What is the capital of India?', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai', 1],
    ['Who wrote Harry Potter?', 'J.K. Rowling', 'George R.R. Martin', 'J.R.R. Tolkien', 'Suzanne Collins', 1],
    ['What is the largest planet in our solar system?', 'Earth', 'Jupiter', 'Saturn', 'Mars', 2],
    ['Which is the smallest country in the world?', 'Monaco', 'Vatican City', 'San Marino', 'Liechtenstein', 2],
    ['Which is the longest river in the world?', 'Amazon', 'Nile', 'Yangtze', 'Mississippi', 2],
    ['What is the national animal of India?', 'Tiger', 'Lion', 'Elephant', 'Leopard', 1],
    ['Who is known as the father of computers?', 'Charles Babbage', 'Alan Turing', 'Bill Gates', 'Steve Jobs', 1],
    ['Which is the fastest land animal?', 'Cheetah', 'Leopard', 'Tiger', 'Horse', 1],
    ['What is the boiling point of water?', '90°C', '100°C', '110°C', '120°C', 2],
    ['What is the capital of France?', 'Paris', 'Berlin', 'Madrid', 'Rome', 1],
    ['Who painted the Mona Lisa?', 'Leonardo da Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet', 1],
    ['Which planet is known as the Red Planet?', 'Mars', 'Venus', 'Mercury', 'Jupiter', 1],
    ['What is the chemical symbol for water?', 'H2O', 'CO2', 'O2', 'NaCl', 1],
    ['Who discovered penicillin?', 'Alexander Fleming', 'Marie Curie', 'Louis Pasteur', 'Isaac Newton', 1],
    ['What is the tallest mountain in the world?', 'K2', 'Mount Everest', 'Kangchenjunga', 'Makalu', 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

lifelines_used = {'50:50': False, 'Phone-a-Friend': False, 'Ask the Expert': False}

money = 0

for i in range(len(questions)):
    question = questions[i]
    print(question[0])
    print(f"(1). {question[1]}            (2). {question[2]}")
    print(f"(3). {question[3]}            (3). {question[4]}")

    while True:
        user_lifeline_choice = input("you need life line(yes/no): ").rstrip().lower()

        if user_lifeline_choice == "yes":
            for index , lifeline in enumerate(lifelines_used,start=1):
                print(f"press{index}. for {lifeline}")

            user_input=int(input("enter a number: "))

            if user_input == 1 and not lifelines_used['50:50']:
                print("user chooses 50-50 lifeline")
                options=question[1:5]
                correct_option = question[-1]
                incorrect_option = [question[i] for i in range(1,5) if i!=correct_option ]
                # print(f"incorrect option are {incorrect_option}")
                remove_option = random.sample(incorrect_option,2)
                remaining_option =[option for option in options if option not in remove_option]
                print(f"remaining option after 50-50 lifeline: {remaining_option}")
                print(question[0])
                print(f"(1). {question[1]}            (2). {question[2]}")
                print(f"(3). {question[3]}            (3). {question[4]}")
                lifelines_used['50:50'] = True
                break
            if user_input == 2 and not lifelines_used['Phone-a-Friend']:
                print("you have 30 sec to talk a friend on phone")
                for sec in range(1,61):
                    time.sleep(1)
                    print(f"{sec} second passed .....")
                    lifelines_used['Phone-a-Friend'] = True
                print(f"after using phone-a-friend lifeline the correct option is {question[-1]}")
                break
            if user_input == 3 and not lifelines_used['Ask the Expert']:
                print("you have 30 sec to talk a expert on studio")
                for sec in range(1,61):
                    time.sleep(1)
                    print(f"{sec} second passed .....")
                    lifelines_used['Ask the Expert'] = True
                print(f"after using Ask the Expert lifeline the correct option is {question[-1]}")
                lifelines_used['Ask the Expert']=True
                break
            else:
                print("already used lifeline")

        elif user_lifeline_choice == "no" :
            break
        else:
            print("invalid input! please choose(yes/no)")

    reply = int(input("Enter a number between 1 to 4 or 0 to quit: "))
    if reply == 0:
        money = levels[i-1] if i > 0 else 0
        print("You quit the game.")
        break

    if reply == question[-1]:
        print(f"Correct answer! You won {levels[i]}")
        if i == 4:
            print("Basic level ended. Easy level started.")
            money = 80000
        elif i == 9:
            print("Medium level started.")
            money = 160000
        elif i == 14:
            print("Hard level started.")
            money = 10000000
        elif i == 15:
            print("Super hard level started.")
            money = 70000000
    else:        
        print("Wrong answer!")
        break
print(f"Your total money: {money}")

