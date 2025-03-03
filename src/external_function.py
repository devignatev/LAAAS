import pandas as pd

'''
Функция которая выдирает из частот все аллели которые в них содержатся

Вход:
Частота:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Выход:
Список частот:
[5.0, 7.0, 8, 9.0, 10, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 16.1, 17.0, 17.1, 18.0, 19.0, 19.1, 20.0, 21.0, 22.0, 23.0]
'''

def dict_allels_in_frequencies(frequencies):
    dict_allels = []
    for locus in frequencies:
        for allels in frequencies[locus]:
            if allels not in dict_allels:
                dict_allels.append(allels)
    return sorted(dict_allels, key=float)

'''
Функция которая переводит словарь частот в вид понятный пердставителям Homo sapiens sapiens

Вход:
Частота:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Выход:
Что-то такое, только в exel:
      D20S1082    D6S474  D14S1434  ...  D10S2325   D7S1517   Penta E
5.0        NaN       NaN       NaN  ...       NaN       NaN  0.036810
7.0        NaN       NaN       NaN  ...       NaN       NaN       NaN
8          NaN       NaN       NaN  ...       NaN       NaN       NaN
9.0   0.006803       NaN  0.025974  ...  0.041322       NaN  0.012270
10         NaN       NaN  0.084416  ...       NaN       NaN  0.073620
11.0  0.462585       NaN  0.253247  ...       NaN       NaN  0.141104
12.0  0.149660       NaN  0.025974  ...  0.041322       NaN  0.067485
13.0  0.020408       NaN  0.181818  ...  0.157025       NaN  0.061350
14.0  0.040816  0.328859  0.383117  ...  0.231405       NaN  0.042945
15.0  0.265306  0.201342       NaN  ...  0.198347       NaN  0.079755
16.0  0.054422  0.174497  0.045455  ...  0.090909       NaN  0.153374
16.1       NaN       NaN       NaN  ...       NaN       NaN       NaN
17.0       NaN  0.080537       NaN  ...  0.074380       NaN  0.092025
17.1       NaN       NaN       NaN  ...       NaN       NaN       NaN
18.0       NaN  0.214765       NaN  ...  0.074380  0.018293  0.073620
19.0       NaN       NaN       NaN  ...  0.057851  0.073171  0.049080
19.1       NaN       NaN       NaN  ...       NaN       NaN       NaN
20.0       NaN       NaN       NaN  ...       NaN  0.201220  0.042945
21.0       NaN       NaN       NaN  ...       NaN  0.079268  0.030675
22.0       NaN       NaN       NaN  ...       NaN  0.134146  0.018405
23.0       NaN       NaN       NaN  ...       NaN  0.164634  0.024540
23.3       NaN       NaN       NaN  ...  0.033058       NaN       NaN
24.0       NaN       NaN       NaN  ...       NaN  0.097561       NaN
25.0       NaN       NaN       NaN  ...       NaN  0.207317       NaN
26.0       NaN       NaN       NaN  ...       NaN  0.018293       NaN
27.0       NaN       NaN       NaN  ...       NaN  0.006098       NaN
28.0       NaN       NaN       NaN  ...       NaN       NaN       NaN
29         NaN       NaN       NaN  ...       NaN       NaN       NaN
30.0       NaN       NaN       NaN  ...       NaN       NaN       NaN
31.0       NaN       NaN       NaN  ...       NaN       NaN       NaN
32.0       NaN       NaN       NaN  ...       NaN       NaN       NaN
33         NaN       NaN       NaN  ...       NaN       NaN       NaN
34         NaN       NaN       NaN  ...       NaN       NaN       NaN
35         NaN       NaN       NaN  ...       NaN       NaN       NaN
36         NaN       NaN       NaN  ...       NaN       NaN       NaN
38         NaN       NaN       NaN  ...       NaN       NaN       NaN
'''

def frequencies_in_exel(frequencies, path_save):
    dict_allels = dict_allels_in_frequencies(frequencies)
    print(dict_allels)
    df = pd.DataFrame(frequencies, index=dict_allels)
    print(df)
    df.to_excel(path_save)