import random


game_logo = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▄▄█░██░█░▄▄█░▄▄█░▄▄███▄░▄█░████░▄▄███░▄▄▀█░██░█░▄▀▄░█░▄▄▀█░▄▄█░▄▄▀
█░█▄▀█░██░█░▄▄█▄▄▀█▄▄▀████░██░▄▄░█░▄▄███░██░█░██░█░█▄█░█░▄▄▀█░▄▄█░▀▀▄
█▄▄▄▄██▄▄▄█▄▄▄█▄▄▄█▄▄▄████▄██▄██▄█▄▄▄███▄██▄██▄▄▄█▄███▄█▄▄▄▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """

total_chances = ['💖','💖','💖','💖','💖']
win_emoji = '🏆🎉'
lose_emoji = '💔😭'

def game():

    print(game_logo)

 # generating a random number beween 1 and 100
    correct_number=random.randint(1,100) 

#initializing
    while total_chances.count('💖') > 0:
        gussed_number=int(input("Guess a number between 1 to 100: ")) 

#gussed number is greater than correct number
        if gussed_number > correct_number:
            total_chances.remove('💖')
            total_chances.append('💔')
            print(f"You Guess is too high, you have lost an attempt {total_chances}")

#gussed number is lower than correct number
        elif gussed_number < correct_number:
            total_chances.remove('💖')
            total_chances.append('💔')
            print(f"You Guess is too low, you have lost an attempt {total_chances}")

#gussed number is equal to correct number
        else:
            print(f"You have gotten the correct number, You've won {win_emoji}")
            break
#all chances are used
    
    if total_chances.count('💖') == 0: 
        print(f"You're out of chances, You've lost {lose_emoji}") 



game()
