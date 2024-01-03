

import toml

def read_config():
    config = toml.load('config.toml')
    return config['parameters']
    

def get_parameter_list():
    parameters = read_config()
    return list(parameters.keys())
    
