# 📝 stringtools

[![Run tests](https://github.com/Vazno/stringtools/actions/workflows/pytester.yml/badge.svg?)](https://github.com/Vazno/stringtools/actions/workflows/pytester.yml)

Useful tool to edit strings in many ways.
#### It has tons of functions especially built to be fast and stable ⚡.
- order
- is_pangram
- camelCase
- count_char
- bricks
- generate_nick
## Installation:
``pip install stringtools``


## Usage/Examples

## ```ispangram()```
#### Checks if inputed string is pangram (If it has every letter from aplhabet) e.g:
```python
is_pangram('Watch "Jeopardy!", Alex Trebek\'s fun TV quiz game.') 
# -> True
is_pangram('Hello beautiful world!') 
# -> False
```


## ```camelCase()```
#### Splits camelCase into two words e.g.
```python
stringtools.camelCase("CamelCase")
# -> "Camel Case"
stringtools.camelCase("Camel Case", reverse_=True) 
#-> "CamelCase"
```


## ```count_char()```
#### Returns dictionary with every character counted e.g
```python
count_char("OOPp")
# -> {"O": 2, "P": 1, "p": 1}
count_char("OOPp")
# -> {"o": 2, "p": 2}
```


## ```bricks()```
#### Returns bricked version of string
```python
bricks("Hello world!")
# -> "HeLlO WoRlD!
bricks("abcdef")
# -> "AbCdEf"
```


## ```generate_nick()```
#### Generate nicknames by inputed vowels, consonants, and other sounds.
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



## ```Generate_password()```
#### Generate very strong passwords.
#### You can choose these options for password:
- English (abcd...)
- Numerals (1234...)
- Special Symbols ('`<*...)
- Own symbols (Any)
###### Exclude similar characters (1, l, L, 0, o, O, etc.)
```python
Generate_password(length=50, english=True, symbols=True, numerals=True, exclude_similarities=True)
# -> "C-3?r#$a#[7n>!5\7<8s,(4W)2324C44(-3[4,!%$-!1k1+(Mg"
Generate_password(length=50, english=False, symbols=True, numerals=True, uppercase=False)
# -> "_;53.?30,>92:;=.+$}>[>'6;8$1~_'>8$=504-`751]>434_&"
```


## Authors

- [@Vazno](https://www.github.com/Vazno)


## License 🔑

[MIT](https://choosealicense.com/licenses/mit/) - Copyright (c) 2022 [Beksultan Artykbaev](https://github.com/Vazno)