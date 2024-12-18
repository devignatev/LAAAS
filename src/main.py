import src.creator_of_individuals as CoI
import src.child_maker as CM
import yaml


def main():
    path_config = './config_file.yaml'
    with open(path_config, 'r') as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)

    # creator_of_individuals
    allele_frequency = (config['allele_frequency'])
    name_of_individuals = {
        'YAK': 100
    }
    df = CoI.generate_table(allele_frequency=allele_frequency,
                        name_of_individuals=name_of_individuals)
    CoI.locus_beneath_locus(df).to_excel(config['output_file_path_creator_of_individuals_join'])
    df.to_excel(config['output_file_path_creator_of_individuals'])


    # child_maker
    df_children = CM.add_children(df, 5)
    df_children.to_excel(config['output_file_path_child_maker'])

if __name__ == '__main__':
    main()