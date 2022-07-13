'''
MIT License

Copyright (c) 2022 Beksultan Artykbaev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import random
import pytest

@pytest.mark.parametrize("RANDOM_INT_1", [str(random.randint(1, 999999))])
@pytest.mark.parametrize("RANDOM_INT_2", [str(random.randint(1, 999999))])
@pytest.mark.parametrize("RANDOM_INT_3", [str(random.randint(1, 999999))])
def test_validate_semver(RANDOM_INT_1, RANDOM_INT_2, RANDOM_INT_3):
	from stringtools import validate_semver
	random_version = f"{RANDOM_INT_1}.{RANDOM_INT_2}.{RANDOM_INT_3}"

	valid_semver = f'''
	{RANDOM_INT_1}.{RANDOM_INT_2}.{RANDOM_INT_3}
	{random_version}-prerelease+meta
	{random_version}+meta
	{random_version}+meta-valid
	{random_version}-alpha
	{random_version}-beta
	{random_version}-alpha.beta
	{random_version}-alpha.beta.1
	{random_version}-alpha.1
	{random_version}-alpha0.valid
	{random_version}-alpha.0valid
	{random_version}-alpha-a.b-c-somethinglong+build.1-aef.1-its-okay
	{random_version}-rc.1+build.1
	{random_version}-rc.1+build.123
	{random_version}-beta
	{random_version}-DEV-SNAPSHOT
	{random_version}-SNAPSHOT-123
	{random_version}
	{random_version}
	{random_version}
	{random_version}+build.1848
	{random_version}-alpha.1227
	{random_version}-alpha+beta
	{random_version}----RC-SNAPSHOT.12.9.1--.12+788
	{random_version}----R-S.12.9.1--.12+meta
	{random_version}----RC-SNAPSHOT.12.9.1--.12
	{random_version}+0.build.1-rc.10000aaa-kk-0.1
	{RANDOM_INT_3}.{RANDOM_INT_2}.{RANDOM_INT_1}
	{random_version}-{RANDOM_INT_3}A.is.legal'''


	invalid_semver = f'''
	1
	{RANDOM_INT_3}.{RANDOM_INT_1}
	{random_version}-0{RANDOM_INT_1}
	{random_version}-0{RANDOM_INT_2}.0{RANDOM_INT_3}
	{random_version}+.{RANDOM_INT_1}
	+invalid
	-invalid
	-invalid+invalid
	-invalid.01
	alpha
	alpha.beta
	alpha.beta.1
	alpha.1
	alpha+beta
	alpha_beta
	alpha.
	alpha..
	beta
	1.0.0-alpha_beta
	-alpha.
	{random_version}-alpha..
	{random_version}-alpha..1
	{random_version}-alpha...1
	{random_version}-alpha....1
	{random_version}-alpha.....1
	{random_version}-alpha......1
	{random_version}-alpha.......1
	0{random_version}
	{RANDOM_INT_3}.0{RANDOM_INT_2}.{RANDOM_INT_1}
	{RANDOM_INT_3}.{RANDOM_INT_2}.01
	{RANDOM_INT_2}.{RANDOM_INT_1}
	{random_version}.DEV
	{RANDOM_INT_3}.{RANDOM_INT_2}-SNAPSHOT
	{RANDOM_INT_1}.{RANDOM_INT_2}.{RANDOM_INT_3}.{RANDOM_INT_2}.{RANDOM_INT_1}----RC-SNAPSHOT.{RANDOM_INT_1}.1--..12+788
	{RANDOM_INT_1}.{RANDOM_INT_2}-RC-SNAPSHOT
	-{RANDOM_INT_1}.{RANDOM_INT_3}.{RANDOM_INT_2}-gamma+b7718
	+justmeta
	{random_version}+meta+meta
	{random_version}-whatever+meta+meta
	{random_version}----RC-SNAPSHOT.12.09.1--------------------------------..12'''
	
	for version_name in valid_semver.split():
		assert validate_semver(version_name) == True
	for version_name in invalid_semver.split():
		assert validate_semver(version_name) == False