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
import random
import string
import pytest
@pytest.mark.parametrize("PASSWORD_TEST_SIZE", [random.randint(50, 100)])
def test_Generate_password(PASSWORD_TEST_SIZE):
	from stringtools import Generate_password
	assert str(Generate_password(length=0)) == ""

	# Checking if exclude_similarities work
	assert str(Generate_password(length=PASSWORD_TEST_SIZE, english=True, symbols=True, exclude_similarities=True)) not in Generate_password.similar_chars
	
	# Checking uppercase
	assert str(Generate_password(length=PASSWORD_TEST_SIZE, uppercase=True, lowercase=False)).isupper()

	# Checking lowercase
	assert str(Generate_password(length=PASSWORD_TEST_SIZE, lowercase=True, uppercase=False)).islower()


# Testing own_symbols setting
@pytest.mark.parametrize("PASSWORD_TEST_SIZE", [random.randint(50, 100)])
def test_Generate_password_own_symbols(PASSWORD_TEST_SIZE):
	from stringtools import Generate_password
	# Storing own symbols
	random_own = []

	# Appending random letters to list
	for i in range(2):
		random_own.append(random.choice(string.ascii_lowercase))

	assert "".join(random_own) in str(Generate_password(length=PASSWORD_TEST_SIZE, english=False, symbols=False, numerals=False, own_symbols=random_own))
	assert set(str(Generate_password(length=PASSWORD_TEST_SIZE, english=False, symbols=False, numerals=False, own_symbols=random_own)).lower()) == set(random_own)