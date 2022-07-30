'''This module provides string operations, such as analaysing, converting, generating, validating.'''
# MIT License Copyright (c) 2022 Beksultan Artykbaev


from .analysers import is_pangram
from .analysers import is_heterogram
from .analysers import is_anagram
from .analysers import is_palindrome
from .analysers import is_tautogram
from .analysers import is_binary
from .analysers import count_chars
from .analysers import count_words
from .analysers import Levenshtein


from .converters import bricks
from .converters import replaceall
from .converters import numerate_text
from .converters import remove_trailing_whitespaces
from .converters import remove_leading_whitespaces
from .converters import text_to_binary
from .converters import binary_to_text


from .general import Cases


from .generators import generate_nick
from .generators import GeneratePassword


from .validators import Validator


__all__ = ["is_pangram", "is_heterogram", "is_anagram", "is_palindrome", "is_tautogram", "is_binary", "count_chars", "count_words", "Levenshtein",

	"bricks", "replaceall", "numerate_text", "remove_trailing_whitespaces", "remove_leading_whitespaces", "text_to_binary", "binary_to_text",

	"Cases",

	"generate_nick", "GeneratePassword",

	"Validator"]