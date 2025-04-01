def paren(S, l, r, p, n):
    if p == 2 * n:
        for ss in S:
            print(ss,end="")
        print("\n")
        return
    
    if l > r:
        S[p] = "}"
        paren(S, l, r + 1, p + 1, n)

    if l < n:
        S[p] = "{"
        paren(S, l + 1, r, p + 1, n)

n = int(input("Enter the number of parentheses: "))
S = [" "] * (2 * n)
print("\n Balanced parentheses combination:\n")
paren(S, 0, 0, 0, n)
