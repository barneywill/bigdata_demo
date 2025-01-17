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
|11|split|
|12|explode|


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
# startswith
df = df[df.status.str.startswith('cancelled')]
# multiple conditions
df = df[(df['col1'] > 10) & (df['col1'] < 20)]
```

## 3 new column
```
df['Cancellation Rate'] = round(df['cancel_count'] / df['count'], 2)
df['words'] = df['words'].apply(lambda item: re.sub(r'[^a-zA-Z]', '', str(item).lower()))
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
```

## 11 split
```
df['words'] = df['lines'].str.split()
```

## 12 explode
```
df = df.explode('words')
```