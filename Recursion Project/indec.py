def indec(n,num):

    if n < 1 or n > num:
        return
    
    print(n)

    indec(n - 1, num)

    print(n)


n = int(input("Enter any number n:"))

indec(n,n)