import random
def hangman():
    words=["dog","book","betting","exams","rocket","science"]
    letters=""
    disword=random.choice(words)
    
    print("welcome to hangman")
    life=10
    while life<20:
        guess=input("enter your guess" )
        if guess in disword:
            print("you are close correct guess")
            letters=letters+guess
            if len(letters)==len(disword):
                print("you won!!! the word was",disword)
                break
            else:
                lettersleft= len(disword)-len(letters)
                print("you have",lettersleft,"letters left")
        else:
            life=life-1
            if life==0:
                print("game over, the word was",disword)
                break
            else:
                print(life,"life left")
hangman()