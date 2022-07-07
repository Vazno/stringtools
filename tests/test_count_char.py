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