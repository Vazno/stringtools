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
import socket

class Validator():
	'''This class conatains most of the best re validators, and other validator functions.'''
	def __init__(self) -> None:
		pass

	@staticmethod
	def is_re_pattern_in_text(re_pattern: str, text: str) -> bool:
		'''Checks if regex pattern is in text, returns bool'''
		return bool(re.match(re_pattern, text))

	@staticmethod
	def delete_re_pattern(re_pattern:str, text:str) -> str:
		'''Deletes all found regex pattern from string.'''
		return re.sub(re_pattern, "", text)

	@classmethod
	def validate_semver(cls, version: str) -> bool:
		'''Validate if version name follows semantic versioning.
		- Validator.validate_semver("1.0.0") -> True
		- Validator.validate_semver("1.0.0.0") -> False
		
		For more information go to: https://semver.org/'''
		# https://regex101.com/r/Ly7O1x/3
		return cls.is_re_pattern_in_text(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$", version)

	@classmethod
	def validate_email(cls, email: str) -> bool:
		'''Validate an email address. 
		- Validator.validate_email("email@example.com") -> True
		- Validator.validate_email("email@example..com") -> False'''
		# http://emailregex.com/
		return cls.is_re_pattern_in_text(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)

	@classmethod
	def validate_url(cls, url: str) -> bool:
		'''Validate url address.
		- Validator.validate_url("https://example.com/") -> True
		- Validator.validate_url("example.com") -> False'''
		# https://urlregex.com/
		return cls.is_re_pattern_in_text(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url)

	@staticmethod
	def validate_ipv4(ip: str) -> bool:
		'''Validate an ipv4 address.
		- Validator.validate_ipv4("127.255.255.254") -> True
		- Validator.validate_ipv4("127.255.254") -> False'''
		try:
			socket.inet_pton(socket.AF_INET, ip)
			return True
		except socket.error:
			return False

	@staticmethod
	def validate_ipv6(ip: str) -> bool:
		'''Validate an ipv6 address
		- Validator.validate_ipv6("2345:0425:2CA1:0000:0000:0567:5673:23b5") -> True
		- Validator.validate_ipv6("0425:2CA1:0000:0000:0567:5673:23b5") -> False'''
		try:
			socket.inet_pton(socket.AF_INET6, ip)
			return True
		except socket.error:
			return False