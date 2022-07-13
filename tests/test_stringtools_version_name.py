import re
def test_stringtools_version_name():
	'''Checks if package version name follows semantic versioning'''
	from stringtools import validate_semver
	with open("setup.cfg", "r") as _file:
		data = _file.read()
	assert validate_semver(re.findall(r"\nversion(?:[\s]+|[\s])?[=](?:[\s]+|[\s])?(.*)", data)[0]) == True