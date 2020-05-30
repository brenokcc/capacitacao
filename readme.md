# Python Deep Dive
**Servidor**: Carlos Breno Pereira Silva

**E-mail**: breno.silva@ifrn.edu.br

## Sobre
Este projeto tem o objetivo de documentar as atividades práticas (projetos e exercícios) implementadas durante a
capacitação realizada entre 02/03/2020 a 30/05/2020.

## Cursos

Foi realizada uma série de quatro cursos avançados da linguagem de programação Python na plataforma de ensino
 Udemy.
 
- https://www.udemy.com/course/python-3-deep-dive-part-1/
- https://www.udemy.com/course/python-3-deep-dive-part-2/
- https://www.udemy.com/course/python-3-deep-dive-part-3/
- https://www.udemy.com/course/python-3-deep-dive-part-4/


### Parte 01 - Funcional
    
#### Conteúdo

- Variables

- Namespaces and scope

- Python's numeric types

- Python boolean type

- Run-time vs compile-time

- Functions in general (including lambdas)

- Functional programming techniques (map, reduce, filter, zip, etc)

- Closures

- Decorators

- Imports, modules and packages

- Tuples as data structures

- Named tuples
#### Anotações

- Escopos
    
A palavra reservada "global" serve para acessar variáveis globais.
    
A palavra reservada "nonlocal" serve para acessar variáveis em "closures".
   
```
def counter():
    count = 0 # local variable
    
    def inc():
        nonlocal count  # this is the count variable in counter
        count += 1
        return count
    return inc

c = counter()
c()
c()
print(c.__closure__)
```    

-  Funções lambda, filter, map, reduce, zip
```python
from functools import reduce
numbers = [0, 1, 2, 3]
is_par = lambda n: n % 2 == 0
double = lambda n: n * 2
add = lambda x, y: x + y
for n in filter(is_par, numbers): print(n)
for n in map(double, numbers): print(n)
print(reduce(add, numbers))
for n, pow in zip((1, 2, 3), (1, 4, 9)): print(n, pow)
```
- Decoradores

Decoradores são geralmente implementados como funções:

```
def html_image(width, height):
  def decorator(func):
    def wrapper(*args, **kwargs):
        url = func(*args, **kwargs)
        return '<img src="{}" width="{}" height="{}"/>'.format(
            url, width, height)
    return wrapper
  return decorator

@html_image(16, 16)
def default_icon():
    return '/media/icons/default.ico'

print(default_icon())

```

Mas podem ser implementados como classes também:

```
class HtmlImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            url = func(*args, **kwargs)
            return '<img src="{}" width="{}" height="{}"/>'.format(
                url, self.width, self.height)
        return wrapper

@HtmlImage(16, 16)
def default_icon():
    return '/media/icons/default.ico'

print(default_icon())

```


### Parte 02 - Iteração

#### Conteúdo
- Sequences

- Iterables

- Iterators

- Generators

- Comprehensions

- Context managers

- Generator based coroutines 
#### Anotações
- Protocolo de Sequência
```
def __len__():
    pass
def __getitem__(key):
    return None
def __setitem__(key, value):
    pass
def __delitem__(key):
    pass
def __reversed__():
    pass
def __contains__(obj):
    return True
```
- Protocolo de Iterável
```
# deve retornar um iterador
def __iter__():
    return Nome
```
- Protocolo de Iterador
```
# dever retornar o próximo elemento a ser iterado
def __next__():
    raises StopIteration
```
Exemplo de um iterador iterável:

```
FRUITS = ['banana', 'apple', 'grape', 'orange']

class FruitIterator:
 def __init__(self):
  self.i = 0
 
 def __next__(self):
  if self.i < len(FRUITS):
   self.i+=1
   return FRUITS[self.i-1]
  raise StopIteration()
  
 def __iter__(self):
  return self


for f in FruitIterator():
 print(f)
```
- Geradores

Gerador é um padrão de codificação que possibilita a iteração em um conjunto de objetos cujos elementos são criados em tempo de execução.

Imagine a iteração dos 5 primeiros números pares maiores que zero.

Ela pode ser feita através de uma lista:

```
l = [2, 4, 6, 8, 10]
for n in l:
 print(l)
```

Ela pode ser feita através de um iterador iterável:
```
class Pares:
 def __init__(self):
  self.i = 0

 def __next__(self):
  if self.i < 10:
   self.i += 2
   return self.i
  raise StopIteration()

 def __iter__(self):
  return self


for i in Pares():
 print(i)
```
Ou mais simplisticamente através de uma função geradora:
```
def pares():
 n = 0
 while n < 10:
  n+=2
  yield n

for i in pares():
 print(i)
```
- Comprehensions

```
l = [n for n in range(1, 5)] # lista
d = {n:str(n) for n in range(1, 5)} # dicionário
g = (x for x in range(1, 5)) # gerador
```
 

- Protocolo de Gerenciador de Contexto

Utilizado em situações nais quais se deseja garantir a execução de uma determinal ação sempre que uma outra for realizada.
Ex: fechar arquivo depois de abri-lo, encerrar a conexão depois de iniciada, etc.
```
def __enter__():
    pass

def __exit__(exc_type, exc_value, traceback):
    pass
```

Exemplo:

```
import paramiko

class SSHConnection():
 def __init__(self):
  self.client = None
 
 def __enter__(self):
  self.client = paramiko.SSHClient()
  self.client.load_system_host_keys()
  self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  self.client.connect(hostname='djangoplus.net',username='root')
  print('Connection opened!')
  return self
 
 def execute(self, cmd):
  stdin,stdout,stderr = self.client.exec_command(cmd)
  print(stderr.channel.recv_exit_status())
  print(stdout.read().decode())
  print(stderr.read().decode())
 
 def __exit__(self, exc_type, exc_value, traceback):
  self.client.close()
  print('Connection closed!')
 

with SSHConnection() as conn:
 conn.execute('pwd')
```

Gerenciadores de contexto pode ser implementados sob a forma de gerador ao invés de classe

Exemplo:

```
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()
```


### Parte 03 - Mapas

#### Conteúdo
- Associative arrays

- Hash functions

- Python dictionaries and sets

- Specialized dictionary structures (OrderedDict)

- Python's implementation of multi-sets

- Counter class

- ChainMap class

- Custom dictionaries by inheriting from the UserDict class

- Serialization and deserialization of dictionaries to JSON

- Schemas in custom JSON deserialization

- JSONSchema, Marshmallow, PyYaml and Serpy
#### Anotações

- Criando dicionários com UserDict

Permite armazenar os dados em uma estrutura de dados customizável sem necessitar implementar toda a interface de dicionários.

```
from collections import UserDict
import json
class JsonDict(UserDict):
    def __init__(self, s):
        self.data = json.loads(s)
    def __setitem__(self, key, value):
        self.data[key] = value
    def __getitem__(self, key):
        return self.data[key]
    def __str__(self):
        return json.dumps(self.data)
    def __repr__(self):
        return "JsonDict('{}')".format(str(self))

d = JsonDict('{"a": 1}')
print(d)
print(repr(d))
```


### Parte 04 - POO
    
#### Conteúdo
- Classes and instances

- Class data and function attributes

- Properties

- Instance, class and static methods

- Polymorphism and special functions

- Single inheritance

- Slots

- Descriptor protocol and its relationship to properties and functions

- Enumerations

- Exceptions

- Metaprogramming (including metaclasses)
#### Anotações

- Propriedades

Pode ser definidas com decoradores:

```
from numbers import Integral

class Person:
    @property
    def age(self):
        return getattr(self, '_age', None)
    
    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer.')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value
```

Ou podem ser definidas com a classe "property":

```
class Person:
    def get_age(self):
        return getattr(self, '_age', None)
    
    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer.')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value
        
    age = property(fget=get_age, fset=set_age)
```

- Protocolo de Descritores

```
def __set_name__(self, cls, name):
    pass

def __get__(self, obj, cls=None):
    return

def __set__(self, obj, value):
    pass

def __delete__(self, obj):
    pass
```
Aplicação:

```
class Attribute:
 def __init__(self, cls_type):
  self.name = None
  self.cls_type = cls_type
 def __set_name__(self, cls, name):
  self.name = name
 def __get__(self, obj, cls=None):
  return obj.__dict__.get(self.name) if obj else self
 def __set__(self, obj, value):
  obj.__dict__[self.name] = None if value is None else self.cls_type(value)
 

class Object:
 nome = Attribute(str)
 idade = Attribute(int) 

o = Object()
o.nome = 'Breno'
o.idade = '4'

print(type(o.nome), type(o.idade))
```

- Métodos

Assim como atributos, é possível definir métodos em tempo de execução.

A definição de novos métodos podem ser a nível classe:

```
class Object:
    def x(self):
        print('x')

def y(self):
    print('y')

Object.y = y

o = Object()
o.x()
o.y()
```

Ou a nível de instâncias:

```
import types

class Object:
    def x(self):
        print('x')

def y(self):
    print('y')

o = Object()
o.y = types.MethodType(y, o)

o.x()
o.y()
```

- Criando classes em tempo de execução

Classes podem ser criadas em tempo de execução através de chamadas "type(cls_name, cls_bases, cls_dict)":

```
Pessoa = type('Pessoa', (), dict(nome=None, idade=None, get_idade=lambda self: self.idade))
p = Pessoa()
p.idade = 35
p.get_idade()

```


- Herança, Decoradores e Metaclasse

A inclusão de propriedades (atributos) ou comportamentos (métodos) em classes pode se dar através de herança, decoradores ou metaclasses:

Usando herança:

```
import json
class JsonObject:
    def to_json(self):
        return json.dumps(self.__dict__)


class Person(JsonObject):
    def __init__(self):
        self.name = None
    
p = Person()
p.name = 'Breno'
p.to_json()
```

Usando decorador:

```
def json_object(cls):
    def to_json(self):
        return json.dumps(self.__dict__)
    cls.to_json = to_json
    return cls

@json_object
class Person(JsonObject):
    def __init__(self):
        self.name = None

p = Person()
p.name = 'Breno'
p.to_json()
```

Usando metaclasse:

```
class JsonType(type):
    def __new__(mcls, name, bases, class_dict):
        new_cls = super().__new__(mcls, name, bases, class_dict)
        def to_json(self):
            return json.dumps(self.__dict__)
        new_cls.to_json = to_json
        return new_cls

class Person(metaclass=JsonType):
    def __init__(self):
        self.name = None

p = Person()
p.name = 'Breno'
p.to_json()

```




