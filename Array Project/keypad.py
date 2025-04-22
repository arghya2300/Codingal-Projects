keypad = ["","","abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wyz"]


def printCombination(combination, curr, output, n):

    if curr == n:
        print(output,sep=",")
        return
    

    if combination[curr] == 0 or combination[curr] == 1:
        return
    
    for letter in keypad[combination[curr]]:
        output.append(letter)

        printCombination(combination, curr + 1, output, n)
        output.pop()

combination = [4,3]
n = len(combination)


printCombination(combination, 0, [], 2)
