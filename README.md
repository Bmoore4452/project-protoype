# Documentation for Pre-Employment Assesment Prototype Project

## Project Summary

Pre-employment assessments are crucial for employers to gather valuable information about potential job candidates. These assessments provide a more in-depth understanding of the candidate's skills, knowledge, and personality traits than a resume or job interview alone. The assessments can include cognitive ability, personality, and situational judgment tests that help employers make informed hiring decisions. By using pre-employment assessments, employers can select the most qualified and suitable candidates for the position, which leads to better job performance and a more successful organization overall.

This project is a prototype for an assessment tool that tests the user's knowledge on multiple levels. As the user passes each level of questioning, they will move on to the next level. If the user fails a level of questioning, they will be notified of the failure and given information on what they need to study to pass their current highest achieved level.

## Usage

To run the `main.py` file from the Project-Prototype in the Command Line Interface (CLI), navigate to the project directory and execute the following command:

`python main.py`

When the user runs the program in the CLI, they will be presented with a series of questions. The user will be prompted to select an answer from the options provided, which are limited to a, b, c, or d. If the user enters any other character, they will be prompted to enter a valid input until an acceptable option is selected or the program is ended by pressing control + C.

If the user selects the correct answer, the next question will be presented. If the user selects an incorrect answer, they will be notified of the mistake, and the next question will still be presented. This process will continue until all the questions at the current level have been answered.

If the user's score is greater than or equal to 60 percent, they will be notified that they have passed the current level and presented with the next level of questions. If the user's score is less than 60 percent, they will be notified of their failure to attain a passing score and presented with recommendations for topics to study in order to improve their score if they decide to take the assessment again.

### How it works?

Each "ask" function (i.e., `askCurrent`,`askRecent`, and `askLegend`) takes a list of dictionaries as an argument, where each dictionary represents a question, its possible answers, and the correct answer.

The function starts by initializing a [`score`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22score%22%5D 'main.py') variable to 0 and defining a list of [`choices`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22choices%22%5D 'main.py') for the multiple-choice options. It then shuffles the list of questions and the choices to ensure that no two quizzes are the same.

The function then iterates over each question in the shuffled list. For each question, it identifies the question text, the possible answers, and the correct answer. It shuffles the possible answers to randomize their order.

Next, the function prints the question and the possible answers, each labeled with a letter from the [`choices`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22choices%22%5D 'main.py') list. It then prompts the user to input their answer. The user's input is casefolded, meaning it's converted to lowercase to ensure that the comparison with the correct answer is case-insensitive.

The function then checks if the user's input is a valid choice (i.e., it's one of the letters in the [`choices`](command:_github.copilot.openSymbolInFile?%5B%22main.py%22%2C%22choices%22%5D 'main.py') list). If the input is valid, the function checks if it corresponds to the correct answer. If it does, the user's score is incremented by 1. If the input is not valid, the function prompts the user to enter a valid answer.

After all the questions have been asked, the function calculates the user's score as a percentage of the total number of questions. If the user's score is 60% or higher, the function prints a message indicating that the user has completed level 1. If the score is lower than 60%, the function prints a message indicating that the user is not a Baltimore Ravens fan.

Finally, the function returns the user's score as a percentage.
