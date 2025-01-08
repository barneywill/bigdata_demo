# Python

| |Index|
|---|---|
|1|[String](#string)|
|2|[Loop](#loop)|
|3|[Condition](#condition)|
|4|[Collection(List, Set, Dictionary)](#collection)|
|5|[IO](#io)|
|6|[Optional](#optional)|
|7|[Lambda](#lambda)|

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
```
l = [1, 2, 3]
l.append(4)
l.insert(0, 0)
l += [5, 6]
print(l)

# length
print(len(l))
# remove one
print(l.pop(0))
# get the first one
print(l[0])
# get the last one
print(l[-1])

# map
l_double = [v * 2 for v in l]

# filter, map
l_filter_double = [v * 2 for v in l if v % 0 == 0]

for i, c in enumerate(l_double):
    print(f'{i} {c}')
```

#### Sort
```
l = [1, 4, 2, 3]
l.sort()
print(l)
```

### 4.2 Set
```
s = set()
s.add(1)
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

print(d.keys())
print(d.values())

for k, v in d.items():
    print(f'{k} {v}')

arr = [(k, v) for k, v in d.items()]
```

## 5 <a id='io'></a>IO
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

## 6 <a id='optional'>Optional
```
from typing import Optional
def example(value: Optional[str]) -> str:
    return "none" if value is None else value
```

## 7 <a id='lambda'></a>Lambda
```
add_ten = lambda arg : arg + 10
print(add_ten(5))

multiply = lambda x, y: x * y
print(multiply(3, 4))
```

