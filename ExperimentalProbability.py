import random


count = 0
win = 0


while count<1000000:
    computernumber1 = random.randint(0,6)
    computernumber2 = random.randint(0,6)
    comuternumberx = computernumber1 * computernumber2
    randomguess = random.randint(0,36)
    if randomguess == comuternumberx:
        win +=1
    count+=1

probability = win/count

print("The probability of guessing the correct number is",probability)
