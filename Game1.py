import random
from hangmanart import stages,logo 
from hangmanwords import word_list
from clear import clear


lives = len(stages)-1
display = []

choosen_word=random.choice(word_list)
# print(f'choosen word is {choosen_word}')
word_length = len(choosen_word)
print(logo)
print("if you enter connect word u wont loose life")
print("if u enter wrong word you loose a life")
for _ in range(len(choosen_word)):
    display += "_"
print(display)
end_of_game = False

while not end_of_game:
    guess=input("guess a letter:").lower()
    clear()
    if guess in display:
        print(f"you have already guessed the letter{guess}")
        print(f"Lifes left:{lives}")
    for positon in range(word_length):
        letter = choosen_word[positon]
        if letter ==guess:
            display[positon]=guess
    print(display)
    
    if "_" not in display:
       end_of_game = True
       print("You win")
       
    if guess not in choosen_word:
        print(f'you guessed {guess} is wrong you loose life')
        lives -= 1
        print(f"Lifes left:{lives}")
        if lives == 0:
            end_of_game = True
            print("game over")
            
    print(stages[lives])


