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

import re
from collections.abc import Mapping
from typing import Mapping, Union


class Cases:
	'''Convert string's case'''
	ACRONYM_RE = re.compile(r"([A-Z]+)$|([A-Z]+)(?=[A-Z0-9])")
	PASCAL_RE = re.compile(r"([^\-_\s]+)")
	SPLIT_RE = re.compile(r"([\-_\s]*[A-Z]+?[^A-Z\-_\s]*[\-_\s]*)")
	UNDERSCORE_RE = re.compile(r"(?<=[^\-_\s])[\-_\s]+[^\-_\s]")

	def __init__(self) -> None:
		pass


	@classmethod
	def pascalize(cls, str_or_iter: Union[str, Mapping, list]):
		"""
		Convert a string, dict, or list of dicts to pascal case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: Union[list, dict, str]
		:returns:
			pascalized string, dictionary, or list of dictionaries.
		"""
		if isinstance(str_or_iter, (list, Mapping)):
			return cls._process_keys(str_or_iter, cls.pascalize)

		s = str(cls._is_none(str_or_iter))
		if s.isupper() or s.isnumeric():
			return str_or_iter

		def _replace_fn(match):
			"""
			:rtype: str
			"""
			return match.group(1)[0].upper() + match.group(1)[1:]

		s = cls.camelize(cls.PASCAL_RE.sub(_replace_fn, s))
		return s[0].upper() + s[1:] if len(s) != 0 else s

	@classmethod
	def camelize(cls, str_or_iter: Union[str, Mapping, list]):
		"""
		Convert a string, dict, or list of dicts to camel case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: Union[list, dict, str]
		:returns:
			camelized string, dictionary, or list of dictionaries.
		"""
		if isinstance(str_or_iter, (list, Mapping)):
			return cls._process_keys(str_or_iter, cls.camelize)

		s = str(cls._is_none(str_or_iter))
		if s.isupper() or s.isnumeric():
			return str_or_iter

		if len(s) != 0 and not s[:2].isupper():
			s = s[0].lower() + s[1:]

		# For string "hello_world", match will contain
		#             the regex capture group for "_w".
		return cls.UNDERSCORE_RE.sub(lambda m: m.group(0)[-1].upper(), s)

	@classmethod
	def kebabize(cls, str_or_iter: Union[str, Mapping, list]):
		"""
		Convert a string, dict, or list of dicts to kebab case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: Union[list, dict, str]
		:returns:
			kebabized string, dictionary, or list of dictionaries.
		"""
		if isinstance(str_or_iter, (list, Mapping)):
			return cls._process_keys(str_or_iter, cls.kebabize)

		s = str(cls._is_none(str_or_iter))
		if s.isnumeric():
			return str_or_iter

		if not (s.isupper()) and (cls.is_camelcase(s) or cls.is_pascalcase(s)):
			return (
				cls._separate_words(
					string=cls._fix_abbreviations(s),
					separator="-"
				).lower()
			)

		return cls.UNDERSCORE_RE.sub(lambda m: "-" + m.group(0)[-1], s)

	@classmethod
	def decamelize(cls, str_or_iter: Union[str, Mapping, list]):
		"""
		Convert a string, dict, or list of dicts to snake case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: Union[list, dict, str]
		:returns:
			snake cased string, dictionary, or list of dictionaries.
		"""
		if isinstance(str_or_iter, (list, Mapping)):
			return cls._process_keys(str_or_iter, cls.decamelize)

		s = str(cls._is_none(str_or_iter))
		if s.isupper() or s.isnumeric():
			return str_or_iter

		return cls._separate_words(cls._fix_abbreviations(s)).lower()

	@classmethod
	def depascalize(cls, str_or_iter: Union[str, Mapping, list]):
		"""
		Convert a string, dict, or list of dicts to snake case.
		:param str_or_iter: A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: Union[list, dict, str]
		:returns:
			snake cased string, dictionary, or list of dictionaries.
		"""
		return cls.decamelize(str_or_iter)

	@classmethod
	def dekebabize(cls, str_or_iter: Union[str, Mapping, list]):
		"""
		Convert a string, dict, or list of dicts to snake case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: Union[list, dict, str]
		:returns:
			snake cased string, dictionary, or list of dictionaries.
		"""
		if isinstance(str_or_iter, (list, Mapping)):
			return cls._process_keys(str_or_iter, cls.dekebabize)

		s = str(cls._is_none(str_or_iter))
		if s.isnumeric():
			return str_or_iter

		return s.replace("-", "_")

	@classmethod
	def is_camelcase(cls, str_or_iter: Union[str, Mapping, list]) -> bool:
		"""
		Determine if a string, dict, or list of dicts is camel case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: bool
		:returns:
			True/False whether string or iterable is camel case
		"""
		return str_or_iter == cls.camelize(str_or_iter)

	@classmethod
	def is_pascalcase(cls, str_or_iter: Union[str, Mapping, list]) -> bool:
		"""
		Determine if a string, dict, or list of dicts is pascal case.
		:param str_or_iter: A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: bool
		:returns:
			True/False whether string or iterable is pascal case
		"""
		return str_or_iter == cls.pascalize(str_or_iter)

	@classmethod
	def is_kebabcase(cls, str_or_iter: Union[str, Mapping, list]) -> bool:
		"""
		Determine if a string, dict, or list of dicts is camel case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: bool
		:returns:
			True/False whether string or iterable is camel case
		"""
		return str_or_iter == cls.kebabize(str_or_iter)

	@classmethod
	def is_snakecase(cls, str_or_iter: Union[str, Mapping, list]) -> bool:
		"""
		Determine if a string, dict, or list of dicts is snake case.
		:param str_or_iter:
			A string or iterable.
		:type str_or_iter: Union[list, dict, str]
		:rtype: bool
		:returns:
			True/False whether string or iterable is snake case
		"""
		if cls.is_kebabcase(str_or_iter) and not cls.is_camelcase(str_or_iter):
			return False

		return str_or_iter == cls.decamelize(str_or_iter)

	@staticmethod
	def _is_none(_in):
		"""
		Determine if the input is None.
		:param _in: input
		:return: an empty sting if _in is None, else the input is kept unchanged
		"""
		return "" if _in is None else _in

	@classmethod
	def _process_keys(cls, str_or_iter, fn):
		if isinstance(str_or_iter, list):
			return [cls._process_keys(k, fn) for k in str_or_iter]
		if isinstance(str_or_iter, Mapping):
			return {fn(k): cls._process_keys(v, fn) for k, v in str_or_iter.items()}
		return str_or_iter

	@classmethod
	def _fix_abbreviations(cls, string):
		"""
		Rewrite incorrectly cased acronyms, initialisms, and abbreviations,
		allowing them to be decamelized correctly. For example, given the string
		"APIResponse", this function is responsible for ensuring the output is
		"api_response" instead of "a_p_i_response".
		:param string: A string that may contain an incorrectly cased abbreviation.
		:type string: str
		:rtype: str
		:returns:
			A rewritten string that is safe for decamelization.
		"""
		return cls.ACRONYM_RE.sub(lambda m: m.group(0).title(), string)

	@classmethod
	def _separate_words(cls, string, separator="_"):
		"""
		Split words that are separated by case differentiation.
		:param string: Original string.
		:param separator: String by which the individual
			words will be put back together.
		:returns:
			New string.
		"""
		return separator.join(s for s in cls.SPLIT_RE.split(string) if s)