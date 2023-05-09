from brain_games.games.template import is_greeting
import prompt
from random import randint
from random import choice


def is_calc():
    temp = is_greeting()
    print('What is the result of the expression?')
    exprssn = ['+', '*', '-']
    count_correct = 0
    while count_correct < 3:
         r_num = randint(0, 99)
         r_num2 = randint(0, 99)
         r_exprssn = choice(exprssn)
         print(f'Question: {r_num} {r_exprssn} {r_num2}')
         ans = prompt.string('Your answer: ')
         if (r_num int(r_exprssn) r_num2) == int(ans):
              count_correct += 1
              print('Correct!')


