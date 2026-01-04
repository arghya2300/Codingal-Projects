def a_and_b(orange, blue,total):
    pro_o = orange / total
    pro_bgo = blue / (total - 1)
    pro_o_and_b = pro_o * pro_bgo
    return round(pro_o_and_b, 3)

orange = 5
blue = 6
total = orange + blue

print("The probability of getting 1st orange and 2nd blue ball is: \n", a_and_b(orange, blue,total))


