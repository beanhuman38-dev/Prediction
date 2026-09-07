import random
count = 0
Computer_score = 0
Player_score = 0
numbers = [11, 22, 56, 37, 84, 23, 55, 36, 27, 97, 83, 49, 67, 10, 54, 11, 91, 28, 61, 37, 61, 41, 41, 53, 21, 65, 31, 72, 41, 86, 91, 98, 42, 5, 62, 16, 52, 27, 62, 33, 62, 41, 22, 52, 12, 63, 22, 74, 12, 85, 29, 13, 3, 0]
while count<10 :
    computernumber = numbers[random.randint(0,30)]
    player1number = int(input("Player 1Enter an integer between 0-100 as close to the computer's number"))
    player2number = random.randint(0,100)
    difference1 = abs(player1number - computernumber)
    difference2 = abs(player2number - computernumber)
    if difference1 < difference2:
        Player_score = Player_score+1
    elif difference2 < difference1:
        Computer_score = Computer_score + 1
    count +=1
    print( "Player",Player_score)
    print("Computer", Computer_score)
if Player_score> Computer_score:
    print("Player wins")
elif Player_score < Computer_score:
    print("Computer wins")
