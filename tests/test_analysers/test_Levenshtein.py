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
import pytest
@pytest.mark.parametrize("test_data",
	[[("classic", "kitten", "sitting", 3),
    ("same", "kitten", "kitten", 0),
    ("empty", "", "", 0),
    ("a", "meilenstein", "levenshtein", 4),
    ("b", "levenshtein", "frankenstein", 6),
    ("c", "confide", "deceit", 6),
    ("d", "CUNsperrICY", "conspiracy", 8)]])
def test_Levenshtein(test_data):
	from stringtools import Levenshtein

	assert Levenshtein.classic_levenshtein("foo", "boo") == 1
	assert Levenshtein.classic_levenshtein("ba", "abc") == 2
	assert Levenshtein.classic_levenshtein("foobar", "foobra") == 2
	assert Levenshtein.classic_levenshtein("fee", "deed") == 2

	for _tuple in test_data:

		# Classic version is too slow.
		# assert Levenshtein.classic_levenshtein(_tuple[1], _tuple[2]) == _tuple[3]

		assert Levenshtein.damerau_levenshtein(_tuple[1], _tuple[2]) == _tuple[3]

		assert Levenshtein.recursive_levenshtein(_tuple[1], _tuple[2]) == _tuple[3]

		assert Levenshtein.wf_levenshtein(_tuple[1], _tuple[2]) == _tuple[3]

		assert Levenshtein.wfi_levenshtein(_tuple[1], _tuple[2]) == _tuple[3]

