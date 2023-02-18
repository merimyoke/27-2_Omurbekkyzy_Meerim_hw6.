from decouple import config
from random import randint, choice


def casinoLogic():
    budget = config('MY_MONEY', cast=int)
    while True:
        user_question = input('do you want to play? yes/no: ')
        print(f'your budget is {budget}$')
        user_input_number = (int(input('please write down a number from 1 to 30: ')))
        user_input_money = (int(input('how much are you willing to bet? ')))
        my_list = [randint(1, 30)]
        generate_number = choice(my_list)

        if generate_number == user_input_number and user_question == 'yes':
            win = user_input_money * 2
            budget += win
            return f'generated number is: {generate_number}, you won {win}, your total cash is: {budget}'
        elif generate_number != user_input_number and user_question == 'yes':
            lose = user_input_money
            budget -= lose
            return f'generated number is: {generate_number},you lost {lose}, your total cash is: {budget}'
        elif user_question == 'no':
            print(f'your total: {budget}')
            break
        elif user_question != 'yes' and user_question != 'no':
            return 'please write yes or no'
