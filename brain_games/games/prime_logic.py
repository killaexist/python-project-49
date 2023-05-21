import prompt
from random import randint
from brain_games.games.template import wrong_answer, is_greeting, prime_desc


def is_prime():
    name = is_greeting()
    prime_desc
    count_correct = 0
    while count_correct < 3:
        r_num = randint(0, 99)
        print(f'Question: {r_num}')
        ans = prompt.string('Your answer: ')
        for prime in range(2, r_num):
            if r_num % num == 0 and ans == 'no' or r_num % num != 0 and ans == 'yes':
                count_correct += 1
                print('Correct!')
                break
            elif r_num % prime == 0 and ans == 'yes':
                print(f"'yes' {wrong_answer()} 'no'")
                print(f"Let's try again, {name}!")
                count_correct += 5
                break
            elif r_num % prime != 0 and ans == 'yes':
                count_correct += 1
                print('Correct!')
                break
            elif r_num % prime != 0 and ans == 'no':
                print(f"'no' {wrong_answer()} 'yes'")
                print(f"Let's try again, {name}!")
                count_correct += 5
                break
            else:
                print(f"'{ans}' {wrong_answer()} 'yes'")
                print(f"Let's try again, {name}")
                break

        if count_correct > 3:
            break
        elif count_correct == 3:
            print(f'Congratulations, {name}!')



