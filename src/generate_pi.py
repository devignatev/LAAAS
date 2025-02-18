import pandas as pd
import src.сalculation as CALC

'''
data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
pd.DataFrame.from_dict(data, orient='index')
       0  1  2  3
row_1  3  2  1  0
row_2  a  b  c  d
'''

def generate_table(df, frequency):
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
                    pi, pp = CALC.multiple_calculation(row.to_dict(), row_parents.to_dict(), frequency)
                    if pi >= 400 or pp >= 0.9975:
                        if index.split('+')[0] != index_parents and index.split('+')[1].split('-')[0] != index_parents:
                            calc += 1
                            print(calc, index, index_parents)