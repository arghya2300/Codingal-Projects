def myrecursion(number):
    if(number>10):
        return
    print(number)
    myrecursion(number + 1)

print(myrecursion(1))