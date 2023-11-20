#! /usr/bin/python3.10
import json
import re

FILE_PATH = 'data.json'

def get_questions(file_path:str)-> dict:
    """
    This function takes a file path as input and returns a list of dictionaries containing the questions
    and their corresponding answers. If the file cannot be read, it returns None.

    Args:
    - file_path (str): The path to the file containing the questions and answers.

    Returns:
    - data (list): A dictionary containing the questions and their corresponding answers.
    """
    try:
        file = open(file_path, 'rt')
        data = json.load(file)
        file.close()
    except OSError:
        print("Something went wrong while trying to read the file with the questions")
        data = None
    return data


def ask_user_a_question():
    """
    Asks the user a question about AI and returns their input.

    If the user wants to exit, they can enter "exit".

    Returns:
    - user_input (str): The user's input.
    """
    user_input = input("What would you like to know about AI? (enter exit if you want to exit): ")
    return user_input


def find_similarities(questions_list:list, user_input:str) -> list:
    """
    Uses keywords to find similarities. 
    Returns up to 3 closest hits.

    Args:
    - questions_list (list): A list of Question objects.
    - user_input (str): The user's input which is the question they ask.

    Returns:
    - tuple: A list containing the up to 3 closest hits.
    """
    similar_questions = []

    for question_object in questions_list:

        keywords_found = []

        for keyword in question_object['keywords']:
            if keyword.lower() in user_input.lower():
                keywords_found.append(keyword)


        keywords_found_amount = len(keywords_found)
        if keywords_found:
            similar_questions.append({'keywords_amount':keywords_found_amount, 'question':question_object})
    
    similar_questions.sort(key=lambda similarity: similarity['keywords_amount'])
    return similar_questions[:2]


def show_similar_questions(similarities:list):
    """
    Prints a list of questions that are similar to the one provided.

    Args:
    - similarities (list): A list of dictionaries containing information about similar questions.
    """
    if not similarities:
        print("Sorry, we do not know of a question similar to the one you gave")
    else:
        print("Here are the questions with similarities with the one you gave")

        question_number = 0
        for similarity in similarities:
            question_number += 1
            print(f"{question_number}) {similarity['question']['question']}")


def ask_user_a_choice(max_number:int) -> int:
    """
    Asks the user to input a number between 1 and max_number and returns the choice.

    Args:
    - max_number (int): the maximum number the user can choose.

    Returns:
    - choice (int): the number chosen by the user.
    """
    user_input = input(f'Please enter the number of your question between 1 and {max_number} : ')

    while True:
        try:
            choice = int(user_input)
            if choice > 0 and choice <= max_number:
                break
        except ValueError:
            user_input = input(f"Wrong input, please enter a number between 0 and {max_number}")

    return choice


def show_an_answer(question_object:dict):
    """
    Prints the question and answer from a given question object.

    Args:
    - question_object (dict): A dictionary containing a 'question' and 'answer' key.
    """
    output_message = f"The question is : {question_object['question']}\n"
    output_message += f"The answer :\n\n{question_object['answer']}\n"
    print(output_message)

def user_wants_to_continue(user_input:str)-> bool:
    """ Checks user_input:str and returns False if it says 'exit', else True. """

    if user_input == "exit":
        return False
    return True


def main():
    questions_list = get_questions(FILE_PATH)
    if questions_list:  # if the program fail to open/read the file we stop it

        user_input = ask_user_a_question()

        while user_wants_to_continue(user_input):
            similarities = find_similarities(questions_list, user_input)
            show_similar_questions(similarities)
            if similarities:
                user_choice = ask_user_a_choice(len(similarities))
                show_an_answer(similarities[user_choice - 1]['question'])

            user_input = ask_user_a_question()

    exit("The program is ending")


if __name__ == "__main__":
    main()