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

from functools import reduce
import re

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

def camelCase(word: str, reverse_: bool = False) -> str:
	'''Splits camelCase into two words e.g:
		"CamelCase" -> "Camel Case"
	reverse_=True will give:
		"Camel Case" -> "CamelCase"'''
	if word == "":
		return word
	else:
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
