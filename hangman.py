
secretWord = "Haider"
numOfLetters = len(secretWord)
numOfLettersGuessed = 0
correct = 0
lettersAlreadyGuessed = ""
userAnswer = ""
theWordis = ""
theWordis = ["_,"] * numOfLetters

print(theWordis)

choice = raw_input("Do you want to play HANG MAN game:")

if(choice== "yes"): 

    while numOfLettersGuessed != numOfLetters:

        userAnswer = raw_input("Guess a Letter: ")

        if userAnswer in secretWord and  userAnswer not in lettersAlreadyGuessed:
            correct+=1
            lettersAlreadyGuessed ="".join(userAnswer)           
            indexW = secretWord.index(userAnswer)
            theWordis[indexW]= userAnswer
        

        print(theWordis)
        numOfLettersGuessed+=1
else:
    print("Bye Bye !")


if(correct==len(secretWord)):
    print("You won !")
else:
    print("You lost !")


