import pandas as pd
import src.сalculation as CALC
import yaml

'''
Модуль нормализации файла.
Основаня идея: в модуль поступает файл который содержит в аллелях значения по типу '0', 'OL' и прочие подобные. Функция
сканирует весь файл, считает потенциальные частоты, и на основании этих частот заполняет пробелы.
'''

def normalizated(df):
    frequencies = CALC.counting_frequencies_from_file(df)
    print(df)

if __name__ == '__main__':
    path_config = './config_file.yaml'
    with open(path_config, 'r') as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    df = pd.read_excel(config['normalization_input_file'], index_col=0, )
    normalizated(df)