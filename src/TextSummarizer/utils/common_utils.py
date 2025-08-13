import os, sys
import yaml
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from src.TextSummarizer.logger.logger import logger
from src.TextSummarizer.exceptions.customexception import TextSummarizerException
from box import ConfigBox
from pathlib import Path
from typing import Any, List


@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """ reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
        
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            file = yaml.safe_load(yaml_file)
            logger.info(f"logger file loaded successfully from: {path_to_yaml}")

            return ConfigBox(file)
        
    except BoxValueError:
        raise ValueError('yaml file is empty')
    
    except Exception as e:
        logger.error('yaml file is empty')
        raise TextSummarizerException(e, sys)
    

@ensure_annotations
def create_dir(dir_path:List, verbose=True):
    """ function to create list of directories
    
    Args:
        dir_path (List): list of path of directories to be created
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to True
        
    Return:
        None
    
    """
    try:
        
        for dir in dir_path:
            os.makedirs(dir, exist_ok=True)
            
            if verbose:
                logger.info(f"created directory at: {dir}")
    
    except Exception as e:
        logger.error(f'{e}')
        raise TextSummarizerException(e, sys)



