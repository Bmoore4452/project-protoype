import random

# Create level 1 questions and answers
currentRavens = [
    {
        "question": "What jersey number does Lamar Jackson wear? ",
        "answers": ["8", "5", "1", "15"],
        "correct": "8",
    },
    {
        "question": "What position does Lamar Jackson play? ",
        "answers": ["Quarterback", "Running Back", "Wide Reciever", "Linebacker"],
        "correct": "Quarterback",
    },
    {
        "question": "Who is the head coach for the Baltimore Ravens? ",
        "answers": ["John Harbough", "Andy Reid", "Bill Belichick", "Nick Sirianni"],
        "correct": "John Harbough",
    },
    {
        "question": "What is the primary color of the Baltimore Ravens? (other than black) ",
        "answers": ["Purple", "Yellow", "Red", "Green"],
        "correct": "Purple",
    },
    {
        "question": "How many wins did the 2023 Baltimore Ravens have? ",
        "answers": ["13", "6", "11", "9"],
        "correct": "13",
    },
]

# Create level 2 questions and answers
recentRavens = [
    ("What number did Terrell Suggs wear? ", "55"),
    ("What year did the Baltimore Ravens win their last Super Bowl? ", "2013"),
    ("Who was the quarterback for the 2012-2013 Baltimore Ravens? ", "Joe Flacco"),
    (
        "How many touchdowns did Joe Flacco throw in the 2013 playoffs en route to Super Bowl? ",
        "11",
    ),
    ("Who did the Baltimore Ravens win the 2013 Super Bowl agaisnt? ", "49ers"),
]

# Create level 3 questions and answers
legendRavens = [
    ("What number did Ray Lewis wear? ", "52"),
    ("What year was Ray Lewis drafted? ", "1999"),
    (
        "Who was the genral manager for Baltimore Ravens for the 1999 NFL Draft? ",
        "Ozzie Newsome",
    ),
    (
        "Who has the longest interception return in Baltimore Ravens history? ",
        "Ed Reed",
    ),
    ("Who did the Baltimore Ravens win the 2000 Super Bowl agaisnt? ", "Giants"),
]


# Start the game
def main():
    score = 0

    # Define multiple choice input options
    choices = ["a", "b", "c", "d"]
    
    # Shuffle questions and answers so not test is ever the same
    random.shuffle(currentRavens)
    random.shuffle(choices)
    
    # Iterate through questions list
    for x in currentRavens:

        # Iterate through and identify each question, answers, and correct answer
        for y in x:

            # Identify question
            if y == "question":
                question = x[y]

            # Identify answer options
            if y == "answers":
                a = x[y]
                random.shuffle(a)

            # Identify correct answer
            if y == "correct":
                correct = {"correct": x[y]}

                # Prints each question
                print(question)

                # Converts input options and answer options into a dictionary
                res = {choices[i]: a[i] for i in range(len(choices))}

                # Prints each options for user to choose from
                print(f"A. {res['a']}")
                print(f"B. {res['b']}")
                print(f"C. {res['c']}")
                print(f"D. {res['d']}")

                # Prompt user input
                while True:
                    choice = input("Pick: ").casefold()

                    # Check for a valid choice
                    if choice in choices:

                        # Check for correct input
                        if res[choice] == correct["correct"]:
                            score += 1
                            break
                        else:
                            print("Incorrect")
                            break
                    else:
                        print("***Please choose a valid answer (a, b, c , or d)***")

    # Evaluate user's performance
    result = score / len(currentRavens) * 100
    if result >= 60:
        print("You have completed level 1")
    else:
        print("You are not a Baltimore Ravens fan")


# result1 = askCurrent(currentRavens)
# if result1 >= 60:
#     result2 = askRecent(recentRavens)
# else:
#     print("Please study the current Baltimore Ravens")
#     return
# if result2 >= 60:
#     result3 = askLegend(legendRavens)
# else:
#     print("Please study the 2013 Baltimore Ravens")
#     return
# if result3 >= 60:
#     print("You are a true Baltimore Ravens fan")
# else:
#     print("Please study the 2000 Baltimore Ravens")
#     return


# Ask questions for level 1
# def askCurrent(questions):
#     score = 0
# Ask each question
# for question, answer in questions:
# Allow user input
#     x = input(question).casefold()
#     # Check users input
#     if x == str(answer).casefold():
#         score += 1
#     else:
#         print("incorrect! The answer is", answer)
# result = score / len(questions) * 100
# if result >= 60:
#     print("You have completed level 1")
# else:
#     print("You are not a Baltimore Ravens fan")
# return result


# Ask questions for level 2
# def askRecent(questions):
#     score = 0
#     # Ask each question
#     for question, answer in questions:
#         # Allow user input
#         x = input(question).casefold()
#         # Check users input
#         if x == str(answer).casefold():
#             score += 1
#         else:
#             print("incorrect! The answer is", answer)
#     result = score / len(questions) * 100
#     if result >= 60:
#         print("You have completed level 2")
#     else:
#         print("You are a level 1 fan")
#     return result


# # Ask questions for level 3
# def askLegend(questions):
#     score = 0
#     # Ask each question
#     for question, answer in questions:
#         # Allow user input
#         x = input(question).casefold()
#         # Check users input
#         if x == str(answer).casefold():
#             score += 1
#         else:
#             print("incorrect! The answer is", answer)
#     result = score / len(questions) * 100
#     if result >= 60:
#         print("You have completed level 3")
#     else:
#         print("You are a level 2 fan")
#     return result


if __name__ == "__main__":
    main()
