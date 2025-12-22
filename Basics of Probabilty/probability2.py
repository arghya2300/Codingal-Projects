import random

total_outcomes = 6
favorable_outcomes = 1 
probability = favorable_outcomes / total_outcomes

print("Probability of getting a 6 on the first throw:", probability)

roll = random.randint(1, 6)
print("You rolled:", roll)

if roll == 6:
    print("Game can be started")
else:
    print("Roll again")