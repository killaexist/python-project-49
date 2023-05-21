import prompt
from random import randint
from brain_games.games.template import wrong_answer, is_greeting, progression_desc

def is_progression():
    name = is_greeting()
    progression_desc()
    count_correct = 0
    list_num = []
    list_str = ''
    while count_correct < 3:
        first_num = randint(0, 99)
        step = randint(2, 10)
        len_list = randint(5, 10)
        hide_index = randint(1, len_list - 1)
        for x in range(len_list):
            first_num = first_num + step
            list_num.append(first_num)
        list_num[hide_index] = '..'
        for c in list_num:
            list_str += str(c) + ' '
        print(f'Question: {list_str}')
        ans = prompt.string('Your answer: ')
        if list_num[hide_index - 1] + step == int(ans):
            print('Correct!')
            count_correct += 1
            list_str = ''
            list_num = []
        else:
            print(f"'{ans}' {wrong_answer()} '{list_num[hide_index - 1] + step}'")
            print(f"Let's try again, {name}!")
            break
    if count_correct == 3:
        print(f'Congratulations, {name}!')





