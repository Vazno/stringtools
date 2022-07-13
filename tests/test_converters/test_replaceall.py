# MIT License

# Copyright (c) 2022 Beksultan Artykbaev

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
import random
import string
from typing import List
@pytest.mark.parametrize("RANDOM_STRING", ["".join([random.choice(string.ascii_lowercase) for i in range(random.randint(21, 50))])])

# Generating list with random characters
@pytest.mark.parametrize("RANDOM_CHARS", [list(set([random.choice(string.ascii_lowercase + string.punctuation) for i in range(random.randint(25, 50))]))])

@pytest.mark.parametrize("RANDOM_INT", [random.randint(10, 20)])
def test_replaceall(RANDOM_STRING: str, RANDOM_CHARS: List, RANDOM_INT: int):
	from stringtools import replaceall
	_dict = dict()

	# Generating dictionary with random characters
	for i in range(RANDOM_INT-3, 0, -2):
		_dict[RANDOM_CHARS[i]] = str(RANDOM_CHARS[i+1])

	# Checking if function correctly replaces with dictionary it should not contain any keys from dictionary
	assert replaceall(RANDOM_STRING, _dict) not in _dict.keys()

	assert set(RANDOM_STRING) == set(replaceall(RANDOM_STRING, dict())) # Checking empty dictionary