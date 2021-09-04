"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, original input
	:return: This function will return the largest digit.
	"""
	if n < 0:		# alter negative inputs into positive
		n *= -1
	ans = helper(n, 0, 0)
	return ans


def helper(n, x, ans):
	"""
	:param n: int, original input
	:param x: int, numbers of digit
	:param ans: int, the largest digit
	return:
		This function will return the largest digit.
	"""
	digit = pow(10, x)		# numbers of digit

	# base case: finish examining all the digits
	if n // digit == 0:
		return ans

	else:
		number = n // digit - n // (digit * 10) * 10		# extract the number we want to examine
		if number > ans:
			ans = number
		return helper(n, x + 1, ans)


if __name__ == '__main__':
	main()
