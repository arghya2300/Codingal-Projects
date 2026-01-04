def a_and_b(a, b):
    if a == 1:
        prob_student = 0.3 
        if b == 1:
            prob_dining = 0.75
        else:
            prob_dining = 0.25
        print("the probability of given b is", prob_dining)
            
    if a == 2:
        prob_student = 0.7 
        if b == 1:
            prob_dining = 0.6
        else:
            prob_dining = 0.4
        print("the probability of given b is", prob_dining)
    global prob_a_and_b
    prob_a_and_b = prob_student*prob_dining
    return round(prob_a_and_b, 3)


print("is student a freshman?")
a = int(input("Enter 1 or 2: \n 1) yes \n 2) no \n"))

print("is student eating in the dining hall?")
b = int(input("Enter 1 or 2: \n 1) yes \n 2) no \n"))


print("here is the probability of the events occuring:", a_and_b(a,b))