# Pandas

| |Index|
|---|---|
|1|select|
|2|filter|
|3|new column|
|4|rename column|
|5|groupby|
|6|sort|
|7|drop, drop_duplicates|
|8|join|
|9|fillna|
|10|limit|
|11|count|
|12|split|
|13|explode|
|14|read files|

## 0 create
```
data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
df = pd.DataFrame(data, index=['a', 'b'], columns=['col1', 'col2', 'col3'])
```

## 1 select
```
df = df[['col1', 'col2', 'col3']]
```

## 2 filter
```
# equals
df = df[df.col1 == 1]
# is null
df = df[df.col1.isnull()]
# not null
df = df[df.col1.notnull()]
# startswith
df = df[df.status.str.startswith('cancelled')]
# multiple conditions
df = df[(df['col1'] > 10) & (df['col1'] < 20)]
# filter a list element
df[df['words'].map(len) >= min_word_count]
# include a string
df[(df.answer.notnull()) & (df.answer.str.find('no') == -1)]
# exclude some strings
stop_words_set = {'w1', 'w2'}
df = df[~df['words'].isin(stop_words_set)]
```

## 3 new column
```
df['Cancellation Rate'] = round(df['cancel_count'] / df['count'], 2)

df['words'] = df['words'].str.lower()
df['words'] = df['words'].str.replace(' ', '_')

df['words'] = df['words'].apply(lambda item: re.sub(r'[^a-zA-Z]', '', str(item).lower()))
df['word_count'] = df.answer.apply(lambda item: 0 if pd.isna(item) else len(str(item).strip().split()))

df['col1'] = 'N'
df.loc[(text_df['col2'] == 'whatever'), 'col1'] = 'P'
```

## 4 rename column
```
df.rename(columns={'original_name':'new_name'}, inplace=True)
```

## 5 groupby
```
df = person.groupby(['email']).size().reset_index(name='count')
```

## 6 sort
```
person.sort_values(by='id', inplace=True)
```

## 7 drop
```
del df['col1']

df.pop('col1')
# drop columns
df.drop(['col1', 'col2'])
df.drop(['col1', 'col2'], axis='columns')
df.drop(columns=['col1', 'col2'])
# drop indexs
df.drop([0, 1])
df.drop([0, 1], axis='index')
df.drop(index=[0, 1])
```

### 7.1 drop_duplicates
```
person.drop_duplicates(subset=['email'], keep='first', inplace=True)
```

## 8 join
```
person.join(address.set_index('personId'), on=['personId'], how='left', lsuffix='_l', rsuffix='_r')
```

## 9 fill null with zero
```
df_result['cancel_count'] = df_result['cancel_count'].fillna(0)
```

## 10 limit
```
# top 10
df[:10]

df.loc[1]
df.loc[[1, 2]]
df.iloc[1]
df.iloc[[1, 2]]

df.head()
df.head(10)
df.head().T
```

## 11 count
```
len(df.index)
len(df.col1.notnull().index)
len(df.col1.unique())
```

## 12 split
```
df['words'] = df['lines'].str.split()
```

## 13 explode
```
df = df.explode('words')
```

## 14 read files
```
import glob
import pandas as pd
filenames = glob.glob('/path/to/*.csv')
df = pd.concat((pd.read_csv(f) for f in filenames), ignore_index=True)
```

## 15 write
```
df.to_csv('filepath')
df.to_dict(orient='records')
```

## 16 print full text
```
pd.set_option('display.max_colwidth', None)
```

