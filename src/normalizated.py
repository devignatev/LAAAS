import pandas as pd
import src.сalculation as CALC
import src.external_function as EF
import yaml
import src.external_function as ef

'''
Модуль нормализации файла.
Основаня идея: в модуль поступает файл который содержит в аллелях значения по типу '0', 'OL' и прочие подобные. Функция
сканирует весь файл, считает потенциальные частоты, и на основании этих частот заполняет пробелы.
'''

def normalizated(df):

    # Обновим датафрейму разметку
    # Было D20S1082  D20S1082.1
    # Стало D20S1082_1  D20S1082_2
    df_1_2 = ef.uniqueness_locus(df)

    # Считаем частоты
    frequencies = CALC.counting_frequencies_from_file(df_1_2)

    sum = 0
    for i in frequencies:
        for j in frequencies[i]:
            sum += frequencies[i][j]
        print(i, sum)
        sum = 0

    print(frequencies)



if __name__ == '__main__':
    path_config = './config_file.yaml'
    with open(path_config, 'r') as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    df = pd.read_excel(config['normalization_input_file'], index_col=0, sheet_name='ЯКУТЫ')
    normalizated(df)