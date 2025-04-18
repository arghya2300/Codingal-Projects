# Python program to find
# length of the longest
# consecutive 1s in
# binary representation of
# a number.

def maxConsecutiveOnes(x):

	# Initialize result
	count = 0

	# Count the number of iterations to
	# reach x = 0.
	while (x!=0):
	
		# This operation reduces length
		# of every sequence of 1s by one.
		x = (x & (x << 1))

		count=count+1
	
	return count

# Driver code

print(maxConsecutiveOnes(14))
print(maxConsecutiveOnes(222))

# This code is contributed
# by Anant Agarwal.
