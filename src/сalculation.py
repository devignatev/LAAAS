from pandas.core.methods.to_dict import to_dict

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
Словарь частот, к примеру какой-то такой:
{'D20S1082': {11.0: 0.46258503401360546, 15.0: 0.2653061224489796, 12.0: 0.14965986394557823, 16.0: 0.05442176870748299,
14.0: 0.04081632653061224, 13.0: 0.02040816326530612, 9.0: 0.006802721088435374}, 'D6S474': {15: 0.20134228187919462,
14: 0.3288590604026846, 18.0: 0.21476510067114093, 17.0: 0.08053691275167785, 16.0: 0.174496644295302}, ... }
'''

def counting_frequencies_from_file(df):
    print(df)
    frequencies = {}
    allel = [el.split('_')[0] for el in df.columns.to_list() if int(el.split('_')[1]) % 2 != 0]
    for el in allel:
        frequencies[el] = {}
    df_dict = df.to_dict('index')
    for individual in df_dict:
        for locus in df_dict[individual]:
            print(individual, locus)
            print(df_dict[individual][locus])
            if str(df_dict[individual][locus]) != 'nan' and str(df_dict[individual][locus]) != 'OL':
                if df_dict[individual][locus] in frequencies[locus.split('_')[0]]:
                    calc = frequencies[locus.split('_')[0]][df_dict[individual][locus]]
                    calc += 1
                    frequencies[locus.split('_')[0]][df_dict[individual][locus]] = calc
                else:
                    frequencies[locus.split('_')[0]][df_dict[individual][locus]] = 1

    for locus in frequencies:
        summ = 0
        for calc in frequencies[locus]:
            summ += frequencies[locus][calc]
        for calc in frequencies[locus]:
            frequencies[locus][calc] = frequencies[locus][calc]/summ
    return frequencies
