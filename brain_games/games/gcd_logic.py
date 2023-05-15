from brain_games.games.template import is_greeting, gcd_desc, wrong_answer
import prompt
from random import randint


def is_gcd():
    name = is_greeting()
    gcd_desc()
    count_correct = 0
    list_divider = []
    while count_correct < 3:
        r_num = randint(0, 99)
        r_num2 = randint(0, 99)
        print(f"Question: {r_num} {r_num2}")
        ans = prompt.string("Your answer: ")
        for divider in range(1, max(r_num, r_num2)):
            if r_num % divider == 0 and r_num2 % divider == 0:
                list_divider.append(divider)
        if int(ans) == max(list_divider):
            print('Correct!')
            count_correct += 1
            list_divider = []
        else:
            print(f"'{ans}' {wrong_answer()} '{max(list_divider)}'")
            print(f"Let's try again, {name}!")
            break
    if count_correct == 3:
        print(f'Congratulations, {name}!')
