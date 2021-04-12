import random 

words = [ "pizza", "fairy", "shirt", "plane", "javascript" ]




lives = 9
secret_word = random.choice(words)
clue = []
for x in secret_word:
    clue.append('_')
print(secret_word)

def update_clue(guessed_letter):

    index = 0 
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter 
        index += 1

while lives > 0:

    print(clue)
    print(f"You have {lives} remaining")
    #show the number of characters needed to guess 
    # input characters 
    guess = input('guess a letter or the whole world: ')

    if guess in secret_word : 
    # function update our clue
    # check to see if its true 
        update_clue(guess)
    else: 
        lives -= 1
        print('incorrect you lose a life!')
        
    # if true: see the word with guess in it
    #if word has been guessed , hop out of while loop
    # false ...
        # decrement lives count
        # 
    
    
    

