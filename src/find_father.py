import pandas as pd
import src.сalculation as CALC

'''
Функция которая исчет ложно-положительных отцов

Вход:
Словарь матери, структурированный подобным образом:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Словарь отца, структурированный подобным образом:
{'D20S1082_1': 15.0, 'D20S1082_2': 11.0, 'D6S474_1': 14.0, 'D6S474_2': 16.0, 'D14S1434_1': 14.0, 'D14S1434_2': 14.0}

Выход:
Цифра, характеризующее расчитаную частоту
'''

def find_father(df, frequency):
    calc = 0
    new_df = pd.DataFrame({'№': [], 'Sex': [], 'Child_ID': [], 'Status': []})
    for index, row in df.iterrows():

        # Отбор детей
        if len(index.split('+')) == 2:

            #Перебор родителей
            for index_parents, row_parents in df.iterrows():
                # Отбор родителей
                if len(index_parents.split('+')) == 1:

                    # Проверка на совпадение коэфицентов
                    pi, pp = CALC.calculation_pi_and_pp(row.to_dict(), row_parents.to_dict(), frequency)
                    if pi >= 400 or pp >= 0.9975:
                        if index.split('+')[0] != index_parents and index.split('+')[1].split('-')[0] != index_parents:
                            calc += 1
                            #print(calc, index, index_parents)