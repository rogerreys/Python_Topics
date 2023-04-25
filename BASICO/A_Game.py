import random

def header(computer_wins, user_wins,rounds):
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)


def game_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1
    return user_wins, computer_wins


def choice_options():
    options = ('piedra', 'papel', 'tijera')

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
      print('esa opcion no es valida')
      return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    
    return user_option, computer_option


def choice_winner(computer_wins, user_wins, time):
    if computer_wins == 2:
        time = False
        return 'El ganador es la computadora', time

    if user_wins == 2:
        time = False
        return 'El ganador es el usuario', time
    return None, time

def run_game():
    computer_wins = 0
    user_wins = 0

    rounds = 1
    time = True
    while time:

        header(computer_wins, user_wins, rounds)
        
        user_option, computer_option = choice_options()
        
        rounds += 1

        user_wins, computer_wins = game_rules(user_option, computer_option, user_wins, computer_wins)
        
        winner, time = choice_winner(computer_wins, user_wins, time)
    print("GANADOR: ", winner)
            
run_game()