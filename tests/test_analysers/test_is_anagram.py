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
from typing import List
import pytest
import random
import string

@pytest.mark.parametrize("TEST_LIST_ONE", [[random.choice(string.printable) for i in range(random.randint(10, 20))]])
@pytest.mark.parametrize("TEST_LIST_TWO", [[random.choice(string.printable) for i in range(random.randint(10, 20))]])
def test_is_anagram(TEST_LIST_ONE: List, TEST_LIST_TWO: List):
	from stringtools import is_anagram

	_first = TEST_LIST_ONE
	random.shuffle(TEST_LIST_ONE)

	assert is_anagram("".join(_first), "".join(TEST_LIST_ONE)) == True
	assert is_anagram("".join(TEST_LIST_ONE), "".join(TEST_LIST_TWO)) == False