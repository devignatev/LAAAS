import pandas as pd
import yaml
import random

'''
 Функция переводит датафрейм в понятное значение для Арлекино
 
Вход: Дата фрейм формата:
 
       D20S1082_1  D20S1082_2  D6S474_1  ...  D7S1517_2  Penta E_1  Penta E_2
YAK1         16.0        16.0      17.0  ...       22.0       16.0       11.0
YAK2         11.0        15.0      17.0  ...       20.0       16.0       18.0
YAK3         18.0        11.0      15.0  ...       25.0       16.0       22.0
YAK4         11.0        11.0      15.0  ...       20.0       15.0        7.0
YAK5         16.0        11.0      18.0  ...       20.0       19.0       10.0
YAK6         15.0        12.0      16.0  ...       20.0       15.0        7.0
YAK7         11.0        15.0      14.0  ...       25.0       19.0       16.0
YAK8         11.0        11.0      18.0  ...       23.0        5.0       16.0
YAK9         11.0        11.0      15.0  ...       23.0       11.0       17.0
YAK10        16.0        11.0      14.0  ...       21.0       10.0       14.0
 
[10 rows x 50 columns]

Выход: Дата фрейм формата:
 
       1  D20S1082  D6S474  D14S1434  ...  D21S2050  D10S2325  D7S1517  Penta E
YAK1   1      13.0    18.0      12.0  ...      16.1      13.0     22.0      9.0
              15.0    14.0      13.0  ...      27.0      16.0     19.0     11.0
YAK2   1      11.0    15.0      14.0  ...      28.0      16.0     20.0     16.0
              11.0    14.0      11.0  ...      30.0       9.0     20.0     20.0
YAK3   1      16.0    14.0      14.0  ...      29.0      17.0     23.0     15.0
              15.0    15.0      11.0  ...      33.0      15.0     21.0     15.0
YAK4   1      12.0    18.0      14.0  ...      25.0      16.0     23.0     18.0
              16.0    15.0      11.0  ...      36.0      17.0     20.0     23.0
YAK5   1      11.0    14.0      14.0  ...      33.0      14.0     20.0     17.0
              15.0    14.0      16.0  ...      28.0      14.0     23.0     17.0
YAK6   1      15.0    16.0      13.0  ...      35.0      14.0     26.0     16.0
              15.0    16.0      13.0  ...      31.0      15.0     20.0     16.0
YAK7   1      15.0    15.0      14.0  ...      16.1      13.0     22.0     16.0
              11.0    14.0      11.0  ...      35.0      15.0     21.0     20.0
YAK8   1      15.0    14.0      14.0  ...      26.0      15.0     25.0     10.0
              15.0    15.0      14.0  ...      35.0      14.0     22.0     22.0
YAK9   1      12.0    14.0      10.0  ...      33.0      13.0     19.0     13.0
              12.0    18.0      11.0  ...      16.1      13.0     23.0     15.0
YAK10  1      11.0    16.0      14.0  ...      35.0      17.0     25.0     12.0
              11.0    18.0      14.0  ...      28.0      17.0     23.0     16.0

[20 rows x 26 columns]
 '''
def locus_beneath_locus(df):
    data_new = {}
    calc = 0
    old_list = []
    new_list = []
    data = df.to_dict(orient='list')
    number_list = []
    list_numbers_one = []
    for i in df.index:
        list_numbers_one.append('1')
        list_numbers_one.append('')
        number_list.append(i)
        number_list.append('')

    data_new['1'] = list_numbers_one

    for i in data:
        if i != '№':
            calc += 1
            if calc % 2 == 0:
                for j in range(len(data[i])):
                    new_list.append(old_list[j])
                    new_list.append(data[i][j])
                data_new[i.split('_')[0]] = new_list
                new_list = []
            old_list = data[i]
    df_new = pd.DataFrame(data_new, number_list)
    return (df_new)

'''
Функция принимает какой аллель ему нужно достать из словоря с частотами, и возвращает 2 массива обернутых в кортеж

Вход: 
1) D20S1082, 
2) {'D20S1082': {9.0: 0.005747, 10.0: 0.011494, 11.0: 0.442529, 12.0: 0.114943, 13.0: 0.014368,
14.0: 0.022989, 15.0: 0.270115, 16.0: 0.100575, 17.0: 0.008621, 18.0: 0.005747, 19.0: 0.002874},
'D6S474': {14.0: 0.317143, 15.0: 0.302857, 16.0: 0.145714, 17.0: 0.065714, 18.0: 0.168571} ...


Выход:
1) [9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0]
2) [0.005747, 0.011494, 0.442529, 0.114943, 0.014368, 0.022989, 0.270115, 0.100575, 0.008621, 0.005747, 0.002874]
'''
def converter_dict_to_list(allele, allele_frequency):
    list_allele_number = []
    list_allele_frequency = []
    for i in allele_frequency[allele]:
        list_allele_number.append(i)
        list_allele_frequency.append(allele_frequency[allele][i])
    return (list_allele_number, list_allele_frequency)

'''
Функция генерирует готовый датафрейм

Вход:
1) Частота алелей формата:
{'D20S1082': {9.0: 0.005747, 10.0: 0.011494, 11.0: 0.442529, 12.0: 0.114943, 13.0: 0.014368,
14.0: 0.022989, 15.0: 0.270115, 16.0: 0.100575, 17.0: 0.008621, 18.0: 0.005747, 19.0: 0.002874},
'D6S474': {14.0: 0.317143, 15.0: 0.302857, 16.0: 0.145714, 17.0: 0.065714, 18.0: 0.168571} ...

2) Наименонования индивидов формата:
{
    'YAK': 10
}

Выход: Дата фрейм формата:
 
       D20S1082_1  D20S1082_2  D6S474_1  ...  D7S1517_2  Penta E_1  Penta E_2
YAK1         16.0        16.0      17.0  ...       22.0       16.0       11.0
YAK2         11.0        15.0      17.0  ...       20.0       16.0       18.0
YAK3         18.0        11.0      15.0  ...       25.0       16.0       22.0
YAK4         11.0        11.0      15.0  ...       20.0       15.0        7.0
YAK5         16.0        11.0      18.0  ...       20.0       19.0       10.0
YAK6         15.0        12.0      16.0  ...       20.0       15.0        7.0
YAK7         11.0        15.0      14.0  ...       25.0       19.0       16.0
YAK8         11.0        11.0      18.0  ...       23.0        5.0       16.0
YAK9         11.0        11.0      15.0  ...       23.0       11.0       17.0
YAK10        16.0        11.0      14.0  ...       21.0       10.0       14.0
 
[10 rows x 50 columns]
'''
def generate_table(allele_frequency, name_of_individuals):
    data = {}
    table_colum_number = []

    # Генерируем согласно списку имен
    if len(name_of_individuals) > 0:
        for i in name_of_individuals:
            for j in range(1, name_of_individuals[i] + 1):
                table_colum_number.append(i + str(j))
    table_colum_number

    # Приступаем к генерации аллелей индивидов
    for allele in allele_frequency:
        for i in range(1, 3):
            duo_list_allele = converter_dict_to_list(allele, allele_frequency)
            data[str(allele) + '_' + str(i)] = random.choices(duo_list_allele[0], duo_list_allele[1], k=len(table_colum_number))
    df = pd.DataFrame(data, index=table_colum_number)
    return (df)