def tailrec(n,inputnumber):

    if n > inputnumber:
        return
    
    print(n)

    tailrec(n + 1, inputnumber)


inputnumber  = int(input("Enter n to print numbers from 1 to n: "))

tailrec(1,inputnumber)