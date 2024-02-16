# Create level 1 questions and answers
currentRavens = [
    {
        "question": "What jersey number does Lamar Jackson wear? ",
        "answers": ["8", "5"],
        "correct": "8",
    },
    # ("What position does Lamar Jackson play? ", "QB"),
    # ("Who is the head coach for the Baltimore Ravens? ", "John Harbough"),
    # (
    #     "What is the primary color of the Baltimore Ravens? (other than black) ",
    #     "Purple",
    # ),
    # ("How many wins did the 2023 Baltimore Ravens have? ", "13"),
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
    choices = ["a", "b", "c", "d"]
    for x in currentRavens:
        for y in x:
            if y == "question":
                question = x[y]
            if y == "answers":
                a, b = x[y]
            if y == "correct":
                correct = x[y]
                print(question)
                print(f"A. {a}")
                print(f"B. {b}")
            choice = input("Pick: ").casefold()

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
