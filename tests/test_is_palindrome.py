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
import pytest
import random
import string
@pytest.mark.parametrize("obj",
	# Generating random List[str, int]
	[[random.choice([random.choice(string.printable), random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])]) for i in range(random.randint(50, 100))]])
def test_is_palindrome(obj):
	from stringtools import is_palindrome

	# Checking str
	str_obj = [str(x) if type(x) == int else x for x in obj] # Converting List[str, int] to string
	palindrome_str = str_obj + str_obj[::-1]
	assert is_palindrome(palindrome_str) == True
	assert is_palindrome(str_obj) == False

	# Checking list
	reversed_list = obj[::-1]
	palindrome_list = obj + reversed_list
	assert is_palindrome(palindrome_list) == True
	assert is_palindrome(obj) == False

	# Checking tuple
	reversed_tuple = tuple(obj)[::-1]
	palindrome_tuple = tuple(obj) + reversed_tuple
	assert is_palindrome(reversed_tuple) == False # Checking Tuple[str, int]
	assert is_palindrome(palindrome_tuple) == True
	# Checking int
	random_str_int = "".join([str(element) for element in obj if type(element) == int]) # Generating string containing only digits
	
	int_value = int(random_str_int) # Converting string with digits to int
	assert is_palindrome(int_value) == False
	palindrome_str = random_str_int + random_str_int [::-1] # Creating palindrome int
	assert is_palindrome(palindrome_str) == True