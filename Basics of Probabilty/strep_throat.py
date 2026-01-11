def find_prob(a,b):
    
    if a == 1:
        prob_a = 0.2
        
        if b == 1:
            prob_bga = 0.85
        elif b == 2:
            prob_bga = 0.15
        else:
            print("Invalid value")
        
        prob_a_and_b = prob_a * prob_bga
        
        print("probability of b given a is ", prob_bga)
        print("probability of both events occuring", prob_a_and_b)
        
a = 1
b = 2   

print("probabilites for a and b is:")
find_prob(a,b)