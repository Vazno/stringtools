from random import choice
import string
def test_bricks():
	from stringtools.myfunctions import bricks
	# Generating random string
	_string = ""
	for i in range(50):
		_string += choice(list(string.printable))
	# Creating bricked version
	bricked_string = ""
	_counter = 0
	# Generating bricked strings from randomly generated string
	for char in _string:
		if _counter == 0:
			bricked_string += char.upper()
			_counter +=1
		else:
			bricked_string += char.lower()
			_counter = 0
	assert bricked_string == bricks(_string)