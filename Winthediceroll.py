import random
count = 0
Computer_score = 0
Player_score = 0
numbers = [1,2,3,4,5,6]
player1number = int(input("Player 1Enter an integer between 1 and 6 inclusive as close to the computer's number"))
while count<60 :
    computernumber = numbers[random.randint(0,5)]
    if  computernumber == player1number:
        Player_score = Player_score+1
    count +=1
print("Out of 60 dice rolls you won",Player_score,"times" )
