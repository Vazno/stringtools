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

class Generate_password():
	"""Returns randomized password by input settings
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

	similar_chars = ["1", "L", "O", "0", '"', "'", "I", "B", "6", "|"]

	def __init__(self, length: int = 12,
			english: bool = True, symbols: bool = True,  numerals: bool = True,
			own_symbols = "", exclude_similarities: bool = False,
			lowercase: bool = True, uppercase: bool = True) -> str:

		self.length = length
		self.english = english
		self.symbols = symbols
		self.numerals = numerals
		self.own_symbols = own_symbols

		self.exclude_similarities = exclude_similarities
		self.lowercase = lowercase
		self.uppercase = uppercase


	def __create_main_list(self):
		self.main_list = []
		if self.english:
			self.main_list.append(list(string.ascii_uppercase))
		if self.symbols:
			self.main_list.append(list(string.punctuation))
		if self.numerals:
			self.main_list.append(list(string.digits))
		if self.own_symbols:
			self.own_symbols = list(set(self.own_symbols))
			self.main_list.append(self.own_symbols)

	def __exclude_similar(self):
		for _list in self.main_list:
			for char in _list:
				if char in self.similar_chars:
					_list.remove(char)
	
	def __upper_lower(self, char):
		if self.lowercase and self.uppercase:
			return choice([char.lower(), char.upper()])
		elif self.lowercase and not self.uppercase:
			return char.lower()
		elif self.uppercase and not self.lowercase:
			return char.upper()
		elif not self.lowercase and not self.uppercase:
			return char

	def __generate_password(self):
		password_holder = ""
		for i in range(self.length):
			random_list = choice(self.main_list)
			random_char = choice(random_list)
			password_holder += self.__upper_lower(random_char)
		return password_holder

	def __str__(self):
		if self.length != 0:
			self.__create_main_list()
			if self.exclude_similarities:
				self.__exclude_similar()
			return self.__generate_password()
		else:
			return ""