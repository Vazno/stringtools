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

import string
from collections import Counter
from typing import Dict, Union, Tuple, List


def is_pangram(sentence: str, alphabet: str = string.ascii_lowercase) -> bool:
	'''Checks if inputed string is pangram (A pangram is a sentence using every letter of a given alphabet at least once.)
	- is_pangram('Watch "Jeopardy!", Alex Trebek\'s fun TV quiz game.') -> True
	- is_pangram('Hello beautiful world!') -> False'''
	#Checking if created set contains all characters from our alphabet, and returning bool
	return all(char in set(sentence.lower()) for char in alphabet.lower())

def is_heterogram(sentence: str) -> bool:
	'''Checks if inputed string is heterogram (A heterogram is a string in which no letter of the alphabet occurs more than once.)
	- is_heterpgram("abcd") -> True
	- is_heterogram("abcdd") -> False'''
	return all(False for key, value in dict(Counter(sentence.lower())).items() if key.isalpha() and value != 1)

def is_anagram(first_word: str, second_word: str) -> bool:
	'''Checks if inputed string is an anagram (Anagram is a string that contain all letters from other string.)
	- is_anagram("Listen", "Silent") -> True
	- is_anagram("123", ("1234")) -> False'''
	return dict(Counter(first_word.replace(" ", "").lower())) == dict(Counter(second_word.replace(" ", "").lower()))

def is_palindrome(obj: Union[List[Union[str, int]], str, int, Tuple[Union[str, int]]]) -> bool:
	'''Checks if inputed string is a palindrome (A palindrome is a word, number, phrase,
	or other sequence of characters which reads the same backward as forward, such as madam or racecar.)
		Takes Built-in Data Types (list, tuple, str, int)
	(A palindrome is a word, number, phrase, or other sequence of characters which reads
	the same backward as forward, such as madam or racecar.)
	- is_palindrome("radar") -> True
	- is_palindrome("word") -> False'''
	
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

def is_tautogram(sentence: str) -> bool:
	'''Checks if inputed string is a tautogram (A tautogram is a text in which all words start with the same letter.)
	- is_tautogram("Crazy cat, cute, cuddly") -> True
	- is_tautogram("Crazy mouse, cute, cuddly") -> False'''
	list_sentence = sentence.lower().split(" ")
	def __first_char(_list: List[str]):
		for word in _list:
			for char in word:
				if char.isalpha():
					return char
	first_character = __first_char(list_sentence)
	for word in list_sentence:
		for char in word:
			if char.isalpha():
				if char != first_character:
					return False
				break
	return True

def is_binary(obj: Union[str, int]) -> bool:
	'''Checks if given string or int is binary number
	(A binary number is a number expressed in the base-2 numeral system or binary numeral system,
	a method of mathematical expression which uses only two symbols: 0 and 1)
	- is_binary(100101010101) -> True
	- is_binary("1010010101012") -> False'''
	allowed_chars = ["0", "1", "b", " "]
	return all(True if num in allowed_chars else False for num in str(obj))

def count_chars(sentence: str, lowercase: bool = False) -> Dict:
	'''Returns dictionary with every character counted.
	- count_chars("OOPp") -> {"O": 2, "P": 1, "p": 1}
	- count_chars("OOPp", lowercase=True) -> {"o": 2, "p": 2}'''
	if sentence != "":
		if lowercase:
			return dict(Counter(sentence.lower()))
		else:
			return dict(Counter(sentence))
	else:
		return dict()

def count_words(sentence: str) -> int:
	'''Returns an integer with every word counted.
	- count_words("Hello world!") -> 2
	- count_words("This is me") -> 3'''
	if sentence:
		return len(sentence.split())
	else: return 0 # If sentence is empty returns 0

class Levenshtein():
	'''This class contains functions for Levenshtein distance calculations'''
	# 	Copyright (c) 2012, Daniel Lindsley
	# All rights reserved.

	# Redistribution and use in source and binary forms, with or without
	# modification, are permitted provided that the following conditions are met:

	# 	* Redistributions of source code must retain the above copyright
	# 	notice, this list of conditions and the following disclaimer.
	# 	* Redistributions in binary form must reproduce the above copyright
	# 	notice, this list of conditions and the following disclaimer in the
	# 	documentation and/or other materials provided with the distribution.
	# 	* Neither the name of the pylev nor the
	# 	names of its contributors may be used to endorse or promote products
	# 	derived from this software without specific prior written permission.

	# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
	# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
	# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	# DISCLAIMED. IN NO EVENT SHALL pylev BE LIABLE FOR ANY
	# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
	# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
	# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
	# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
	# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
	# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

	@staticmethod
	def classic_levenshtein(string_1: str, string_2: str) -> int:
		"""
		Calculates the Levenshtein distance between two strings.
		This version is easier to read, but significantly slower than the version
		below (up to several orders of magnitude). Useful for learning, less so
		otherwise.
		- Levenshtein.classic_levenshtein('kitten', 'sitting') -> 3
		- Levenshtein.classic_levenshtein('kitten', 'kitten') -> 0
		- Levenshtein.classic_levenshtein('', '') -> 0
		"""
		len_1 = len(string_1)
		len_2 = len(string_2)
		cost = 0

		if len_1 and len_2 and string_1[0] != string_2[0]:
			cost = 1

		if len_1 == 0:
			return len_2
		elif len_2 == 0:
			return len_1
		else:
			return min(
				Levenshtein.classic_levenshtein(string_1[1:], string_2) + 1,
				Levenshtein.classic_levenshtein(string_1, string_2[1:]) + 1,
				Levenshtein.classic_levenshtein(string_1[1:], string_2[1:]) + cost,
			)

	@staticmethod
	def damerau_levenshtein(string_1: str, string_2: str) -> int:
		"""
		Calculates the Damerau-Levenshtein distance between two strings.
		In addition to insertions, deletions and substitutions,
		Damerau-Levenshtein considers adjacent transpositions.
		This version is based on an iterative version of the Wagner-Fischer algorithm.
		- Levenshtein.damerau_levenshtein('kitten', 'sitting') -> 3
		- Levenshtein.damerau_levenshtein('kitten', 'kittne') -> 1
		- Levenshtein.damerau_levenshtein('', '') -> 0
		"""
		if string_1 == string_2:
			return 0

		len_1 = len(string_1)
		len_2 = len(string_2)

		if len_1 == 0:
			return len_2
		if len_2 == 0:
			return len_1

		if len_1 > len_2:
			string_2, string_1 = string_1, string_2
			len_2, len_1 = len_1, len_2

		prev_cost = 0
		d0 = [i for i in range(len_2 + 1)]
		d1 = [j for j in range(len_2 + 1)]
		dprev = d0[:]

		s1 = string_1
		s2 = string_2

		for i in range(len_1):
			d1[0] = i + 1
			for j in range(len_2):
				cost = d0[j]

				if s1[i] != s2[j]:
					# substitution
					cost += 1

					# insertion
					x_cost = d1[j] + 1
					if x_cost < cost:
						cost = x_cost

					# deletion
					y_cost = d0[j + 1] + 1
					if y_cost < cost:
						cost = y_cost

					# transposition
					if i > 0 and j > 0 and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
						transp_cost = dprev[j - 1] + 1
						if transp_cost < cost:
							cost = transp_cost
				d1[j + 1] = cost

			dprev, d0, d1 = d0, d1, dprev

		return d0[-1]

	@staticmethod
	def recursive_levenshtein(
		string_1: str, string_2: str, len_1: int = None, len_2: int = None, offset_1: int = 0, offset_2: int = 0, memo: Dict = None) -> int:
		"""
		Calculates the Levenshtein distance between two strings.
		- Levenshtein.recursive_levenshtein('kitten', 'sitting') -> 3
		- Levenshtein.recursive_levenshtein('kitten', 'kitten') -> 0
		- Levenshtein.recursive_levenshtein('', '') -> 0
		"""
		if len_1 is None:
			len_1 = len(string_1)

		if len_2 is None:
			len_2 = len(string_2)

		if memo is None:
			memo = {}

		key = ",".join([str(offset_1), str(len_1), str(offset_2), str(len_2)])

		if memo.get(key) is not None:
			return memo[key]

		if len_1 == 0:
			return len_2
		elif len_2 == 0:
			return len_1

		cost = 0

		if string_1[offset_1] != string_2[offset_2]:
			cost = 1

		dist = min(
			Levenshtein.recursive_levenshtein(
				string_1, string_2, len_1 - 1, len_2, offset_1 + 1, offset_2, memo
			)
			+ 1,
			Levenshtein.recursive_levenshtein(
				string_1, string_2, len_1, len_2 - 1, offset_1, offset_2 + 1, memo
			)
			+ 1,
			Levenshtein.recursive_levenshtein(
				string_1, string_2, len_1 - 1, len_2 - 1, offset_1 + 1, offset_2 + 1, memo
			)
			+ cost,
		)
		memo[key] = dist
		return dist

	@staticmethod
	def wf_levenshtein(string_1: str, string_2: str) -> int:
		"""
		Calculates the Levenshtein distance between two strings.
		This version uses the Wagner-Fischer algorithm.
		- Levenshtein.wf_levenshtein('kitten', 'sitting') -> 3
		- Levenshtein.wf_levenshtein('kitten', 'kitten') -> 0
		- Levenshtein.wf_levenshtein('', '') -> 0
		"""
		len_1 = len(string_1) + 1
		len_2 = len(string_2) + 1

		d = [0] * (len_1 * len_2)

		for i in range(len_1):
			d[i] = i
		for j in range(len_2):
			d[j * len_1] = j

		for j in range(1, len_2):
			for i in range(1, len_1):
				if string_1[i - 1] == string_2[j - 1]:
					d[i + j * len_1] = d[i - 1 + (j - 1) * len_1]
				else:
					d[i + j * len_1] = min(
						d[i - 1 + j * len_1] + 1,  # deletion
						d[i + (j - 1) * len_1] + 1,  # insertion
						d[i - 1 + (j - 1) * len_1] + 1,  # substitution
					)

		return d[-1]

	@staticmethod
	def wfi_levenshtein(string_1: str, string_2: str) -> int:
		"""
		Calculates the Levenshtein distance between two strings.
		This version uses an iterative version of the Wagner-Fischer algorithm.
		- Levenshtein.wfi_levenshtein('kitten', 'sitting') -> 3
		- Levenshtein.wfi_levenshtein('kitten', 'kitten') -> 0
		- Levenshtein.wfi_levenshtein('', '') -> 0
		"""
		if string_1 == string_2:
			return 0

		len_1 = len(string_1)
		len_2 = len(string_2)

		if len_1 == 0:
			return len_2
		if len_2 == 0:
			return len_1

		if len_1 > len_2:
			string_2, string_1 = string_1, string_2
			len_2, len_1 = len_1, len_2

		d0 = [i for i in range(len_2 + 1)]
		d1 = [j for j in range(len_2 + 1)]

		for i in range(len_1):
			d1[0] = i + 1
			for j in range(len_2):
				cost = d0[j]

				if string_1[i] != string_2[j]:
					# substitution
					cost += 1

					# insertion
					x_cost = d1[j] + 1
					if x_cost < cost:
						cost = x_cost

					# deletion
					y_cost = d0[j + 1] + 1
					if y_cost < cost:
						cost = y_cost

				d1[j + 1] = cost

			d0, d1 = d1, d0

		return d0[-1]