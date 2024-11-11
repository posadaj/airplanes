from main import layup_sequence

def test_base_cases():
	assert layup_sequence(1) == 1
	assert layup_sequence(2) == 2

def test_simple_odd():
	assert layup_sequence(3) == 3

def test_simple_even():
	assert layup_sequence(4) == 5

def test_couple_iterations():
	assert layup_sequence(7) == 17

def test_10k():
	result = layup_sequence(10000)
	print("Layup sequence for n=10,000 is: " + str(result))
	assert True