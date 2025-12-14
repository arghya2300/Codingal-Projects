import random

ball = ['red', 'blue', 'green', 'yellow', 'black']
result = random.choice(ball)

print(ball.count('red'), "/",len(ball))

if result == 'red':
    print("you win")
else:
    print("loser")
