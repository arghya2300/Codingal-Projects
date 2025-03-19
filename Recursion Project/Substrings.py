def find_substrings(s):
    substrings = []
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    
    return substrings

s = input("Enter a string: ")
result = find_substrings(s)

print("\nAll substrings are:")
for substring in result:
    print(substring)
