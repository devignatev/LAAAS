'''
Вход:
Массив матери, содержащий наименование локуса, значение частоты локуса 1, значение частоты локуса 1
Массив ребенка, содержащий наименование локуса, значение частоты локуса 1, значение частоты локуса 1
Словарь с значением частот

Выход:
Цифра, характеризующее расчитаную частоту
'''

def calc_q(mother, children, frequency):
    if mother[1] in children or mother[2] in children:
        if mother[1] == mother[2]:
            return (frequency[mother[0]][mother[1]]) * (2 - (frequency[mother[0]][mother[2]]))
        return ((frequency[mother[0]][mother[1]]) + (frequency[mother[0]][mother[2]])) * (2 - ((frequency[mother[0]][mother[1]]) + (frequency[mother[0]][mother[2]])))
    else:
        return 0

'''
Вход:
Словарь матери, структурированный подобным образом:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Словарь отца, структурированный подобным образом:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Выход:
Цифра, характеризующее расчитаную частоту
'''

def multiple_calculation(dict_mother, dict_children, frequency):
    sum = 1.0
    x = 0
    for locus in frequency:
        x+=1
        q = calc_q(
            [locus, dict_mother[locus + '_1'], dict_mother[locus + '_2']],
            [locus, dict_children[locus + '_1'], dict_children[locus + '_2']],
            frequency
        )
        if q == 0:
            return 0, 0
        else:
            #print('Итерация:', x, 'Умножаем', pp, 'Cумма:', sum)
            sum = sum * float(q)
    pi = 1/sum
    pp = 1/1+sum
    return pi, pp