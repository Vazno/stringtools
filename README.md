# 📝 stringtools 
Useful tool to edit strings in many ways.
#### It has tons of functions especially built to be fast and stable ⚡.
- order
- is_pangram
- camelCase
- bricks
- generate_nick
## Installation:
``pip install stringtools``

## Usage/Examples

```python
import stringtools
stringtools.order("worl1d name5 He0llo is3 what2 your4 ?6", 
    pl_indexing=True, del_index_numerals=True)
--> "Hello world what is your name ?"

stringtools.order("worl1d name5 He0llo is3 what2 your4 ?6", True, False)
--> "He0llo worl1d what2 is3 your4 name5 ?6"


stringtools.camelCase("CamelCase")
--> "Camel Case"

stringtools.camelCase("Camel Case", reverse_=True)
--> "CamelCase"

e.t.c...
```

## Authors

- [@Vazno](https://www.github.com/Vazno)


## License 🔑

[MIT](https://choosealicense.com/licenses/mit/) - Copyright (c) 2022 [Beksultan Artykbaev](https://github.com/Vazno)