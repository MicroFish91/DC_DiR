# fillCorrectChars():
# Takes a userChar (e.g. 'a'), and looks for cases where it exists in referenceWord.
# Wherever it finds a match, it replaces the '_' with the guessed letter in the same index
def fillCorrectChars(userChar, userWord, referenceWord):

    output = []

    for index, char in enumerate(referenceWord):
        if char == userChar:
            output.append(userChar)
        elif char != '_':
            output.append(userWord[index])
        else: 
            output.append('_')
    
    return ''.join(output)




# ****** MAIN STARTS HERE ******

# Uncomment the 3 lines under this and comment out line 29 if you want to run without taking a user input
# import random

# hangWords = ["python", "javascript", "ruby", "html", "css", "node", "react" ]
# hangWord = random.choice(hangWords)

hangWord = input("What word would you like to use? ").lower()

userWord = "_" * len(hangWord)
numCorrect = 0
userLives = 9

while userLives > 0:
    print(f'Hangman: {userWord} ')
    print(f'You have {userLives} lives remaining.')

    userInput = input("Please enter your guess (one letter) or guess the whole word: ").lower()

    # If you guess the whole word at once you win automatically
    if userInput == hangWord:
        print(f'You win with {userLives} lives remaining!')
        break
    # If you guess the whole word using one letter at a time
    elif numCorrect == len(hangWord) - 1:
        print(f'You win with {userLives} lives remaining!')
        break
    # Else-if your letter is within the hangWord
    elif userInput in hangWord:
        count = hangWord.count(userInput)
        # Makes sure we aren't counting a letter that was previously correct
        if userInput not in userWord:
            numCorrect += count
        # Here we use a function that we built at the top
        userWord = fillCorrectChars(userInput, userWord, hangWord)  
        print(f'Correct! There was {count} \'{userInput}\'(s)!')
    # Else: If your guess was wrong
    else:
        print('Wrong, nice try...')
        userLives -= 1

# If you hit 0 lives, you exit the loop and display the lose message
if userLives == 0:
    print('You have 0 lives remaining.  You lose...')