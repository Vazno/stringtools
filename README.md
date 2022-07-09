# 📝 stringtools

[![Run tests](https://github.com/Vazno/stringtools/actions/workflows/pytester.yml/badge.svg?)](https://github.com/Vazno/stringtools/actions/workflows/pytester.yml)

Useful tool to edit strings in many ways.
#### It has tons of functions, and classes especially built to be fast and stable ⚡.


## There are 3 categories:
### analaysers - Analyse string
<p id="analysers"></p><table><tr><td><a href="#ispangram">ispangram</a>
</td><td><a href="#is_heterogram">is_heterogram</a>
</td><td><a href="#is_anagram">is_anagram</a>
</td><td><a href="#is_palindrome">is_palindrome</a>
</td><td><a href="#is_tautogram">is_tautogram</a>
</td><td><a href="#count_char">count_char</a>
</td></tr></table>

### converters - Convert one string value to other string value
<p id="converters"></p><table><tr><td><a href="#bricks">bricks</a>
</td></tr></table>

### generators - Generate text inforamation.
<p id="generators"></p><table><tr><td><a href="#generate_nick">generate_nick</a>
</td><td><a href="#Generate_password">Generate_password</a>
</td></tr></table>


# Installation:
``pip install stringtools``


# Usage/Examples


## analaysers:

#### ```ispangram()```
##### <a href="#analysers">↑</a> Checks if inputed string is pangram (If it has every letter from aplhabet) e.g:

```python
is_pangram('Watch "Jeopardy!", Alex Trebek\'s fun TV quiz game.') 
# -> True
is_pangram('Hello beautiful world!') 
# -> False
```

#### ```is_heterogram()```
##### <a href="#analysers">↑</a> A heterogram is a string in which no letter of the alphabet occurs more than once
```python
is_heterogram("abcd")
# -> True
is_heterogram("abcdd")
# -> False
```

#### ```is_anagram()```
#### <a href="#analysers">↑</a> Anagram it's a string that contain all letters from other string 
```python
is_anagram("Tom Marvolo Riddle", "I Am Lord Voldemort")
# -> True
is_anagram("God", "Good")
# -> False
```

#### ```is_palindrome()```
#### <a href="#analysers">↑</a> A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar.
```python
is_palindrome(["r","a","d","a","r"])
# -> True
is_palindrome(123)
# -> False
```
#### ```is_tautogram()```
#### <a href="#analysers">↑</a> A tautogram is a text in which all words start with the same letter.
```python
is_tautogram("Crazy cat, cute, cuddly")
# -> True
is_tautogram("Crazy mouse, cute, cuddly")
# -> False
```

#### ```count_char()```
##### <a href="#analysers">↑</a> Returns dictionary with every character counted e.g
```python
count_char("OOPp")
# -> {"O": 2, "P": 1, "p": 1}
count_char("OOPp", lowercase=True)
# -> {"o": 2, "p": 2}
```


## converters:

#### ```bricks()```
##### <a href="#converters">↑</a> Returns bricked version of string
```python
bricks("Hello world!")
# -> "HeLlO WoRlD!
bricks("abcdef")
# -> "AbCdEf"
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


## Authors

- [@Vazno](https://www.github.com/Vazno)


## License 🔑

[MIT](https://choosealicense.com/licenses/mit/) - Copyright (c) 2022 [Beksultan Artykbaev](https://github.com/Vazno)