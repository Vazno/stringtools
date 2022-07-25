
![Logo](https://raw.githubusercontent.com/Vazno/stringtools/main/readme-images/stringtools.svg)
<p align="center">
    <em>stringtools provides string operations, such as analaysing, converting, generating, validating.</em>
</p>

<p align="center">
<a href="https://github.com/Vazno/stringtools/actions/workflows/pytester.yml" target="_blank">
    <img src="https://github.com/Vazno/stringtools/actions/workflows/pytester.yml/badge.svg?" alt="Tests">
</a>

<a href="https://lgtm.com/projects/g/Vazno/stringtools/context:python" target="_blank">
    <img src="https://img.shields.io/lgtm/grade/python/g/Vazno/stringtools.svg?logo=lgtm&logoWidth=18" alt="Tests">
</a>

<a href="https://pypi.org/project/stringtools" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/stringtools.svg?color=%2334D058" alt="Supported Python versions">
</a>

---

**Source Code**: <a href="https://github.com/Vazno/stringtools" target="_blank">https://github.com/Vazno/stringtools</a>

**PyPI**: <a href="https://pypi.org/project/stringtools/" target="_blank">https://pypi.org/project/stringtools/</a>

---
stringtools has a lot of solutions specially built to be fast and stable ⚡.

The key features are:

* **Easy to use**: It's has a very friendly and well-commented code.
* **Open source**: stringtools is completely free and [open source](https://opensource.org/about)
* **Stability**: Most of the code is covered with tests, so there is a less chance to catch a bug.


# Installation:
``pip install stringtools``

# User’s Guide:

## There are 4 categories:
### analaysers - Analyse string.
<p id="analysers"></p><table><tr><td><a href="#ispangram">ispangram</a>
</td><td><a href="#is_heterogram">is_heterogram</a>
</td><td><a href="#is_anagram">is_anagram</a>
</td><td><a href="#is_palindrome">is_palindrome</a>
</td></tr><tr><td><a href="#is_tautogram">is_tautogram</a>
</td><td><a href="#is_binary">is_binary</a>
</td><td><a href="#count_chars">count_chars</a>
</td><td><a href="#count_words">count_words</a>
</td></tr><tr><td><a href="#Levenshteinclassic_levenshtein">classic_levenshtein</a>
</td><td><a href="#Levenshteindamerau_levenshtein">damerau_levenshtein</a>
</td><td><a href="#Levenshteinrecursive_levenshtein">recursive_levenshtein</a>
</td><td><a href="#Levenshteinwf_levenshtein">wf_levenshtein</a>
</td></tr><tr><td><a href="#Levenshteinwfi_levenshtein">wfi_levenshtein</a>
</td></tr></table>

### converters - Convert one string value to other string value.
<p id="converters"></p><table><tr><td><a href="#bricks">bricks</a>
</td><td><a href="#replaceall">replaceall</a>
</td><td><a href="#numerate_text">numerate_text</a>
</td><td><a href="#remove_trailing_whitespaces">remove_trailing_whitespaces</a>
</td></tr><tr><td><a href="#remove_leading_whitespaces">remove_leading_whitespaces</a>
</td></tr></table>

### generators - Generate text inforamation.
<p id="generators"></p><table><tr><td><a href="#generate_nick">generate_nick</a>
</td><td><a href="#GeneratePassword">GeneratePassword</a>
</td></tr></table>

### validators - Validate ip, email addresses, e.t.c
<p id="validators"></p><table><tr><td><a href="#Validatorvalidate_semver">validate_semver</a>
</td><td><a href="#Validatorvalidate_email">validate_email</a>
</td><td><a href="#Validatorvalidate_ipv4">validate_ipv4</a>
</td><td><a href="#Validatorvalidate_ipv6">validate_ipv6</a>
</td></tr><tr><td><a href="#Validatorvalidate_url">validate_url</a>
</td></tr></table>


# Usage/Examples


## analaysers:

#### ```ispangram()```
##### <a href="#analysers">↑</a> Checks if inputed string is pangram (A pangram is a sentence using every letter of a given alphabet at least once.)
```python
is_pangram('Watch "Jeopardy!", Alex Trebek\'s fun TV quiz game.') 
# -> True
is_pangram('Hello beautiful world!') 
# -> False
```

#### ```is_heterogram()```
##### <a href="#analysers">↑</a> Checks if inputed string is heterogram (A heterogram is a string in which no letter of the alphabet occurs more than once.)
```python
is_heterogram("abcd")
# -> True
is_heterogram("abcdd")
# -> False
```

#### ```is_anagram()```
#### <a href="#analysers">↑</a> Checks if inputed string is an anagram (Anagram is a string that contain all letters from other string.)
```python
is_anagram("Tom Marvolo Riddle", "I Am Lord Voldemort")
# -> True
is_anagram("God", "Good")
# -> False
```

#### ```is_palindrome()```
#### <a href="#analysers">↑</a> Checks if inputed string is a palindrome (A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar.)
```python
is_palindrome(["r","a","d","a","r"])
# -> True
is_palindrome(123)
# -> False
```

#### ```is_tautogram()```
#### <a href="#analysers">↑</a> Checks if inputed string is a tautogram (A tautogram is a text in which all words start with the same letter.)
```python
is_tautogram("Crazy cat, cute, cuddly")
# -> True
is_tautogram("Crazy mouse, cute, cuddly")
# -> False
```

#### ```is_binary()```
#### <a href="#analysers">↑</a> Checks if given string or int is a binary number (A binary number is a number expressed in the base-2 numeral system or binary numeral system, a method of mathematical expression which uses only two symbols: 0 and 1)
```python
is_binary(100101010101)
# -> True
is_binary("1010010101012")
# -> False
```

#### ```count_chars()```
##### <a href="#analysers">↑</a> Returns dictionary with every character counted.
```python
count_chars("OOPp")
# -> {"O": 2, "P": 1, "p": 1}
count_chars("OOPp", lowercase=True)
# -> {"o": 2, "p": 2}
```

#### ```count_words()```
##### <a href="#analysers">↑</a> Returns an integer with every word counted.
```python
count_words("Hello world!")
# -> 2
count_words("This is me")
# -> 3
```

#### ```Levenshtein.classic_levenshtein()```
##### <a href="#analysers">↑</a> Calculates the Levenshtein distance between two strings. This version is easier to read, but significantly slower than the version below (up to several orders of magnitude). Useful for learning, less so otherwise.
```python
Levenshtein.classic_levenshtein('kitten', 'sitting')
# -> 3
Levenshtein.classic_levenshtein('kitten', 'kitten')
# -> 0
Levenshtein.classic_levenshtein('', '')
# -> 0
```

#### ```Levenshtein.damerau_levenshtein()```
##### <a href="#analysers">↑</a> Calculates the Damerau-Levenshtein distance between two strings. In addition to insertions, deletions and substitutions, Damerau-Levenshtein considers adjacent transpositions. This version is based on an iterative version of the Wagner-Fischer algorithm.
```python
Levenshtein.damerau_levenshtein('kitten', 'sitting')
# -> 3
Levenshtein.damerau_levenshtein('kitten', 'kitten')
# -> 0
Levenshtein.damerau_levenshtein('', '')
# -> 0
```

#### ```Levenshtein.recursive_levenshtein()```
##### <a href="#analysers">↑</a> Calculates the Levenshtein distance between two strings.
```python
Levenshtein.recursive_levenshtein('kitten', 'sitting')
# -> 3
Levenshtein.recursive_levenshtein('kitten', 'kitten')
# -> 0
Levenshtein.recursive_levenshtein('', '')
# -> 0
```

#### ```Levenshtein.wf_levenshtein()```
##### <a href="#analysers">↑</a> Calculates the Levenshtein distance between two strings. This version uses the Wagner-Fischer algorithm.
```python
Levenshtein.wf_levenshtein('kitten', 'sitting')
# -> 3
Levenshtein.wf_levenshtein('kitten', 'kitten')
# -> 0
Levenshtein.wf_levenshtein('', '')
# -> 0
```

#### ```Levenshtein.wfi_levenshtein()```
##### <a href="#analysers">↑</a> Calculates the Levenshtein distance between two strings. This version uses an iterative version of the Wagner-Fischer algorithm.
```python
Levenshtein.wfi_levenshtein('kitten', 'sitting')
# -> 3
Levenshtein.wfi_levenshtein('kitten', 'kitten')
# -> 0
Levenshtein.wfi_levenshtein('', '')
# -> 0
```

## converters:

#### ```bricks()```
##### <a href="#converters">↑</a> Returns bricked version of a string.
```python
bricks("Hello world!")
# -> "HeLlO WoRlD!
bricks("abcdef")
# -> "AbCdEf"
```

#### ```replaceall()```
##### <a href="#converters">↑</a> Replaces text from given sentence and dictionary.
dictionary should be formatted like this:
```python
{"old_string": "new_string"}
```
```python
replaceall("12345", {"1": "One ", "2": "Two ", "3": "Three "})
# -> "One Two Three 45"
replaceall("Hello world!", {"Hello": "Sup", "world": "earth"})
# -> "Sup earth!"
```

#### ```numerate_text()```
##### <a href="#converters">↑</a> Numerate each line of text.
```python
numerate_text("Hello world\nHow are you doing?")
# -> "1 Hello World\\n2 How are you doing?"
numerate_text("First line.\nThe second line\nThe third line")
# -> "1 First line.\n2 The second line\n3 The third line"
```

#### ```remove_trailing_whitespaces()```
##### <a href="#converters">↑</a> Remove all trailing whitespaces from sentence.
dictionary should be formatted like this
```python
remove_trailing_whitespaces("text   ")
# -> "text"
remove_trailing_whitespaces("Look at this. ")
# -> "Look at this."'''
```

#### ```remove_leading_whitespaces()```
##### <a href="#converters">↑</a> Remove all leading whitespaces from sentence.
dictionary should be formatted like this
```python
remove_leading_whitespaces("   text")
# -> "text"
remove_leading_whitespaces(" Look at this.")
# -> "Look at this."'''
```
## generators:

#### ```generate_nick()```
##### <a href="#generators">↑</a> Generate nicknames by inputed vowels, consonants, and other sounds.
```python
for i in range(20):
	print(stringtools.generate_nick(length=5))
# -> 
# Irrol
# Uppuq
# Aguir
# Moury
# Uwrax
# Ezeoa
# Agaum
# Egeti
# Efuyu
# Iruek
# Qawze
# Oguei
# Hochu
# Maqod
# Suyff
# Idoor
# Keigh
# Uredi
# Eceuy
# Elere
```

#### ```GeneratePassword()```
##### <a href="#generators">↑</a> Generate very strong passwords.
##### You can choose these options for password:
- English (abcd...)
- Numerals (1234...)
- Special Symbols ('`<*...)
- Own symbols (Any)
- Exclude similar characters (1, l, L, 0, o, O, etc.)
```python
GeneratePassword(length=50, english=True, symbols=True, numerals=True, exclude_similarities=True)
# -> "C-3?r#$a#[7n>!5\7<8s,(4W)2324C44(-3[4,!%$-!1k1+(Mg"
GeneratePassword(length=50, english=False, symbols=True, numerals=True)
# -> "_;53.?30,>92:;=.+$}>[>'6;8$1~_'>8$=504-`751]>434_&"
```


## validators:

#### ```Validator.validate_semver()```
##### <a href="#validators">↑</a> Validate if version name follows semantic versioning. For more information go to: https://semver.org/
```python
Validator.validate_semver("1.0.0")
# -> True
Validator.validate_semver("1.0.0.0")
# -> False
```

#### ```Validator.validate_email()```
##### <a href="#validators">↑</a> Validate an email address.
```python
Validator.validate_email("email@example.com")
# -> True
Validator.validate_email("email@example..com")
# -> False
```
#### ```Validator.validate_url()```
##### <a href="#validators">↑</a> Validate url address.
```python
Validator.validate_url("https://example.com/")
# -> True
Validator.validate_url("example.com")
# -> False
```

#### ```Validator.validate_ipv4()```
##### <a href="#validators">↑</a> Validate an ipv4 address.
```python
Validator.validate_ipv4("127.255.255.254")
# -> True
Validator.validate_ipv4("127.255.254")
# -> False
```

#### ```Validator.validate_ipv6()```
##### <a href="#validators">↑</a> Validate an ipv6 address.
```python
Validator.validate_ipv6("2345:0425:2CA1:0000:0000:0567:5673:23b5")
# -> True
Validator.validate_ipv6("0425:2CA1:0000:0000:0567:5673:23b5")
# -> False
```


# Authors

- [@Vazno](https://www.github.com/Vazno)
- [@toastdriven](https://github.com/toastdriven/pylev/blob/main/LICENSE) - Levenshtein funcs

## License 🔑

[MIT](https://choosealicense.com/licenses/mit/) - Copyright (c) 2022 [Beksultan Artykbaev](https://github.com/Vazno)
