import time
import matplotlib.pyplot as plt



def layup_sequence(n: int) -> int:
	"""
	Implement the Layup Sequence defined for n as:
	S(n) =
		1 if n = 1
		2 if n = 2
		S(n-1) + S(n-2)   if n is even
		2*S(n-1) - S(n-2) if n is odd

	Returns:
		The value of the layup sequence for n. Returns null if n <= 0 or n is not an integer.

	Analysis:
		This solution is implemented with recursion so although it is the simplest, it will
		not scale for large values of n. The runtime of this solution is approximately O(2^N)
		where each increment of N roughly doubles the amount of function calls.
	"""
	if type(n) != int:
		return None

	if (n <= 0):
		return None

	if (n == 1 or n == 2):
		return n

	if (n % 2 == 0):
		return layup_sequence(n-1) + layup_sequence(n-2)
	else:
		return 2*layup_sequence(n-1) - layup_sequence(n-2)


def main():
	""" Visualize the runtime complexity of the implementation. """

	# Measure the runtime
	max_value = 20
	n = list(range(1, max_value+1))
	latency = []
	for n_value in n:
		print(f"Calculating layup_sequence for n: " + str(n_value))
		start = time.time()
		layup_sequence(n_value)
		latency.append(time.time() - start)

	# Generate the visual
	fig, ax = plt.subplots()
	ax.plot(n, latency)
	ax.set_xticks( list( range(0, max_value+1, 5) ))
	ax.set(xlabel='N', ylabel='time (s)',
       title='Latency of Layup Sequence Algorithm')
	ax.grid()
	plt.show()


if __name__ == '__main__':
	main()
