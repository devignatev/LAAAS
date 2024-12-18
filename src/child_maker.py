import yaml
import pandas as pd
import random

def generation_of_alleles_for_the_child(allele_list):
    return (allele_list[random.randint(0, 1)], allele_list[random.randint(2, 3)])

def add_children(df, nums_children):
    dict_data = df.to_dict()
    calc_colum_index = 0
    calc_name = 0
    list_frequency = []
    new_dict = {}
    past_colum = {}

    for colum_index, colum in dict_data.items():
        calc_colum_index += 1

        if calc_colum_index % 2 == 0:
            new_colum_past = past_colum.copy()
            new_colum = colum.copy()
            past_name = None

            for name in list(past_colum.keys()):  # Создаем список ключей для безопасной итерации
                calc_name += 1

                if calc_name % 2 == 0:
                    list_frequency.extend([
                        past_colum[past_name],
                        colum.get(past_name, None),
                        past_colum[name],
                        colum.get(name, None)
                    ])

                    name_children = f"{past_name}+{name}"
                    allele_children = generation_of_alleles_for_the_child(list_frequency)

                    new_colum_past[name_children] = allele_children[0]
                    new_colum[name_children] = allele_children[1]

                    list_frequency = []
                past_name = name

            new_dict[colum_index_past] = new_colum_past
            new_dict[colum_index] = new_colum

        colum_index_past = colum_index
        past_colum = colum.copy()

    return pd.DataFrame(new_dict)