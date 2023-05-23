from brain_games.games.template import is_greeting, even_desc, wrong_ans
import prompt
from random import randint


def is_even():
    name = is_greeting()
    even_desc()
    count_correct = 0
    while count_correct < 3:
        r_num = randint(0, 99)
        print(f'Question: {r_num}')
        ans = prompt.string('Your answer: ')
        if r_num % 2 == 0 and ans == 'yes' or r_num % 2 != 0 and ans == 'no':
            count_correct += 1
            print('Correct!')
        elif r_num % 2 != 0 and ans == 'yes':
            print(f"'{ans}' {wrong_ans()} 'no'")
            print(f"Let's try again, {name}!")
            count_correct = 0
            break
        elif r_num % 2 == 0 and ans == 'no':
            print(f"'{ans}' {wrong_ans()} 'yes'")
            print(f"Let's try again, {name}!")
            count_correct = 0
            break
        else:
            print(f"'{ans}' {wrong_ans()} 'yes'")
            print(f"Let's try again, {name}")
            count_correct = 0
            break
    if count_correct == 3:
        print(f'Congratulations, {name}!')
