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
##### lambda, filter, map, reduce, zip
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

- Protocolo de Descritores

```
def __get__(self, obj, cls=None):
    return

def __set__(self, obj, value):
    pass

def __delete__(self, obj):
    pass
```

