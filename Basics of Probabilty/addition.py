g_even = {2,4,6}
g_two = {2,3,4,5,6}
total_outcomes = {1,2,3,4,5,6}

def probability(g_even,g_two, total_outcomes):
    
    pro_even = len(g_even) / len(total_outcomes)
    pro_G_Two = len(g_two) / len(total_outcomes)
    
    intersection = g_even.intersection(g_two)
    pro_of_intersection = len(intersection) / len(total_outcomes)
    
    return pro_even + pro_G_Two - pro_of_intersection
    
print(probability(g_even,g_two, total_outcomes))  