import yaml

get_price_intervals = 5 # in minutes

def load_config(path):
    with open(path) as fh:
        yaml_config = yaml.load(fh)
        return yaml_config
