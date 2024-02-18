import random
print(f"---------\n You guess a, that's not in the word. You lose a life")
print('''
 ___                                                                       
(   )                                                                      
 | | .-.     .---.   ___ .-.     .--.    ___ .-. .-.     .---.   ___ .-.   
 | |/   \   / .-, \ (   )   \   /    \  (   )   '   \   / .-, \ (   )   \  
 |  .-. .  (__) ; |  |  .-. .  ;  ,-. '  |  .-.  .-. ; (__) ; |  |  .-. .  
 | |  | |    .'`  |  | |  | |  | |  | |  | |  | |  | |   .'`  |  | |  | |  
 | |  | |   / .'| |  | |  | |  | |  | |  | |  | |  | |  / .'| |  | |  | |  
 | |  | |  | /  | |  | |  | |  | |  | |  | |  | |  | | | /  | |  | |  | |  
 | |  | |  ; |  ; |  | |  | |  | '  | |  | |  | |  | | ; |  ; |  | |  | |  
 | |  | |  ' `-'  |  | |  | |  '  `-' |  | |  | |  | | ' `-'  |  | |  | |  
(___)(___) `.__.'_. (___)(___)  `.__. | (___)(___)(___)`.__.'_. (___)(___) 
                                ( `-' ;                                    
                                 `.__.
'''
)

word_list = ["levi","cherry","apple"]
display = []
result_display = ""
stages = [ r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= ''', 
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= ''', 
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
#TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)
# print(chosen_word)

for i in chosen_word:
    display += "_"
# print(display)

for i in display:
    result_display += i
print(f"Vui lòng nhập\n{result_display}")

end_of_game = False
while not end_of_game:
    guest = input("Guest a letter")
    # print(len(chosen_word))
    for word in range(len(chosen_word)):
        if guest == chosen_word[word]:
            display[word] = chosen_word[word]
    print(f"kq {display}")
    print(len(stages))
    if guest not in chosen_word:
        lives -= 1
        print(stages[lives]) #stages[index]
        if lives == 0:
            end_of_game = True
            print("You lose")
    if "_" not in display:
        end_of_game = True