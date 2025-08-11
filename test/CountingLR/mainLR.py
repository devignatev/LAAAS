import src.сalculation as CALC
import pandas as pd
import src.external_function as ef
import src.creator_of_individuals as CoI

# Считаем частоты изходя из файла якуты.xlsx
def countigFR():
    df = pd.read_excel('/Users/mihailignatev/PycharmProjects/LAAAS/test/CountingLR/Files/якуты.xlsx', index_col=0, sheet_name='ЯКУТЫ')
    # Обновим датафрейму разметку
    # Было D20S1082  D20S1082.1
    # Стало D20S1082_1  D20S1082_2
    df = ef.uniqueness_locus(df)
    frequencies = CALC.counting_frequencies_from_file(df)
    return frequencies

#Создаем бабушек и дедушек
def create_1(frequencies, name_of_individuals):
    df = CoI.generate_table(allele_frequency=frequencies,
                            name_of_individuals=name_of_individuals)
    return df

#Создаем отцов и матерей
def create_2(df, nums_children):
    df_children = CoI.add_children(df, nums_children)
    return df_children

#Создаем детей от детей
def create_3(df, nums):
    df_cildren_from_children = CoI.add_children_from_children(df, nums)
    return df_cildren_from_children

def countingLR():
    frequencies = countigFR()

    # Сколько индивидов генерируем
    name_of_individuals = {
        'YAK': 100
    }

    # Запускаем генерацию 1 звена
    df = create_1(frequencies, name_of_individuals)
    print(df)

    # Запускаем генерацию 2 звена
    df = create_2(df, 4)
    print(df)

    # Запускаем генерацию 3 звена
    df = create_3(df, 4)
    print(df)

    print(frequencies)

    df.to_excel('/Users/mihailignatev/PycharmProjects/LAAAS/test/CountingLR/Files/Выход.xlsx')


if __name__ == '__main__':
    countingLR()