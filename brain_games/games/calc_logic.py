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
         if r_exprssn == '+':
             pluse = r_num + r_num2
             if pluse == int(ans):
                 print('Correct!')
                 count_correct += 1
             else:
                 print(f"'{ans}' is wrong answer ;(. Correct answer was '{pluse}'")
                 print(f"Let's try again, {temp}!")
                 break
         
         elif r_exprssn == '-':
             minus = r_num - r_num2
             if minus == int(ans):
                 print('Correct!')
                 count_correct += 1
             else:
                 print(f"'{ans}' is wrong answer ;(. Correct answer was '{minus}'")
                 print(f"Let's try again, {temp}!")
                 break
         
         elif r_exprssn == '*':
             multiply = r_num * r_num2
             if multiply == int(ans):
                 print('Correct!')
                 count_correct += 1
             else:
                 print(f"'{ans}' is wrong answer ;(. Correct answer was '{multiply}'")
                 print(f"Let's try again, {temp}!")
                 break
    if count_correct == 3:
        print(f'Congratulations, {temp}')

