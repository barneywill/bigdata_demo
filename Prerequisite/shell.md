# Shell

#!/bin/sh

| |Index|
|---|---|
|1|[Script](#script)|
|2|[Date](#date)|
|3|[String](#string)|
|4|[Loop](#loop)|
|5|[If](#if)|
|6|[Comments](#comment)|
|7|[File & Directory](#file)|
|8|[Exit](#exit)|
|9|[Other](#other)|

## 1 <a id='script'></a>Script
```
# parameter
$# : the count of parameters
$0 : the script name
$1 : the first parameter
$n : the nth parameter
$* : all pamaeters
$@ : all parameters
$? : the result of last command
\$$ : current pid

# current directory
$(cd `dirname $0`; pwd)
```

## 2 <a id='date'></a>Date
```
$ date
Wed Mar 27 17:27:18 CST 2019
$ date +"%Y-%m-%d %H:%M:%S"
2019-03-27 17:28:27
$ date +"%Y-%m-%d %H:%M:%S" --date="-1 day"
2019-03-26 17:29:10
$ date +%s
1553678982

$ date -d "-1day2019-05-20" +%Y%m%d
20190519

$ date -d"$(date -d"1 month" +"%Y%m01") -1 day" +"%Y%m%d"
20190531

$ date +"%Y%m$(cal|sed 'N;${s/.* //;P;d};D')"
20190531
```

## 3 <a id='string'></a>String 
### 3.1 replace
```
${var//a/b}
echo "$var"|awk 'gsub("a","b") {print $0}'
echo "$"|sed 's/a/b/'
```

### 3.2 substring
```
var=hello
echo ${#var}
echo $var|awk '{print substr($0, 2, 3)}'
echo ${var:2}
echo ${var:2:3}

echo ${var#he}
echo ${var%lo}

echo ${var1:`echo $((${#var2}+1))`}
```

### 3.3 split
```
str=${str//,/ }
for item in $str 
do
    echo $item
done
```
or
```
        i=1
        while((1==1))
        do
                item=`echo $str|cut -d "," -f$i`
                if [ "$item" != "" ]
                then
                        ((i++))
                        echo $item
                else
                        break
                fi
        done
```
or
```
$ echo $str|awk -F ',' '{print $1}
```
or
```
$ echo $str|awk '{split($0,arr,","); for (i in arr) {print arr[i]}}'
```

## 4 <a id='loop'></a>Loop
```
# 1
var='1 2 3'
for var in $vars
do
echo $var
done

# 2
for i in {1..100}
do
echo $i
done

# 3
i=0
for var in $vars
do
echo "$i $var"
((i=i+1))
done

# 4
#while true
while [ 1 -eq 1 ]
do
..
break/continue
..
done
```

## 5 <a id='if'></a>If

### 5.1 string
```
if [ -z "$var" ]
then
echo "var is empty"
fi

if [ -n "$var" ]
then
echo "var is not empty"
fi

if [[ "$var" = "" ]]
then
echo "empty"
fi

if [[ "$var" != "" ]]
then
echo "not empty"
fi

# string contains
if [[ "$all" == *"$sub"* ]]; then
or
if [[ "$all" =~ "$sub" ]] ;then
```

### 5.2 integer
```
if [ $a -eq 0 ]
then
echo "a = 0"
fi

if [ $a -ne 0 ]
then
echo "a != 0"
fi

if [ $a -gt 0 ]
then
echo "a > 0"
fi

if [ $a -lt 0 ]
then
echo "a < 0"
fi
```

### 5.3 if-else
```
if cond; then
...
elif cond; then
...
else
...
fi
```

### 5.4 boolean
```
# 1
if [ $a -lt 0 -a -z "$b" ]; then
　　echo ''
fi

# 2
if [ $a -lt 0 ] && [ -z "$b" ]; then
　　echo ''
fi
```

## 6 <a id='comment'></a>Comments
```
# comment

<<'COMMENT'
comment1
comment2
...
COMMENT
```

## 7 <a id='file'></a>File & Directory

### 7.1 exist
```
if [ -d "/path/to/dir" ]
then
echo 'directory /path/to/dir exists'
else
echo 'directory /path/to/dir does not exists'
fi

if [ -f "/path/to/file" ]
then
echo 'file /path/to/file exists'
else
echo 'file /path/to/file does not exists'
fi
```

### 7.2 iterate
```
dir=/path/to/dir/
for file in $dir/*
do
echo $file
done
```

## 8 <a id='exit'></a>Exit
```
exit 0
exit 1
```

## 9 <a id='other'></a>Other
```
# integer calculation
echo $((2+1))
```