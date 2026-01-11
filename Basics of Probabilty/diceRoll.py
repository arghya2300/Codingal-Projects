import numpy as np

die_sides = int(input("Enter the number of sides for dice (6/12): "))
die = range(1, die_sides)

numb_rolls = int(input("Enter the number of rolls u want to roll the dice:"))  

results = np.random.choice(die, size=numb_rolls, replace=True)
print(results)