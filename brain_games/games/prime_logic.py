import prompt
from random import randint
from brain_games.games.template import wrong_ans, is_greeting, prime_desc


def is_prime():
    name = is_greeting()
    prime_desc
    count_correct = 0
    count_prime = 0
    while count_correct < 3:
        r_num = randint(0, 99)
        print(f'Question: {r_num}')
        ans = prompt.string('Your answer: ')
        for prime in range(2, r_num):
            if r_num % prime == 0:
                count_prime += 1
                break
        if count_prime == 1 and ans == 'no':
            print('Correct!')
            count_prime = 0
            count_correct += 1
        elif count_prime == 1 and ans == 'yes':
            print(f"'{ans}' {wrong_ans()} 'no'")
            print(f"Let's try again, {name}!")
            break
        elif count_prime == 0 and ans == 'yes':
            print('Correct!')
            count_prime = 0
            count_correct += 1
        elif count_prime == 0 and ans == 'no':
            print(f"'{ans}' {wrong_ans()} 'yes'")
            print(f"Let's try again, {name}!")
            break
    if count_correct == 3:
        print(f'Congratulations, {name}!')
