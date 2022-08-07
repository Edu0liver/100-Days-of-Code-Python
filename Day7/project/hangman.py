import random
import hangman_art
import hangman_words

random_word = random.choice(hangman_words.word_list)

word_length = len(random_word)
random_word_array = []

for _ in range(word_length):
    random_word_array += "_"

game_over = False
lives = 6

print(hangman_art.logo)

while not game_over:
    letter_choice = input("Guess a letter: ").lower()

    for letter_index in range(word_length):
        if letter_choice == random_word[letter_index]:
            random_word_array[letter_index] = letter_choice

    if letter_choice not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("\nYOU LOSE!")
            print(f"The word was {random_word}")

    if "_" not in random_word_array:
        game_over = True
        print("\nYOU WIN!")


    print(f"{random_word_array}\n")
    print(f"{hangman_art.stages[lives]}")