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

@pytest.mark.parametrize("sentence", ["".join([random.choice([random.choice(string.ascii_lowercase), " "]) for i in range(random.randint(500, 1000))]).split(" ")])
def test_is_tautogram(sentence: List):
	from stringtools import is_tautogram
	tautogram_list = []
	random_char = random.choice(string.ascii_letters)
	
	for word in sentence:
		if word.isalpha():
			tautogram_list.append(word.replace(word[0], random_char))
			tautogram_list.append(" ")
	

	assert is_tautogram(sentence="".join(tautogram_list)) == True
	assert is_tautogram(sentence=" ".join(sentence)) == False