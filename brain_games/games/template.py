import prompt


def is_greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even_desc():
    print('Answer "yes" if the number is even, otherwise answer "no"')


def calc_desc():
    print('What is the result of the expression?')


def gcd_desc():
    print('Find the greatest common divisor of given numbers.')


def progression_desc():
    print('What number is missing in the progression?')


def prime_desc():
    print('Answer "yes" if the number is prime, otherwise answer "no"')


def wrong_answer():
    return "is wrong answer ;(. Correct answer was"
