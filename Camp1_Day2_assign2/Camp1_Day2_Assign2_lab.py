from random import randint
GuessNumber = randint(1, 10)
if __name__ == '__main__':
    #print(GuessNumber)
    while True:
        InputNumber = input("Guess the number: ")
        if(int(InputNumber) == GuessNumber):
            print("Correct! ")
            break
        else:
            print("Wrong, try again! ")
