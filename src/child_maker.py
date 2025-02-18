import yaml
import pandas as pd
import random

# Функция для генерации аллелей ребенка
# Выбираем один аллель от каждого из родителей случайным образом
def generation_of_alleles_for_the_child(allele_list):
    return (allele_list[random.randint(0, 1)], allele_list[random.randint(2, 3)])

# Функция для добавления потомков в таблицу
# df — исходный датафрейм с родительскими генами
# num_children — количество потомков, создаваемых для каждой пары родителей
def add_children(df, num_children=1):
    dict_data = df.to_dict()  # Преобразуем DataFrame в словарь для удобства обработки
    calc_colum_index = 0  # Счетчик колонок
    calc_name = 0  # Счетчик имен для пар родителей
    list_frequency = []  # Список для хранения аллелей пары родителей
    new_dict = {}  # Новый словарь для создания обновленного DataFrame
    past_colum = {}  # Хранит данные предыдущего столбца (родителя)

    # Проходим по колонкам исходного словаря
    for colum_index, colum in dict_data.items():
        calc_colum_index += 1

        # Обрабатываем только четные колонки (пары родителей)
        if calc_colum_index % 2 == 0:
            new_colum_past = {}  # Новый словарь для предыдущего родителя
            new_colum = {}  # Новый словарь для текущего родителя
            past_name = None  # Имя предыдущего родителя

            # Проходим по каждому индивиду в предыдущем столбце
            for name in list(past_colum.keys()):
                calc_name += 1
                new_colum_past[name] = past_colum[name]  # Сохраняем аллель родителя
                new_colum[name] = colum[name]  # Сохраняем аллель второго родителя

                # Когда находим пару родителей, создаем детей
                if calc_name % 2 == 0:
                    # Собираем аллели родителей
                    list_frequency.extend([
                        past_colum[past_name],  # Первый аллель первого родителя
                        colum.get(past_name, None),  # Второй аллель первого родителя
                        past_colum[name],  # Первый аллель второго родителя
                        colum.get(name, None)  # Второй аллель второго родителя
                    ])

                    # Генерируем нескольких детей
                    for i in range(1, num_children + 1):
                        name_children = f"{past_name}+{name}-{i}"  # Имя потомка (с индексом)
                        allele_children = generation_of_alleles_for_the_child(list_frequency)  # Аллели ребенка

                        # Записываем аллели детей в новые столбцы
                        new_colum_past[name_children] = allele_children[0]
                        new_colum[name_children] = allele_children[1]

                    list_frequency = []  # Очищаем список для следующей пары родителей
                past_name = name  # Запоминаем имя текущего родителя

            # Добавляем обновленные данные в новый словарь
            new_dict[colum_index_past] = new_colum_past
            new_dict[colum_index] = new_colum

        colum_index_past = colum_index  # Запоминаем текущий индекс
        past_colum = colum.copy()  # Копируем данные текущего столбца

    # Возвращаем обновленный DataFrame с потомками
    return pd.DataFrame(new_dict)