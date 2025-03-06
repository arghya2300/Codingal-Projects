def first_set_bit(n):
    if n == 0:
        return 0
    position = 1
    while n:
        if n & 1:
            return position
        n = n >> 1
        position += 1

number = int(input("enter the number:"))
print(f"Position of the first set bit: {first_set_bit(number)}")