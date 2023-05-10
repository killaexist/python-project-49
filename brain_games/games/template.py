import prompt


def is_greeting():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def wrong_answer():
    return "is wrong answer ;(. Correct answer was"
