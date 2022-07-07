'''
MIT License

Copyright (c) 2022 Beksultan Artykbaev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import string
import pytest
import random
@pytest.mark.parametrize("TEST_SIZE", [random.randint(50, 100)])
def test_bricks(TEST_SIZE):
	from stringtools import bricks
	# Generating random string
	_string = ""
	for i in range(TEST_SIZE):
		_string += random.choice(list(string.printable))
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