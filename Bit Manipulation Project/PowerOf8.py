def is_power_of_8(n):
    if n == 0:
        return False
    while n != 1:
        if n % 8 != 0:
            return False
        n = n // 8
    return True

number = int(input("Enter your number: "))

if is_power_of_8(number):
    print(f"Yes, {number} is a power of 8")
else:
    print(f"No, {number} is not a power of 8")