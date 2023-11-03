import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_dirctories (list): A list of paths to directories.
        verbose (bool, optional): If True, will print the path to the directory. Defaults to True.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def read_yaml(path_to_yaml_file: Path) -> ConfigBox:
    """
    Reads a yaml file and returns.
    
    Args:
    
        path_to_yaml_file (Path): The path to the yaml file.
    Raises:
    
        BoxValueError: If the yaml file does not exist.
        e: empty file
    Returns:
        ConfigBox: ConfigBox object.
    """

    try:
        with open(path_to_yaml_file, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Read yaml file: {path_to_yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in kb
    
    Args:
    
        path (Path): The path to the file

    Returns:
        str: The size of the file in kb
    """

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"