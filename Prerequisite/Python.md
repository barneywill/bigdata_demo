# Python

| |Index|
|---|---|
|0|[Hello World](#hello)|
|1|[String](#string)|
|2|[Loop](#loop)|
|3|[Condition](#condition)|
|4|[Collection(List, Set, Dictionary)](#collection)|
|5|[Tuple](#tuple)|
|6|[IO](#io)|
|7|[Multiprocessing](#process)|
|8|[Optional](#optional)|
|9|[Exception(try, except, else, finally)](#exception)|
|10|[Lambda](#lambda)|
|11|[Read Mysql](#mysql)|

## 0 <a id='hello'></a>Hello World
```
import argparse

parser = argparse.ArgumentParser(prog='ProgramName', description='What the program does', epilog='Text at the bottom of help')
parser.add_argument('name')

if __name__ == '__main__':
    args = parser.parse_args()
    print('Hello World : ' + args.name)
```

## 1 <a id='string'></a>String
### 1.1 interpolation
string format
```
s = 'hello'
s += str(123)
print(f'{a} world')
print('%s world' % s)
```

### 1.2 lower, upper, captalize, empty
```
# is alphanumeric
print(s.isalum())

# lower, upper, captalize
print(s.lower())
print(s.upper())
print(s.capitalize())

# is empty
print(not s)
print(s == '')
print(len(s) == 0)
print(s != '')
print(len(s) > 0)
```

### 1.3 substring, startswith
```
'hello'[1:3]
'hello'.startswith('he')
```

### 1.4 index, find
```
s = "banana"
print(s.find("an"))
print(s.find("an",2))
print(s.rfind("an"))

print(s.index("an"))
print(s.index("an",2,6))
print(s.rindex("an"))
```

### 1.5 split
```
s = 'abc def'
for word in s.split(' '):
    print(word)
```

### 1.6 iterate chars
```
s = 'abc'
for i, c in enumerate(s):
    print(f'{i} {c}')

for i in range(len(s)):
    print(s[i])
```

### 1.7 date
date format
```
import datetime

today = datetime.datetime.today()
print(f"{today:%Y%m%d}")
```

## 2 <a id='loop'></a>Loop
```
for i in range(10):
    print(i)

for i in range(10, -1, -1):
    print(i)
```

## 3 <a id='condition'></a>Condition
```
int_str = 'even' if i % 2 == 0 else 'odd'

if i == 0:
    print('zero')
elif i == 1:
    print('one')
else:
    print('other')
```

### switch
```
match i:
    case 0:
        print('zero')
    case 1:
        print('one')
    case _:
        print('other')
```

## 4 <a id='collection'></a>Collection

### 4.1 List
#### 4.1.1 Basics
```
ls = [1, 2, 3]
ls.append(4)
ls.insert(0, 0)
ls += [5, 6]
print(ls)
print(' '.join(v for v in ls))

# length
print(len(ls))
# remove one
print(ls.pop(0))
# get the first one
print(ls[0])
# get the last one
print(ls[-1])
```

#### 4.1.2 Iterate
```
ls = [1, 2, 3]

for v in ls:
    print(v)

for i, c in enumerate(ls):
    print(f'{i} {c}')
```

#### 4.1.3 Sort
sort, sorted
```
ls = [1, 4, 2, 3]

# sort
print(sorted(ls))
print(ls)
ls.sort()
print(ls)

# reverse sort
ls.sort(reverse=True)
print(ls)
```

#### 4.1.4 min, max, sum
```
ls = [1, 4, 2, 3]
print('min %d, max %d, sum %d' % (min(ls), max(ls), sum(ls)))
```

#### 4.1.5 foldLeft
```
import functools as f
ls = [1, 4, 2, 3]
print(f.reduce(lambda acc, item: acc + (item if item % 2 == 0 else 0), ls))
```

#### 4.1.6 map, collect
```
ls = [1, 4, 2, 3]
ls_double = [v * 2 for v in ls]
```

#### 4.1.7 filter, map, collect
```
ls = [1, 4, 2, 3]
ls_filter_double = [v * 2 for v in ls if v % 2 == 0]
```

#### 4.1.8 slice
sub-list
```
ls = [1, 4, 2, 3]
print(ls[1:3])
print(ls[1:])
print(ls[:3])
print(ls[:])
print(ls[-2:])
print(ls[::-1])
```

### 4.2 Set
```
s = set()
s = {1, 2, 3}
s.add(1)
s.remove(2)
print(2 in s)
```

### 4.3 Dictionary
```
d = {'b':2}
if d.get('a') is None:
    d['a'] = 1
else:
    d['a'] += 1
print(d['a'])

d.pop('a')

print(d.keys())
print(d.values())

for k, v in d.items():
    print(f'{k} {v}')

arr = [(k, v) for k, v in d.items()]
```

## 5 <a id='tuple'></a>Tuple
```
def statistics(ls: list) -> tuple[int, int, float]:
    return (min(ls), max(ls), sum(ls)/len(ls))
ls = [1, 4, 2, 3]
stat = statistics(ls)
print(stat[0], stat[1], stat[2])
print('min %d, max %d, avg %f' % stat)
```

### Sort
```
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
```

## 6 <a id='io'></a>IO
```
# read
f = open('/tmp/test', 'r')
print(f.read())
# line by line
lines = f.readlines()
for line in lines:
    print(line)

# write
f = open("/tmp/test", "w")
f.write("hello")
f.close()
```

## 7 <a id='process'></a>Multiprocessing
```
from multiprocessing import Process
from multiprocessing import Pool
import time
import random

def say_hello(name):
    r = random.randint(1, 10)
    time.sleep(r)
    print(f'hello{r} {name}')

if __name__ == '__main__':
    # one process
    start_time = time.perf_counter()
    p = Process(target=say_hello, args='world')
    p.start()
    p.join()
    end_time = time.perf_counter()
    print('process done in %d seconds' % end_time - start_time)

    # process pool
    start_time = time.perf_counter()
    with Pool() as pool:
        result = pool.map(say_hello, range(10))
    end_time = time.perf_counter()
    print('pool done in %d seconds' % end_time - start_time)
```

## 8 <a id='optional'></a>Optional
```
from typing import Optional
def example(value: Optional[str]) -> str:
    return "none" if value is None else value
```

## 9 <a id='exception'></a>Exception
```
try:
    raise ValueError('hello')
except NameError:
    print('NameError')
except ValueError as e:
    print(e)
except:
    print('exception')
else:
    print('all right')
finally:
    print('clean up')
```

## 10 <a id='lambda'></a>Lambda
```
add_ten = lambda arg : arg + 10
print(add_ten(5))

multiply = lambda x, y: x * y
print(multiply(3, 4))
```

## 11 <a id='mysql'></a>Read Mysql
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

# tuple
for x in myresult:
  print(x)
```

## 12 Other
```
python -m http.server
```
