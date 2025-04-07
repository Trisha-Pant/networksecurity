import yaml
from NetworkSecurity.exception import NetworkSecurityException
from NetworkSecurity.logging import logger
import os,sys
import numpy as np
import dill
import pickle

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path) as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def write_yaml_file(file_path:str, data:dict, replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(data,file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    