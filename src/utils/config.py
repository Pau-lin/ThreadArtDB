import yaml

def get_config():
    with open("src/utils/config.yaml",'r') as file:
        config = yaml.safe_load(file.read())
        return config
