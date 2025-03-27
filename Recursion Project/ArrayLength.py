def recursive_length(lst):  
    
    if not lst:
        return 0 
    return 1 + recursive_length(lst[1:])

arr = [1, 2, 234, 234, 745, 3, 6, 653]
print("Length of array:", recursive_length(arr))
