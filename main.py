from words import word_list
from art import logo, stages
from os import system
from random import choice

system("cls")
print(logo)

random_word = choice(word_list)
random_word_dashed = ['_'] * len(random_word)
total_lives = 6

# # DEBUG
# print(random_word)
# #

def update_dashes(random_word_dashed, guess_letter):
    for index, letter in enumerate(random_word):
        if letter == guess_letter:
            random_word_dashed[index] = letter
    return random_word_dashed

while '_' in random_word_dashed and total_lives != 0:
    guess_letter = input("Guess a letter: ").lower()
    if guess_letter not in random_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        print(' '.join(random_word_dashed))
        total_lives -= 1
        print(stages[total_lives - len(stages)])
    elif guess_letter in random_word_dashed:
        print(f"You've already guessed {guess_letter}")
        print(' '.join(random_word_dashed))
        print(stages[total_lives - len(stages)])
    else:
        random_word_dashed = update_dashes(random_word_dashed, guess_letter)
        print(' '.join(random_word_dashed))
        print(stages[total_lives - len(stages)])

if total_lives == 0:
    print("You lose 😭")
else:
    print("You win 🎉")