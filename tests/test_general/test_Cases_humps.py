import pytest

from stringtools.general import Cases


def test_converting_strings():
	assert Cases.camelize("jack_in_the_box") == "jackInTheBox"
	assert Cases.decamelize("rubyTuesdays") == "ruby_tuesdays"
	assert Cases.depascalize("UnosPizza") == "unos_pizza"
	assert Cases.pascalize("red_robin") == "RedRobin"
	assert Cases.kebabize("white_castle") == "white-castle"
	assert Cases.dekebabize("taco-bell") == "taco_bell"


@pytest.mark.parametrize(
	"input_str, expected_output",
	[
		("PERatio", "pe_ratio"),
		("HTTPResponse", "http_response"),
		("_HTTPResponse", "_http_response"),
		("_HTTPResponse__", "_http_response__"),
		("BIP73", "BIP73"),
		("BIP72b", "bip72b"),
		("memMB", "mem_mb"),
	],
)
def test_camelized_acronyms(input_str, expected_output):
	"""
	Validate decamelizing acronyms works as expected.
	:type input_str: str
	:type expected_output: str
	"""
	assert Cases.decamelize(input_str) == expected_output


def test_conditionals():
	assert Cases.is_pascalcase("RedRobin")
	assert Cases.is_snakecase("RedRobin") is False
	assert Cases.is_camelcase("RedRobin") is False
	assert Cases.is_kebabcase("RedRobin") is False

	assert Cases.is_snakecase("ruby_tuesdays")
	assert Cases.is_camelcase("ruby_tuesdays") is False
	assert Cases.is_pascalcase("ruby_tuesdays") is False
	assert Cases.is_kebabcase("ruby_tuesdays") is False

	assert Cases.is_camelcase("jackInTheBox")
	assert Cases.is_snakecase("jackInTheBox") is False
	assert Cases.is_pascalcase("jackInTheBox") is False
	assert Cases.is_kebabcase("jackInTheBox") is False

	assert Cases.is_kebabcase("white-castle")
	assert Cases.is_snakecase("white-castle") is False
	assert Cases.is_camelcase("white-castle") is False
	assert Cases.is_pascalcase("white-castle") is False

	assert Cases.is_camelcase("API")
	assert Cases.is_pascalcase("API")
	assert Cases.is_snakecase("API")
	assert Cases.is_kebabcase("API")


	assert Cases.is_snakecase("whatever_10")
	assert Cases.is_camelcase("whatever_10") is False
	assert Cases.is_pascalcase("whatever_10") is False
	assert Cases.is_kebabcase("whatever_10") is False


def test_numeric():
	assert Cases.camelize(1234) == 1234
	assert Cases.decamelize(123) == 123
	assert Cases.pascalize(123) == 123
	assert Cases.kebabize(123) == 123


def test_upper():
	assert Cases.camelize("API") == "API"
	assert Cases.decamelize("API") == "API"
	assert Cases.pascalize("API") == "API"
	assert Cases.depascalize("API") == "API"
	assert Cases.kebabize("API") == "API"
	assert Cases.dekebabize("API") == "API"


def test_pascalize():
	actual = Cases.pascalize(
		{
			"videos": [
				{
					"fallback_url": "https://media.io/video",
					"scrubber_media_url": "https://media.io/video",
					"dash_url": "https://media.io/video",
				}
			],
			"images": [
				{
					"fallback_url": "https://media.io/image",
					"scrubber_media_url": "https://media.io/image",
					"url": "https://media.io/image",
				}
			],
			"other": [
				{
					"_fallback_url": "https://media.io/image",
					"__scrubber_media___url_": "https://media.io/image",
					"_url__": "https://media.io/image",
				},
				{
					"API": "test_upper",
					"_API_": "test_upper",
					"__API__": "test_upper",
					"APIResponse": "test_acronym",
					"_APIResponse_": "test_acronym",
					"__APIResponse__": "test_acronym",
				},
			],
		}
	)
	expected = {
		"Videos": [
			{
				"FallbackUrl": "https://media.io/video",
				"ScrubberMediaUrl": "https://media.io/video",
				"DashUrl": "https://media.io/video",
			}
		],
		"Images": [
			{
				"FallbackUrl": "https://media.io/image",
				"ScrubberMediaUrl": "https://media.io/image",
				"Url": "https://media.io/image",
			}
		],
		"Other": [
			{
				"_FallbackUrl": "https://media.io/image",
				"__ScrubberMediaUrl_": "https://media.io/image",
				"_Url__": "https://media.io/image",
			},
			{
				"API": "test_upper",
				"_API_": "test_upper",
				"__API__": "test_upper",
				"APIResponse": "test_acronym",
				"_APIResponse_": "test_acronym",
				"__APIResponse__": "test_acronym",
			},
		],
	}
	assert actual == expected


def test_depascalize():
	actual = Cases.depascalize(
		[
			{
				"Symbol": "AAL",
				"LastPrice": 31.78,
				"ChangePct": 2.8146,
				"ImpliedVolatality": 0.482,
			},
			{
				"Symbol": "LBTYA",
				"LastPrice": 25.95,
				"ChangePct": 2.6503,
				"ImpliedVolatality": 0.7287,
			},
			{
				"_Symbol": "LBTYK",
				"ChangePct_": 2.5827,
				"_LastPrice__": 25.42,
				"__ImpliedVolatality_": 0.4454,
			},
			{
				"API": "test_upper",
				"_API_": "test_upper",
				"__API__": "test_upper",
				"APIResponse": "test_acronym",
				"_APIResponse_": "test_acronym",
				"__APIResponse__": "test_acronym",
				"ruby_tuesdays": "ruby_tuesdays",
			},
		]
	)
	expected = [
		{
			"symbol": "AAL",
			"last_price": 31.78,
			"change_pct": 2.8146,
			"implied_volatality": 0.482,
		},
		{
			"symbol": "LBTYA",
			"last_price": 25.95,
			"change_pct": 2.6503,
			"implied_volatality": 0.7287,
		},
		{
			"_symbol": "LBTYK",
			"change_pct_": 2.5827,
			"_last_price__": 25.42,
			"__implied_volatality_": 0.4454,
		},
		{
			"API": "test_upper",
			"_API_": "test_upper",
			"__API__": "test_upper",
			"api_response": "test_acronym",
			"_api_response_": "test_acronym",
			"__api_response__": "test_acronym",
			"ruby_tuesdays": "ruby_tuesdays",
		},
	]

	assert actual == expected
