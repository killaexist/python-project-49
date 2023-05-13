from brain_games.games.template import is_greeting, wrong_answer, calc_desc
import prompt
from random import randint
from random import choice


def is_calc():
    name = is_greeting()
    calc_desc()
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
                print(f"'{ans}' {wrong_answer()} '{pluse}'")
                print(f"Let's try again, {name}!")
                break
        elif r_exprssn == '-':
            minus = r_num - r_num2
            if minus == int(ans):
                print('Correct!')
                count_correct += 1
            else:
                print(f"'{ans}' {wrong_answer()} '{minus}'")
                print(f"Let's try again, {name}!")
                break
        elif r_exprssn == '*':
            multiply = r_num * r_num2
            if multiply == int(ans):
                print('Correct!')
                count_correct += 1
            else:
                print(f"'{ans}' {wrong_answer()} '{multiply}'")
                print(f"Let's try again, {name}!")
                break
    if count_correct == 3:
        print(f'Congratulations, {name}!')
