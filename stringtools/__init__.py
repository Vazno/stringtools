'''This module provides string operations, such as analaysing, converting, generating, validating.'''
# MIT License Copyright (c) 2022 Beksultan Artykbaev

from .analysers import is_pangram, is_heterogram, is_anagram, is_palindrome, is_tautogram, count_chars, count_words
from .converters import bricks, replaceall, numerate_text, remove_trailing_whitespaces, remove_leading_whitespaces
from .generators import generate_nick, GeneratePassword
from .validators import Validator