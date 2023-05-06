from brain_games.template import is_greeting
import prompt
from random import randint


def is_calc():
    temp = is_greeting()
    print('What is the result of the expression?')
    print(f'Hello, {temp}')