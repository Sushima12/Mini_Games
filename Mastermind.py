#Mastermind Mini Game
#4 Random Letters will be chosen
#12 Rounds of Guessing, otherwise Player Lose

import random
import string 
def main():
    generated_code = generate_code()
    game_logic(generated_code)

def generate_code():
    #generates the code for player to guess
    letters = ['A','B','C','D','E','F']
    random_letters = random.choices(letters, k = 4)
    return random_letters

def game_logic(code):
    #12 rounds for Players to guess
    print(code)
    secret_code = ['*', '*', '*', '*']
    for round in range(1, 13):
        player_guess = input("Enter your guess: ")
        guess_list = player_guess.replace(' ', '').split(',')
        for x in range(4):
            #check if the guess is correct
            if code[x] == guess_list[x].upper():
                secret_code[x] = code[x]
                print('Code is: ' + secret_code[0] + secret_code[1] + secret_code[2] + secret_code[3])


if __name__ == '__main__':
    main()