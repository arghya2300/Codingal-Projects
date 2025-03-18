def headrec(num, inputnumber):
    if num > inputnumber:
        return
    headrec(num + 1, inputnumber)

    print(num)

inputnumber = int(input("Enter n to print 1 to n:"))

headrec(1,inputnumber)


