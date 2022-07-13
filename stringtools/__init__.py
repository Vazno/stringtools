'''String analaysing, converting, generating tools.'''
# MIT License Copyright (c) 2022 Beksultan Artykbaev

from .analysers import is_pangram, is_heterogram, is_anagram, is_palindrome, is_tautogram, count_chars, count_words
from .converters import bricks, replaceall, numerate_text, remove_trailing_whitespaces, remove_leading_whitespaces
from .generators import generate_nick, Generate_password
from .validators import validate_semver, validate_email, validate_ipv4, validate_ipv6, validate_url