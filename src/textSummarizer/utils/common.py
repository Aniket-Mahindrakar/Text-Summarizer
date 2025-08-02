import os
import box.exceptions as BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read a yaml file and returns
    
    Args:
        path_to_yaml (str): path to the yaml file
    
    Raises:
        ValueError: if the yaml file is empty
        e: empty yaml file
    
    Returns:
        ConfigBox: ConfigBox type object
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Yaml file: {path_to_yaml} is empty") from e
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories are to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file or directory in KB
    
    Args:
        path (Path): path to the file or directory
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / (1024))
    return f"~ {size_in_kb} KB"