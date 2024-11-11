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

