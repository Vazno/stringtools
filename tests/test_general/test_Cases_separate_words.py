"""
Test the utility for splitting words.
"""
import pytest
from stringtools.general import Cases


@pytest.mark.parametrize(
	"input_str, expected_output",
	[
		# Pascals.
		("HelloWorld", "Hello_World"),
		("_HelloWorld", "_Hello_World"),
		("__HelloWorld", "__Hello_World"),
		("HelloWorld_", "Hello_World_"),
		("HelloWorld__", "Hello_World__"),
		# Camels
		("helloWorld", "hello_World"),
		("_helloWorld", "_hello_World"),
		("__helloWorld", "__hello_World"),
		("helloWorld_", "hello_World_"),
		("helloWorld__", "hello_World__"),
		# Snakes
		("hello_world", "hello_world"),
		("_hello_world", "_hello_world"),
		("__hello_world", "__hello_world"),
		("hello_world_", "hello_world_"),
		("hello_world__", "hello_world__"),
		("whatever_hi", "whatever_hi"),
		("whatever_10", "whatever_10"),
		("sizeX", "size_X"),
		("aB", "a_B"),
		("testNTest", "test_N_Test"),
	],
)

def test_separate_words(input_str, expected_output):
	"""
	:param input_str: String that will be transformed.
	:param expected_output: The expected transformation.
	"""
	output = Cases._separate_words(input_str)
	assert output == expected_output, "{} != {}".format(
		output, expected_output
	)
