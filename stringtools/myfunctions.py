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

import re
import string
import random
from functools import reduce
from collections import Counter


def order(sentence: str, pl_indexing: bool = False, del_index_numerals: bool = False) -> str:
	'''Sorts inputed string by it's number in words e.g:
	
	"name4 wo2rld Hello1 my3 is5 6Alex" -> "Hello1 wo2rld my3 name4 is5 6Alex"
	
	"" -> ""'''
	#Creating list from string
	list_words = sentence.split(" ")

	#Creating list with noting ["0", "0", "0", "0"] to insert items by index assignment later
	new_list = (["0"]*len(list_words))

	#If sentence is using programming language indexing sets pl_value to 0 
	pl_value = 1
	if pl_indexing:
		pl_value = 0
	
	#Inserting items to new_list, and sorting by it's number
	#If del_index_numerals is True, deletes index numerals in words, leaving only unrelated (second) numbers: 
	# "1hell326264o" will give "hell326264o"
	if del_index_numerals:
		for word in list_words:
			digit_ = (re.findall("\d+", str(word)))
			word = word.replace(digit_[0], "")
			digit_ = int(digit_[0])
			digit_ -= pl_value
			new_list[digit_] = word
	else:
		for word in list_words:
			digit_ = (re.findall("\d+", str(word)))
			digit_ = int(digit_[0])-pl_value
			new_list[digit_] = word

	#Converting back to the string
	new_list = reduce(lambda char1, char2: char1 + char2, " ".join(new_list))
	return new_list

def is_pangram(sentence: str, alphabet: str = string.ascii_lowercase) -> bool:
	'''Checks if inputed string is pangram (If it has every letter from aplhabet) e.g:
		
	- 'Watch "Jeopardy!", Alex Trebek\'s fun TV quiz game.' -> True
		
	- 'Hello beautiful world!' -> False'''
	#Creating set of characters from inputed string (sentence)
	sentence_set = set(sentence.lower())
	#Checking if created set contains all characters from our alphabet, and returning bool
	return all(char in sentence_set for char in alphabet)

def camelCase(word: str, reverse_: bool = False) -> str:
	'''Splits camelCase into two words e.g:
		"CamelCase" -> "Camel Case"
	reverse_=True will give:
		"Camel Case" -> "CamelCase"'''
	str_ = ""
	for index_, char in enumerate(word):
		if char.isupper() and index_:
			str_ += f" {char[0]}"
		else:
			str_ += char
	if not reverse_:
		str_ = " ".join(str_.split())
	else:
		str_ = "".join(str_.split())
	return str_

def count_char(sentence: str, lowercase: bool = False) -> dict:
	'''Returns dictionary with every character counted e.g:
		"OOPp" -> {"O": 2, "P": 1, "p": 1}
	lowercase=True, will give:
		"OOPp" -> {"o": 2, "p": 2}'''
	if lowercase:
		return dict(Counter(sentence.lower()))
	else:
		return dict(Counter(sentence))

def bricks(sentence: str) -> str:
	'''Returns bricked version of string
	- "Hello world!" -> "HeLlO WoRlD!"'''
	new_sentence = ''.join(x + y for x, y in zip(sentence[0::2].upper(), sentence[1::2].lower()))
	if len(sentence) % 2 == 0:
		pass
	elif new_sentence[-1].isupper():
		new_sentence[-1] += sentence[-1].lower()
	elif new_sentence[-1].islower():
		new_sentence += sentence[-1].upper()
	else:
		new_sentence += sentence[-1]
	return new_sentence

def generate_nick(
	length = 5,
	vowels = ['a', 'e', 'i', 'o', 'u'],
	vowel_graphems = ['eir', 'ay', 'eau', 'au', 'ayer', 'ei', 'igh', 'aw', 'ow', 'ore', 'ou', 'er', 'ae', 'augh', 'ough', 'oo', 'uoy', 'oar', 'our', 'eer', 'et', 'eigh', 'ey', 'ye', 'ai', 'ew', 'eo', 'uy', 'u', 'air', 'oew', 'oa', 'ur', 'oe', 'ie', 'are', 'ir', 'ea', 'oy', 'aigh', 'or', 'ui', 'yr', 'ar', 'oor', 'ier', 'ue', 'ee', 'oi', 'ear', 'ho', 'ure', 'is', 'ere'],
	consonant_graphems = ['rr', 'sh', 'th', 'gu', 'zz', 'ff', 'sc', 'ft', 'dd', 'wr', 'tt', 'tu', 'qu', 'rh', 'ss', 'bb', 'lm', 'pn', 'pp', 'lf', 'se', 'mn', 'ti', 'll', 'ph', 'ps', 'te', 'kn', 'ch', 'mm', 'ck', 'gh', 'gn', 'wh', 'ed', 'mb', 'sci', 'si', 'dge', 've', 'ce', 'cc', 'ge', 'st', 'lk', 'gg', 'tch', 'ze', 'gue', 'nn', 'ci', 'di'],
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']) -> str:
	'''Generate nicknames by inputed vowels, consonants, and other sounds.'''

	# Picking the first letter of name
	nickname = random.choice(random.choice([vowels, consonants]))
	previous_char = nickname
	
	# Picking the rest of nickname
	for i in range(length-1):
		while len(nickname) != length:
			if len(nickname) > length:
				nickname = random.choice(random.choice([vowels, vowel_graphems, consonants, consonant_graphems]))
				previous_char = nickname

			# If the last letter is vowel adding consonant to the end
			if previous_char in vowels or previous_char in vowel_graphems:
				char = random.choice(random.choice([consonants, consonant_graphems]))
				previous_char = char

			# If the last letter is consonant adding vowel to the end
			else:
				char = random.choice(random.choice([vowels, vowel_graphems]))
				previous_char = char
			nickname += char
	return nickname.capitalize()