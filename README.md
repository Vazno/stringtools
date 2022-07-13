# 📝 stringtools

[![Run tests](https://github.com/Vazno/stringtools/actions/workflows/pytester.yml/badge.svg?)](https://github.com/Vazno/stringtools/actions/workflows/pytester.yml)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Vazno/stringtools.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Vazno/stringtools/context:python)

Useful tool to edit strings in many ways.
#### It has tons of functions, and classes especially built to be fast and stable ⚡.


## There are 4 categories:
### analaysers - Analyse string.
<p id="analysers"></p><table><tr><td><a href="#ispangram">ispangram</a>
</td><td><a href="#is_heterogram">is_heterogram</a>
</td><td><a href="#is_anagram">is_anagram</a>
</td><td><a href="#is_palindrome">is_palindrome</a>
</td><td><a href="#is_tautogram">is_tautogram</a>
</td><td><a href="#count_chars">count_chars</a>
</td><td><a href="#count_words">count_words</a>
</td></tr></table>

### converters - Convert one string value to other string value.
<p id="converters"></p><table><tr><td><a href="#bricks">bricks</a>
</td><td><a href="#replaceall">replaceall</a>
</td><td><a href="#numerate_text">numerate_text</a>
</td><td><a href="#remove_trailing_whitespaces">remove_trailing_whitespaces</a>
</td><td><a href="#remove_leading_whitespaces">remove_leading_whitespaces</a>
</td></tr></table>

### generators - Generate text inforamation.
<p id="generators"></p><table><tr><td><a href="#generate_nick">generate_nick</a>
</td><td><a href="#Generate_password">Generate_password</a>
</td></tr></table>

### validators - Validate ip, email addresses, e.t.c
<p id="validators"></p><table><tr><td><a href="#validate_semver">validate_semver</a>
</td><td><a href="#validate_email">validate_email</a>
</td><td><a href="#validate_ipv4">validate_ipv4</a>
</td><td><a href="#validate_ipv6">validate_ipv6</a>
</td><td><a href="#validate_url">validate_url</a>
</td></tr></table>


# Installation:
``pip install stringtools``


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

#### ```Generate_password()```
##### <a href="#generators">↑</a> Generate very strong passwords.
##### You can choose these options for password:
- English (abcd...)
- Numerals (1234...)
- Special Symbols ('`<*...)
- Own symbols (Any)
- Exclude similar characters (1, l, L, 0, o, O, etc.)
```python
Generate_password(length=50, english=True, symbols=True, numerals=True, exclude_similarities=True)
# -> "C-3?r#$a#[7n>!5\7<8s,(4W)2324C44(-3[4,!%$-!1k1+(Mg"
Generate_password(length=50, english=False, symbols=True, numerals=True)
# -> "_;53.?30,>92:;=.+$}>[>'6;8$1~_'>8$=504-`751]>434_&"
```


## validators:

#### ```validate_semver()```
##### <a href="#validators">↑</a> Validate if version name follows semantic versioning. For more information go to: https://semver.org/
```python
validate_semver("1.0.0")
# -> True
validate_semver("1.0.0.0")
# -> False
```

#### ```validate_email()```
##### <a href="#validators">↑</a> Validate an email address.
```python
validate_email("email@example.com")
# -> True
validate_email("email@example..com")
# -> False
```

#### ```validate_ipv4()```
##### <a href="#validators">↑</a> Validate an ipv4 address.
```python
validate_ipv4("127.255.255.254")
# -> True
validate_ipv4("127.255.254")
# -> False
```

#### ```validate_ipv6()```
##### <a href="#validators">↑</a> Validate an ipv6 address.
```python
validate_ipv6("2345:0425:2CA1:0000:0000:0567:5673:23b5")
# -> True
validate_ipv6("0425:2CA1:0000:0000:0567:5673:23b5")
# -> False
```

#### ```validate_url()```
##### <a href="#validators">↑</a> Validate url address.
```python
validate_url("https://example.com/")
# -> True
validate_url("example.com")
# -> False
```


## Authors

- [@Vazno](https://www.github.com/Vazno)


## License 🔑

[MIT](https://choosealicense.com/licenses/mit/) - Copyright (c) 2022 [Beksultan Artykbaev](https://github.com/Vazno)