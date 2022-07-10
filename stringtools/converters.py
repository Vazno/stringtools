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

from typing import Dict

def bricks(sentence: str) -> str:
	'''Returns bricked version of string
	- bricks("Hello world!") -> "HeLlO WoRlD!"
	- bricks("abcd") -> "AbCd"'''
	new_sentence = ''.join(x + y for x, y in zip(sentence[0::2].upper(), sentence[1::2].lower()))

	if len(sentence) % 2:
		new_sentence += sentence[-1].upper()
	return new_sentence

def replaceall(sentence: str, __old__new: Dict[str]) -> str:
	'''Replaces text from given sentence and dictionary:
		dictionary should be formatted like this {old_string: new_string}
	- replaceall("12345", {"1": "One ", "2": "Two ", "3": "Three "}) -> "OneTwoThree45"
	- replaceall("Hello world!", {"Hello": "Sup", "world": "earth"}) -> "Sup earth!"
	'''
	if __old__new == dict(): # If dictionary is empty returns sentence
		return sentence

	for old_character, new_character in __old__new.items():
		sentence = sentence.replace(old_character, new_character)
	return sentence