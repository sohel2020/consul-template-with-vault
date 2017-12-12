import flask

>>> content = None
>>> with open('env') as f:
...     content = f.read()
...
>>> content
'username=Aniruddha\npassword=1234\n'
>>>
>>> content.split()
['username=Aniruddha', 'password=1234']
>>> content.split('\n)
  File "<stdin>", line 1
    content.split('\n)
                     ^
SyntaxError: EOL while scanning string literal
>>> content.split('\n')
['username=Aniruddha', 'password=1234', '']
>>> filter(lambda x: '=' in x, content.split('\n'))
<filter object at 0x10d932e80>
>>> list(filter(lambda x: '=' in x, content.split('\n')))
['username=Aniruddha', 'password=1234']
>>> l = list(filter(lambda x: '=' in x, content.split('\n')))
>>> l
['username=Aniruddha', 'password=1234']
>>> l[-1]
'password=1234'
>>> {x: y for item.split('=')[0], item.split('=')[0] in l }
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <dictcomp>
ValueError: too many values to unpack (expected 2)
>>> {x: y for item.split('=')[0], item.split('=')[0] in l }
KeyboardInterrupt
>>>
KeyboardInterrupt
>>> l
['username=Aniruddha', 'password=1234']
>>> dict([('username', '1234'), ('password', '12345')])
{'username': '1234', 'password': '12345'}
>>> l = list(map(lambda x: x.split('='), l))
>>> l
[['username', 'Aniruddha'], ['password', '1234']]
>>> dict(l)
{'username': 'Aniruddha', 'password': '1234'}
>>>