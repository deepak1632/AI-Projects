### Utils: Means, let's say you are using some python function frequently in your code, let's say you have created one function called redml, so this function is responsible for reading your redml file. 
### utils" typically refers to a module or collection of functions and classes that provide general-purpose utility functionalities. These utilities are designed to be reusable across different parts of an application and often handle common, low-level tasks that are not specific to the core business logic.

import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args: 
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
        ConfigBox: Configbox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
       path (Path): path of the file

    Returns:
       str: size in KB
       """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
 