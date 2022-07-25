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


from .generators import generate_nick
from .generators import GeneratePassword


from .validators import Validator