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
    dict_allel = CALC.counting_allel_from_file(df_1_2)
    ef.frequencies_in_exel(dict_allel, 'allel_A28.xlsx')
    frequencies = CALC.counting_frequencies(dict_allel)

    for i in frequencies:
        print(i, sum(frequencies[i].values()))

    print(frequencies)

    ef.frequencies_in_exel(frequencies, 'FR_ASTR_A28_AVAR_189.xlsx')



if __name__ == '__main__':
    path_config = './config_file.yaml'
    with open(path_config, 'r') as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    df = pd.read_excel(config['normalization_input_file'], index_col=0)
    normalizated(df)