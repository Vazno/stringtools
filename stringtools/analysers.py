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
from typing import Union, List


def is_pangram(sentence: str, alphabet: str = string.ascii_lowercase) -> bool:
	'''Checks if inputed string is pangram.
	(If it has every letter from aplhabet) e.g:
		
	- 'Watch "Jeopardy!", Alex Trebek\'s fun TV quiz game.' -> True
		
	- 'Hello beautiful world!' -> False'''
	#Checking if created set contains all characters from our alphabet, and returning bool
	return all(char in set(sentence.lower()) for char in alphabet.lower())

def is_heterogram(sentence: str) -> bool:
	'''Checks if inputed string is heterogram.
	(A heterogram is a string in which no letter of the alphabet occurs more than once)
	- is_heterpgram("abcd") -> True
	- is_heterogram("abcdd") -> False'''
	return all(False for key, value in dict(Counter(sentence.lower())).items() if key.isalpha() and value != 1)

def is_anagram(first_word: str, second_word: str) -> bool:
	'''Checks if given word is anagram of other one.
	(Anagram it's a string that contain all letters from other string)
	- is_anagram("Listen", "Silent") -> True
	- is_anagram("123", ("1234")) -> False'''
	return dict(Counter(first_word.replace(" ", "").lower())) == dict(Counter(second_word.replace(" ", "").lower()))

def is_palindrome(obj: Union[List[Union[str, int]], str, int, tuple[Union[str, int]]]) -> bool:
	'''Checks if inputed object is palindrome.
		Takes Built-in Data Types (list, tuple, str, int)
	(A palindrome is a word, number, phrase, or other sequence of characters which reads
	the same backward as forward, such as madam or racecar.)'''
	
	if type(obj) == dict:
		raise ValueError("Dictionaries don't support duplicate keys. So it can't be palindrome.")
	if type(obj) == set:
		raise ValueError("A set does not hold duplicate items. So it can't be palindrome.")
	# If object is str or List[str] or List[int] or List[str, int] or Tuple[...]
	try:
		obj = [x if type(x) == int else x.lower() for x in obj]
		return obj == obj[::-1]
	# If object is int
	except TypeError:
		return str(obj) == str(obj)[::-1]

def count_char(sentence: str, lowercase: bool = False) -> dict:
	'''Returns dictionary with every character counted e.g:
		"OOPp" -> {"O": 2, "P": 1, "p": 1}
	lowercase=True, will give:
		"OOPp" -> {"o": 2, "p": 2}'''
	if sentence != "":
		if lowercase:
			return dict(Counter(sentence.lower()))
		else:
			return dict(Counter(sentence))
	else:
		return dict()