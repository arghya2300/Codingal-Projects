def longest_ones(n):
    count = 0
    max_count = 0
    
    while n > 0:
        if n & 1:  
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
        n = n >> 1  
    
    return max_count


n = int(input("Enter a number: "))
result = longest_ones(n)

print(f"Longest consecutive 1's in binary representation of {n}: {result}")
