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
|7|[Optional](#optional)|
|8|[Exception(try, except, else, finally)](#exception)|
|9|[Lambda](#lambda)|

## 0 <a id='hello'></a>Hello World
```
if __name__ == '__main__':
    print('Hello World')
```

## 1 <a id='string'></a>String
```
s = 'hello'
s += str(123)
print(f'{a} world')

# is alphanumeric
print(s.isalum())
print(s.lower())
print(s.upper())
print(s.capitalize())
```

### split
```
s = 'abc def'
for word in s.split(' '):
    print(word)
```

### iterate chars
```
s = 'abc'
for i, c in enumerate(s):
    print(f'{i} {c}')
```

### date
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
for v in ls_double:
    print(v)

for i, c in enumerate(ls_double):
    print(f'{i} {c}')
```

#### 4.1.3 Sort
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

## 7 <a id='optional'>Optional
```
from typing import Optional
def example(value: Optional[str]) -> str:
    return "none" if value is None else value
```

## 8 <a id='exception'></a>Exception
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

## 9 <a id='lambda'></a>Lambda
```
add_ten = lambda arg : arg + 10
print(add_ten(5))

multiply = lambda x, y: x * y
print(multiply(3, 4))
```

