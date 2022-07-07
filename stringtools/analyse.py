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
from collections import Counter


def is_pangram(sentence: str, alphabet: str = string.ascii_lowercase) -> bool:
	'''Checks if inputed string is pangram (If it has every letter from aplhabet) e.g:
		
	- 'Watch "Jeopardy!", Alex Trebek\'s fun TV quiz game.' -> True
		
	- 'Hello beautiful world!' -> False'''
	#Creating set of characters from inputed string (sentence)
	sentence_set = set(sentence.lower())
	#Checking if created set contains all characters from our alphabet, and returning bool
	return all(char in sentence_set for char in alphabet.lower())


def count_char(sentence: str, lowercase: bool = False) -> dict:
	'''Returns dictionary with every character counted e.g:
		"OOPp" -> {"O": 2, "P": 1, "p": 1}
	lowercase=True, will give:
		"OOPp" -> {"o": 2, "p": 2}'''
	if lowercase:
		return dict(Counter(sentence.lower()))
	else:
		return dict(Counter(sentence))

