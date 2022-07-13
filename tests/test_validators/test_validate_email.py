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
@pytest.mark.parametrize("RANDOM_STR", ["".join([random.choice(string.ascii_letters) for i in range(random.randint(1, 100))])])
@pytest.mark.parametrize("RANDOM_PUNCTUATION", [random.choice(string.punctuation)])
def test_validate_email(RANDOM_STR: str, RANDOM_PUNCTUATION):
	from stringtools import validate_email
	assert validate_email(f"{RANDOM_STR}@{RANDOM_STR}.{RANDOM_STR}") == True
	assert validate_email(f"{RANDOM_STR}@@{RANDOM_STR}.{RANDOM_STR}") == False
	assert validate_email(RANDOM_STR) == False
	assert validate_email(f"{RANDOM_PUNCTUATION}") == False