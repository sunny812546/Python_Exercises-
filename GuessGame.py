# no of guess
# print lesft guess
# you took to finish
# game over

guessno = 9
guesses = 8
step = 0

while(True):
    num = int(input("Guess a number"))
    if guesses<2:
        print("Game Over")
        break
    elif num==guessno:
        step = step + 1
        print(f"congrates you took {step} steps to finish\n")
        break
    elif (num)>guessno:
        step = step + 1
        guesses = guesses - 1
        print(f"Number may be lesser than  {num}",end=" ")
        print("Left steps",guesses)
    elif (num)<guessno:
        step = step + 1
        guesses = guesses - 1
        print(f"Number may be greater than  {num}",end=" ")
        print("Left steps",guesses)
    
            