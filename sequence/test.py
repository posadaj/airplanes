from main import layup_sequence

def test_base_cases():
	assert layup_sequence(1) == 1
	assert layup_sequence(2) == 2

def test_simple_odd():
	assert layup_sequence(3) == 3

def test_simple_even():
	assert layup_sequence(4) == 5