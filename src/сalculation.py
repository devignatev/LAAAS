from pandas.core.methods.to_dict import to_dict
from decimal import Decimal, getcontext

from test import dict_l

'''
Функция которая расчитывает значение q, которое например нужно для расчета pp, pi

Вход:
Массив матери, содержащий наименование локуса, значение частоты локуса 1, значение частоты локуса 1
Массив ребенка, содержащий наименование локуса, значение частоты локуса 1, значение частоты локуса 1
Словарь с значением частот

Выход:
Цифра, характеризующее расчитаную частоту

Пример:
Вход: ('D11S4463', 13.0, 15.0) ('D11S4463', 13.0, 15.0) {'D20S1082': {9.0: 0.005747, 10.0: 0.011494, 11.0: 0.442529,
12.0: 0.114943, 13.0: 0.014368, 14.0: 0.022989, 15.0: 0.270115, 16.0: 0.100575, 17.0: 0.008621, 18.0:
0.005747, 19.0: 0.002874}, ...
Выход: 0.768066255975
'''

def calc_q(mother, children, frequency):
    if mother[1] in children or mother[2] in children:
        if mother[1] == mother[2]:
            return (frequency[mother[0]][mother[1]]) * (2 - (frequency[mother[0]][mother[2]]))
        return (((frequency[mother[0]][mother[1]]) + (frequency[mother[0]][mother[2]])) *
                (2 - ((frequency[mother[0]][mother[1]]) + (frequency[mother[0]][mother[2]]))))
    else:
        return 0

'''
Функция которая расчитывает значения pp, pi

Вход:
Словарь матери, структурированный подобным образом:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Словарь отца, структурированный подобным образом:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Выход:
pp, pi
'''

def calculation_pi_and_pp(dict_mother, dict_children, frequency):
    sum = 1.0
    x = 0
    for locus in frequency:
        x+=1
        q = calc_q(
            (locus, dict_mother[locus + '_1'], dict_mother[locus + '_2']),
            (locus, dict_children[locus + '_1'], dict_children[locus + '_2']),
            frequency
        )
        if q == 0:
            return 0, 0
        else:
            sum = sum * float(q)
    pi = 1/sum
    pp = 1/1+sum
    return pi, pp

'''
Функция подсчета частот в файле

Вход:
Дата фрейм (pandas)

Выход:
Словарь повторений, к примеру какой-то такой:
{'D20S1082': {11: 164, 13: 9, 15: 113, 12: 26, 14: 42, 16: 22, 9: 2}, 
'D6S474': {15: 82, 17: 82, 14: 100, 16: 72, 13: 13, 18: 27, 0: 2}, 
'D12ATA63': {12: 80, 13: 65, 15: 45, 18: 19, 16: 6, 17: 135, 19: 7, 14: 21}}
'''

def counting_allel_from_file(df):
    frequencies = {}
    locus_list = [el.split('_')[0] for el in df.columns.to_list() if int(el.split('_')[1]) % 2 != 0]

    for el in locus_list:
        frequencies[el] = {}
    df_dict = df.to_dict('index')
    for individual in df_dict:
        for locus in df_dict[individual]:
            allel = df_dict[individual][locus]
            if ',' in str(allel):
                allel = allel.replace(',', '.')
            if str(allel) != 'nan' and str(allel) != 'OL' and str(allel) != '0' and allel != 0:
                if allel in frequencies[locus.split('_')[0]]:
                    calc = frequencies[locus.split('_')[0]][allel]
                    calc += 1
                    frequencies[locus.split('_')[0]][allel] = calc
                else:
                    frequencies[locus.split('_')[0]][allel] = 1
    return frequencies

'''
Вся математика тут!
Вход: 
{'D20S1082': {11: 164, 13: 9, 15: 113, 12: 26, 14: 42, 16: 22, 9: 2}, 
'D6S474': {15: 82, 17: 82, 14: 100, 16: 72, 13: 13, 18: 27, 0: 2}, 
'D12ATA63': {12: 80, 13: 65, 15: 45, 18: 19, 16: 6, 17: 135, 19: 7, 14: 21}}
'''
def counting_frequencies(frequencies):
    for locus in frequencies:
        summ = 0
        for calc in frequencies[locus]:
            summ += frequencies[locus][calc]
        for calc in frequencies[locus]:
            frequencies[locus][calc] = frequencies[locus][calc] / summ

        total = sum(frequencies[locus].values())
        for calc in frequencies[locus]:
            frequencies[locus][calc] = frequencies[locus][calc] / total

    return frequencies