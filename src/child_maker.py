import yaml

def main():
    path_config = './config_file.yaml'
    with open(path_config, 'r') as yaml_file:
        config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    allele_frequency = (config['allele_frequency'])



if __name__ == '__main__':
    main()