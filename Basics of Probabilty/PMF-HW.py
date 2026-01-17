import math

n = 10
p = 0.5

prob = 0
for k in range(2, 5): 
    prob += math.comb(n, k) * (p**k) * ((1-p)**(n-k))

print("The probability of getting between 2 and 4 heads in 10 tosses of a fair coin is:", prob)