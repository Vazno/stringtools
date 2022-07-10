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
# Importing random sentence to function
@pytest.mark.parametrize("sentence", ["".join([random.choice(string.ascii_lowercase) for i in range(random.randint(50, 100))])])
# Choosing random boolean
@pytest.mark.parametrize("lowercase", [bool(random.randint(0, 1))])
def test_count_char(sentence, lowercase):
	from stringtools import count_char

	# Created second random function, to test function, it works slower
	def count_char_two(sentence, lowercase):
		if sentence != "":
			if not lowercase:
				# Generating dictionary from sentence
				# Which should look like this:
				# dict.fromkeys(['one', 'two', 'three', 'four'], 0) -> {'one': 0, 'two': 0, 'three': 0, 'four': 0}
				string_dict = dict.fromkeys(set(sentence), 0)
			else:
				sentence = sentence.lower()

				# Generating dictionary from lowecased sentence
				string_dict = dict.fromkeys(set(sentence), 0)
			for char in sentence:
				# Adding + 1 for each character's (key's) value
				string_dict[char] += 1
			return string_dict
		else:
			return dict()
	assert count_char(sentence, lowercase) == count_char_two(sentence, lowercase)