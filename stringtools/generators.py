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
import random
from secrets import choice
from typing import List

def generate_nick(
	length = 5,
	vowels = ['a', 'e', 'i', 'o', 'u'],
	vowel_graphems = ['eir', 'ay', 'eau', 'au', 'ayer', 'ei', 'igh', 'aw', 'ow', 'ore', 'ou', 'er', 'ae', 'augh', 'ough', 'oo', 'uoy', 'oar', 'our', 'eer', 'et', 'eigh', 'ey', 'ye', 'ai', 'ew', 'eo', 'uy', 'u', 'air', 'oew', 'oa', 'ur', 'oe', 'ie', 'are', 'ir', 'ea', 'oy', 'aigh', 'or', 'ui', 'yr', 'ar', 'oor', 'ier', 'ue', 'ee', 'oi', 'ear', 'ho', 'ure', 'is', 'ere'],
	consonant_graphems = ['rr', 'sh', 'th', 'gu', 'zz', 'ff', 'sc', 'ft', 'dd', 'wr', 'tt', 'tu', 'qu', 'rh', 'ss', 'bb', 'lm', 'pn', 'pp', 'lf', 'se', 'mn', 'ti', 'll', 'ph', 'ps', 'te', 'kn', 'ch', 'mm', 'ck', 'gh', 'gn', 'wh', 'ed', 'mb', 'sci', 'si', 'dge', 've', 'ce', 'cc', 'ge', 'st', 'lk', 'gg', 'tch', 'ze', 'gue', 'nn', 'ci', 'di'],
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']) -> str:
	'''Generate nickname by inputed vowels, consonants, and other sounds.'''
	if length == 0:
		return ""
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

class Generate_password():
	"""Returns generated by input settings password
	Character:
		Function contains 2 character bundles:
				- english
				- symbols, numerals
			You can use all of them to create password, by turning on their bool variables.
	Extra:
	- To own_symbols, you can input string, list, set, tuple, it will use the given chars to create password from it.
	- exclude_similarities=True will delete all similar_chars: from password. (The length of password will stay the same)
	Registers:
	- use_uppercase=True will include uppercase letters in password.
	- use_lowercase=True will include lowercase letters in password.
	
	If both of them turned off, it will use it's default settings (Uppercase), and it won't change inputed chars.
	"""


	def __init__(self, length: int = 12,
			english: bool = True, symbols: bool = True,  numerals: bool = True,
			own_symbols = "", exclude_similarities: bool = False,
			lowercase: bool = True, uppercase: bool = True, similar_chars: List = ["1", "L", "O", "0", '"', "'", "I", "B", "6", "|"]) -> str:

		self.length = length
		self.english = english
		self.symbols = symbols
		self.numerals = numerals
		self.own_symbols = own_symbols
		self.similar_chars = similar_chars
		self.exclude_similarities = exclude_similarities
		self.lowercase = lowercase
		self.uppercase = uppercase

	def __str__(self):
		if self.length != 0:
			# Appending all lists with alphabets to main list
			main_list = []
			if self.english:
				main_list.append(list(string.ascii_uppercase))
			if self.symbols:
				main_list.append(list(string.punctuation))
			if self.numerals:
				main_list.append(list(string.digits))
			if self.own_symbols:
				self.own_symbols = list(set(self.own_symbols))
				main_list.append(self.own_symbols)

			# Excluding similar characters if it's set to True
			if self.exclude_similarities:
				self.__exclude_similar(main_list, self.similar_chars)


			password_holder = ""
			for i in range(self.length):
				random_char = choice(choice(main_list)) # Choosing random list, then choosing random character from list
				password_holder += self.__upper_lower(random_char, self.lowercase, self.uppercase)
			return password_holder
		else:
			return ""

	def __exclude_similar(self, main_list: List[List], chars_to_delete: List):
		# Deletes inputed character from list containing lists
		for _list in main_list:
			for char in _list:
				if char in chars_to_delete:
					_list.remove(char)
	
	def __upper_lower(self, char, lowercase, uppercase):
		'''Checking for upper and lowercase boolean values, and returning character based on input values'''
		if lowercase and uppercase:
			return choice([char.lower(), char.upper()])
		elif lowercase and not uppercase:
			return char.lower()
		elif uppercase and not lowercase:
			return char.upper()
		elif not lowercase and not uppercase:
			return char