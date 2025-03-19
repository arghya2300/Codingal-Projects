def fac(n):
    if n == 1 or n == 0:
        return 1
    return n * fac(n - 1)

n = int(input("Enter a number: "))
result = fac(n)
print(f"Factorial of {n} is: {result}")


def print1to10(n):
    if n > 10:
        return
    print(n)
    print1to10(n + 1)

number2 = int(input("Enter a number: "))

print1to10(number2)
