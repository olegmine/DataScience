import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Создаем словарь уникальных значений столбца 'whoAmI'
unique_values = data['whoAmI'].unique()
value_to_int = {x: i for i, x in enumerate(unique_values)}

# Создаем пустой DataFrame для one hot представления
one_hot_df = pd.DataFrame(columns=unique_values)

# Заполняем one hot DataFrame
for value in data['whoAmI']:
    one_hot_row = [0] * len(unique_values)
    one_hot_row[value_to_int[value]] = 1
    one_hot_df = one_hot_df.append(pd.Series(one_hot_row, index=unique_values), ignore_index=True)

print(one_hot_df.head())
