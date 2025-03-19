def reverse_bits(n):
    reversed_num = 0
    while n > 0:
        reversed_num = (reversed_num << 1) | (n & 1)
        n = n >> 1
    return reversed_num

# Example usage:
n = int(input("enter value"))
print(f"Reversed Number: {reverse_bits(n)}")