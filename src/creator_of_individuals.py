import pandas as pd
import random

from src.сalculation import calc_q

'''
Функция создает словарь формата {Локус_1: (Значения аллелей), Локус_2: (Значения аллелей)} исходя из частот в популяции

Вход: 
1) {'D20S1082': {9.0: 0.005747, 10.0: 0.011494, 11.0: 0.442529, 12.0: 0.114943, 13.0: 0.014368, 14.0: 0.022989, 
    15.0: 0.270115, 16.0: 0.100575, 17.0: 0.008621, 18.0: 0.005747, 19.0: 0.002874}, , 'D6S474': {14.0: 0.317143, 
    15.0: 0.302857, ...
2) ['YAK1', 'YAK2', 'YAK3', 'YAK4', 'YAK5', 'YAK6', 'YAK7', 'YAK8', 'YAK9', 'YAK10']

Выход:
{'D20S1082_1': [15.0, 15.0, 11.0, 15.0, 15.0, 11.0, 12.0, 16.0, 15.0, 15.0], 'D20S1082_2': [11.0, 16.0, 15.0, 11.0...
'''

def random_allele(allele_frequency, table_colum_number):
    data = {}
    for allele in allele_frequency:
        for i in range(1, 3):
            duo_list_allele = converter_dict_to_list(allele, allele_frequency)
            data[str(allele) + '_' + str(i)] = random.choices(duo_list_allele[0], duo_list_allele[1],
                                                              k=len(table_colum_number))
    return data

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
    table_colum_number = []
    # Генерируем согласно списку имен
    if len(name_of_individuals) > 0:
        for i in name_of_individuals:
            for j in range(1, name_of_individuals[i] + 1):
                table_colum_number.append(i + str(j))

    # Приступаем к генерации аллелей индивидов
    data = random_allele(allele_frequency, table_colum_number)
    df = pd.DataFrame(data, index=table_colum_number)
    return (df)

# Функция для генерации аллелей ребенка
# Выбираем один аллель от каждого из родителей случайным образом
def generation_of_alleles_for_the_child(allele_list):
    return (allele_list[random.randint(0, 1)], allele_list[random.randint(2, 3)])

'''
Функция добовления детей в таблицу

Вход:
Функция для добавления потомков в таблицу
1) df — исходный датафрейм с родительскими генами:

        D20S1082_1  D20S1082_2  D6S474_1  ...  D7S1517_2  Penta E_1  Penta E_2
YAK1          11.0        11.0      15.0  ...       18.0       17.0       14.0
YAK2          11.0        11.0      18.0  ...       20.0       10.0       22.0
YAK3          11.0        11.0      14.0  ...       22.0       16.0       17.0
YAK4          11.0        11.0      15.0  ...       25.0       14.0       13.0
YAK5          15.0        16.0      17.0  ...       20.0       12.0       23.0
...            ...         ...       ...  ...        ...        ...        ...
YAK96         12.0        16.0      15.0  ...       20.0       20.0        5.0
YAK97         11.0        15.0      15.0  ...       24.0       16.0       18.0
YAK98         14.0        11.0      15.0  ...       23.0       18.0       12.0
YAK99         11.0        15.0      17.0  ...       20.0       18.0       21.0
YAK100        15.0        11.0      15.0  ...       22.0       18.0       20.0

[100 rows x 50 columns]

2) num_children — количество потомков, создаваемых для каждой пары родителей:
2

Выход: Дата фрейм c детьми:

                D20S1082_1  D20S1082_2  ...  Penta E_1  Penta E_2
YAK1                  11.0        11.0  ...       17.0       14.0
YAK2                  11.0        11.0  ...       10.0       22.0
YAK1+YAK2-1           11.0        11.0  ...       14.0       22.0
YAK1+YAK2-2           11.0        11.0  ...       17.0       22.0
YAK3                  11.0        11.0  ...       16.0       17.0
...                    ...         ...  ...        ...        ...
YAK97+YAK98-2         11.0        14.0  ...       16.0       12.0
YAK99                 11.0        15.0  ...       18.0       21.0
YAK100                15.0        11.0  ...       18.0       20.0
YAK99+YAK100-1        11.0        15.0  ...       18.0       18.0
YAK99+YAK100-2        15.0        11.0  ...       21.0       20.0

[200 rows x 50 columns]
'''
def add_children(df, num_children=1):
    dict_data = df.to_dict()  # Преобразуем DataFrame в словарь для удобства обработки
    calc_colum_index = 0  # Счетчик колонок
    calc_name = 0  # Счетчик имен для пар родителей
    list_allel = []  # Список для хранения аллелей пары родителей
    new_dict = {}  # Новый словарь для создания обновленного DataFrame
    past_colum = {}  # Хранит данные предыдущего столбца (родителя)

    # Проходим по колонкам исходного словаря
    for colum_index, colum in dict_data.items():
        calc_colum_index += 1

        # Обрабатываем только четные колонки (пары родителей)
        if calc_colum_index % 2 == 0:
            new_colum_past = {}  # Новый словарь для предыдущего родителя
            new_colum = {}  # Новый словарь для текущего родителя
            past_name = None  # Имя предыдущего родителя

            # Проходим по каждому индивиду в предыдущем столбце
            for name in list(past_colum.keys()):
                calc_name += 1
                new_colum_past[name] = past_colum[name]  # Сохраняем аллель родителя
                new_colum[name] = colum[name]  # Сохраняем аллель второго родителя

                # Когда находим пару родителей, создаем детей
                if calc_name % 2 == 0:
                    # Собираем аллели родителей
                    list_allel.extend([
                        past_colum[past_name],  # Первый аллель первого родителя
                        colum.get(past_name, None),  # Второй аллель первого родителя
                        past_colum[name],  # Первый аллель второго родителя
                        colum.get(name, None)  # Второй аллель второго родителя
                    ])

                    # Генерируем нескольких детей
                    for i in range(1, num_children + 1):
                        name_children = f"{past_name}+{name}-{i}"  # Имя потомка (с индексом)
                        allele_children = generation_of_alleles_for_the_child(list_allel)  # Аллели ребенка

                        # Записываем аллели детей в новые столбцы
                        new_colum_past[name_children] = allele_children[0]
                        new_colum[name_children] = allele_children[1]

                    list_allel = []  # Очищаем список для следующей пары родителей
                past_name = name  # Запоминаем имя текущего родителя

            # Добавляем обновленные данные в новый словарь
            new_dict[colum_index_past] = new_colum_past
            new_dict[colum_index] = new_colum

        colum_index_past = colum_index  # Запоминаем текущий индекс
        past_colum = colum.copy()  # Копируем данные текущего столбца

    # Возвращаем обновленный DataFrame с потомками
    return pd.DataFrame(new_dict)

'''
Функция проверяет наличие инцеста

Вход:
1) YAK3+YAK4-1
2) YAK3+YAK4-2

Выход:
True
'''
def protection_against_incest(ind_1, ind_2):
    list_ind_1 = ind_1.split('-')[0].split('+')
    list_ind_2 = ind_2.split('-')[0].split('+')
    for name_father in list_ind_1:
        if name_father == list_ind_2[0] or name_father == list_ind_2[1]:
            return True
    return False

'''
Функция проверяет наличие инцеста

Вход:


Выход:
1) Локусы матери с значениями аллелей в формате: 
    {'D20S1082_1': 11.0, 'D20S1082_2': 16.0, 'D6S474_1': 14.0, 'D6S474_2': 15.0, 'D14S1434_1': 11.0, 'D14S1434_2': 14.0,
    'D4S2666_1': 11.0, 'D4S2666_2': 9.0, 'D1S1677_1': 14.0, 'D1S1677_2': 14.0, 'D11S4463_1': 14.0, 'D11S4463_2': 16.0,
    'D4S2364_1': 8.0, 'D4S2364_2': 7.0, 'D9S1122_1': 12.0, 'D9S1122_2': 13.0, 'D2S1776_1': 12.0, 'D2S1776_2': 10.0,
    'D17S974_1': 9.0, 'D17S974_2': 9.0, 'D10S1435_1': 13.0, 'D10S1435_2': 13.0, 'D3S3053_1': 9.0, 'D3S3053_2': 12.0,
    'D5S2500_1': 15.0, 'D5S2500_2': 18.0, 'D1S1627_1': 14.0, 'D1S1627_2': 14.0, 'D3S4529_1': 16.0, 'D3S4529_2': 16.0,
    'D2S1360_1': 23.0, 'D2S1360_2': 22.0, 'D3S1744_1': 18.0, 'D3S1744_2': 17.0, 'D9S2157_1': 14.0, 'D9S2157_2': 13.0,
    'D17S1301_1': 13.0, 'D17S1301_2': 10.0, 'D8S1132_1': 19.0, 'D8S1132_2': 24.0, 'Penta D_1': 8.0, 'Penta D_2': 9.0,
    'D21S2050_1': 19.1, 'D21S2050_2': 32.0, 'D10S2325_1': 12, 'D10S2325_2': 19, 'D7S1517_1': 23.0,
    'D7S1517_2': 20.0, 'Penta E_1': 18.0, 'Penta E_2': 15.0}

2)  Локусы отца в формате:
    {'D20S1082_1': 15.0, 'D20S1082_2': 16.0, 'D6S474_1': 15.0, 'D6S474_2': 16.0, 'D14S1434_1': 10.0, ...
'''
def create_children(mather, father):
    children = {}
    list_allel_m = []
    list_allel_f = []
    calc = 0
    for locus in mather:
        calc += 1
        list_allel_m.append(mather[locus])
        list_allel_f.append(father[locus])
        if locus.split('_')[1] == '1':
            old_locus = locus

        if calc == 2:
            list_allel = [
                list_allel_m[0],
                list_allel_m[1],
                list_allel_f[0],
                list_allel_f[1]
            ]

            child_allel_old, child_allel = generation_of_alleles_for_the_child(list_allel)

            children[old_locus] = child_allel_old
            children[locus] = child_allel

            list_allel_m = []
            list_allel_f = []
            calc = 0
    return children

'''
Функция добовления детей от детей в таблицу

Вход:
Функция для добавления потомков в таблицу
1) df — исходный датафрейм с родительскими генами:

        D20S1082_1  D20S1082_2  D6S474_1  ...  D7S1517_2  Penta E_1  Penta E_2
YAK1          11.0        11.0      15.0  ...       18.0       17.0       14.0
YAK2          11.0        11.0      18.0  ...       20.0       10.0       22.0
YAK3          11.0        11.0      14.0  ...       22.0       16.0       17.0
YAK4          11.0        11.0      15.0  ...       25.0       14.0       13.0
YAK5          15.0        16.0      17.0  ...       20.0       12.0       23.0
...            ...         ...       ...  ...        ...        ...        ...
YAK96         12.0        16.0      15.0  ...       20.0       20.0        5.0
YAK97         11.0        15.0      15.0  ...       24.0       16.0       18.0
YAK98         14.0        11.0      15.0  ...       23.0       18.0       12.0
YAK99         11.0        15.0      17.0  ...       20.0       18.0       21.0
YAK100        15.0        11.0      15.0  ...       22.0       18.0       20.0

[100 rows x 50 columns]

2) num_children — количество потомков, создаваемых для каждой пары родителей:
2

Выход: Дата фрейм c детьми:

                D20S1082_1  D20S1082_2  ...  Penta E_1  Penta E_2
YAK1                  11.0        11.0  ...       17.0       14.0
YAK2                  11.0        11.0  ...       10.0       22.0
YAK1+YAK2-1           11.0        11.0  ...       14.0       22.0
YAK1+YAK2-2           11.0        11.0  ...       17.0       22.0
YAK3                  11.0        11.0  ...       16.0       17.0
...                    ...         ...  ...        ...        ...
YAK97+YAK98-2         11.0        14.0  ...       16.0       12.0
YAK99                 11.0        15.0  ...       18.0       21.0
YAK100                15.0        11.0  ...       18.0       20.0
YAK99+YAK100-1        11.0        15.0  ...       18.0       18.0
YAK99+YAK100-2        15.0        11.0  ...       21.0       20.0

[200 rows x 50 columns]
'''
def add_children_from_children(df, num_children=1):
    new_dict = {}
    dict_data = df.to_dict('index')  # Преобразуем DataFrame в словарь для удобства обработки

    list_progenitors = []

    for individ in dict_data:
        if '+' in individ:
            list_progenitors.append(individ)

    global_calc = 0
    calc = 0
    for individ in dict_data:

        # Условие на отбор особей для продолжения рода
        if '+' in individ:
            calc += 1

            # Обнуление счетчика
            if calc == 4:
                calc = 0

            # Условия при которых мы генерируем индивидов
            if calc == 1 or calc == 2:
                global_calc += 1
                if list_progenitors.index(individ) + 3 > len(list_progenitors):
                    name_father = list_progenitors[list_progenitors.index(individ) + 2 - len(individ)]
                else:
                    name_father = list_progenitors[list_progenitors.index(individ) + 2]

                new_dict[individ] = dict_data[individ]
                new_dict[name_father] = dict_data[name_father]

                for i in range(1, num_children):

                    children = create_children(dict_data[individ], dict_data[name_father])
                    #print('Children', global_calc)
                    #print('Mather', individ,  dict_data[individ])
                    #print('Father', name_father, dict_data[name_father])
                    #print('Children', children)

                    name_children = f"{individ}+{name_father}/{i}"
                    new_dict[name_children] = children

        # Условие на перенос бабушек и дедушек в новый список
        else:
            new_dict[individ] = dict_data[individ]

    final_dict = {}
    for i in new_dict:
        final_dict[i] = new_dict[i]

    return pd.DataFrame(final_dict).transpose()