from operator import index
import pandas
import pandas as pd
import src.external_function as EF
import src.creator_of_individuals as CoI
import src.creator_of_individuals as GPI
import src.find_father as FindFather
import src.countingLR as LR
import yaml
import os

def main():
    config_path = os.path.join(os.path.dirname(__file__), 'config_file.yaml')
    with open(config_path, 'r') as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    # создаем 1 поколение (бабушек и дедушек)
    # creator_of_individuals
    allele_frequency = (config['allele_frequency'])
    name_of_individuals = {
        'YAK': 10
    }
    df = CoI.generate_table(allele_frequency=allele_frequency,
                        name_of_individuals=name_of_individuals)
    CoI.locus_beneath_locus(df).to_excel(config['output_file_path_creator_of_individuals_join'])
    df.to_excel(config['output_file_path_creator_of_individuals'])
    print(df)

    # создаем 2 поколение (матерей и отцов)
    # parents_maker
    df_parents = CoI.add_parents(df, config['parents_maker_nums'])
    df_parents.to_excel(config['output_file_path_parents_maker'])
    print(df_parents)

    # создаем 3 поколение (сестер и братьев)
    ##df_children = CoI.add_children(df_parents, config['children_maker_nums'])

    # сортируем по потомкам
    ##df_children = EF.individuals_sorted(df_children, config['children_maker_nums'])

    ##df_children.to_excel(config['output_file_path_children_maker'])

    lr_siblings_df = LR.siblings_countingLR(df_parents, config['allele_frequency'], config['parents_maker_nums'],
                                     config['children_maker_nums'])

    print(lr_siblings_df)
    #lr_siblings_df.to_excel(config['output_file_path_lr_siblings_xlsx'], index=False)
    lr_siblings_df.to_csv(config['output_file_path_lr_siblings_csv'])
    # generate_pi
    #df_gpi = GPI.generate_table(df_children, allele_frequency)

    # Поиск ложно-положительных отцов
    #df_find_father = FindFather.find_father(df_parents, allele_frequency)
    #df_find_father.to_excel(config['output_file_path_find_father'], index=0)



if __name__ == '__main__':
    main()