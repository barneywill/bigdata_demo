import re

from collections import Counter

import pandas as pd

file_path = '/path/to/a/textfile'
f = open(file_path, 'r')
lines = f.readlines()

# 1. Counter
words = []
for line in lines:
    for word in line.split(' '):
        word_clean_lower = re.sub(r'[^a-zA-Z]', '', word).lower()
        if word_clean_lower != '':
            words.append(word_clean_lower)
top10 = Counter(words).most_common(10)

print(top10)

# 2. pandas DataFrame
df = pd.DataFrame({'lines':lines})
df['words'] = df['lines'].str.split()
df.pop('lines')
df = df.explode('words')
df['words'] = df['words'].apply(lambda item: re.sub(r'[^a-zA-Z]', '', str(item).lower()))
df = df[df['words'] != ''].value_counts().reset_index()
df.columns=['word', 'count']
df.sort_values('count', ascending=False)
top10 = df.iloc[:10]

print(top10)

# 3. just python
word_dic = {}
for line in lines:
    for word in line.split(' '):
        word_clean_lower = re.sub(r'[^a-zA-Z]', '', word).lower()
        if word_clean_lower != '':
            if word_dic.get(word_clean_lower) is None:
                word_dic[word_clean_lower] = 1
            else:
                word_dic[word_clean_lower] += 1
print(word_dic)
arr = [(k, v) for k, v in word_dic.items()]
arr.sort(reverse=True, key=lambda item: item[1])
top10 = arr[1:10]

print(top10)