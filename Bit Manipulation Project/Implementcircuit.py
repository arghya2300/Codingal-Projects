def bitwise_operations(a, b):
    and_result = a & b
    or_result = a | b
    xor_result = a ^ b
    not_a = ~a
    return and_result, or_result, xor_result, not_a

a, b = 5, 3
print(bitwise_operations(a, b))