("""Simple utilities for Day01 exercises.

Contains a safe implementation of `factorial(n)` with a small CLI demo.
""")

def factorial(n):
	"""Return n! (factorial of n).

	Args:
		n (int): non-negative integer

	Returns:
		int: n factorial

	Raises:
		TypeError: if `n` is not an int
		ValueError: if `n` is negative
	"""
	if not isinstance(n, int):
		raise TypeError("n must be an integer")
	if n < 0:
		raise ValueError("n must be non-negative")

	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1:
		try:
			value = int(sys.argv[1])
			print(factorial(value))
		except Exception as e:
			print("Error:", e)
	else:
		# demo: print small factorials
		for i in range(6):
			print(f"{i}! =", factorial(i))

