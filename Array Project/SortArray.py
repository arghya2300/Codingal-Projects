def sort(A):
    for i in range(0,len(A)):
        for j in range(i+1, len(A)):
            if A[i] >= A[j]:
             A[i], A[j] = A[j], A[i]
    return A

a = [10,55,30,5,2]
print("original Array", a)
print("\n sorted array", sort(a))
