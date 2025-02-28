import random

def hangman():
    word = generateWord()
    hiddenWord = hideWord(word)

    numberOfMisses = 0

    while (word != hiddenWord):
        guess = input(f"(Guess) Enter a letter in word {hiddenWord} > ").strip()

        if guess not in word:
            numberOfMisses += 1
            print(f"\t{guess} is not in the word")

        elif guess in hiddenWord:
            print(f"\t{guess} is already in the word")

        else:
            hiddenWord = updateWord(guess, word, hiddenWord)


    print(f"The word is {word}. You missed {numberOfMisses}", end = " ")
    print("time" if numberOfMisses == 1 else "times")


    userInput = input("Do you want to guess another word? Enter y or n > ").upper()
    if userInput == 'Y':
        hangman()
    else:
        print("Thank you for playing. Have a nice day!")
    


def generateWord():
    words = ["banana", "apple", "strawberry", "mango", "coconut", "papaya"]

    return words[random.randrange(len(words))]


def hideWord(word):
    hiddenWord = ""

    for i in word:
        hiddenWord += '*'

    return hiddenWord


def updateWord(guess, word, hiddenWord):
    updatedWord = ""

    for i in range(len(hiddenWord)):
        if hiddenWord[i] != '*':
            updatedWord += hiddenWord[i]
        else:
            if guess == word[i]:
                updatedWord += guess
            else:
                updatedWord += '*'


    return updatedWord


def main():
    hangman()


main()
