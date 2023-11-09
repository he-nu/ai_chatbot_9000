#! /usr/bin/python3.10
import json
import re

# KEYWORDS:list = ...


def get_questions(file_path:str)-> dict:
    ...


def ask_user_input():
    user_input = input("What would you like to know about AI?")
    return user_input



def find_similarities(keywords_list:list, user_input:str) -> list:
    """ Uses regular expressions to find similarities. 
    Returns up to 3 closest hits."""
    ...

def main():
    questions = get_questions()
    user_input = ask_user_input()
    similarities = find_similarities()



