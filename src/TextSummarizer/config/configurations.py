from src.TextSummarizer.constants import *
from src.TextSummarizer.utils.common_utils import read_yaml, create_dir
from src.TextSummarizer.exceptions.customexception import TextSummarizerException
from src.TextSummarizer.logger.logger import logger
from src.TextSummarizer.entity.config_entity import DataIngestionConfig

from pathlib import Path
import os, sys


## defining the configuration manager

class ConfigurationManager:
    def __init__(self, config_path:Path = CONFIG_FILE_PATH, params_path:Path = PARAMS_FILE_PATH):
        
        try:
            self.config = read_yaml(config_path)
            self.params = read_yaml(params_path)

            artifact_root = self.config.artifacts_root

            ## creating the artifact root directory
            create_dir([artifact_root])
            logger.info(f"successfully created the artifact root directory of path: {artifact_root}")

        except Exception as e:
            logger.error('Unable to initiate the Configuration Manager')
            raise TextSummarizerException(e, sys)
        
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        try:
            config= self.config.data_ingestion
            
            ##creating the data ingestion directories
            create_dir([config.root_dir])
            logger.info(f"successfully created the data ingestion directory with path: {config.root_dir}")

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_url = config.source_url,
                local_data_file=config.local_data_file,
                unzip_dir= config.unzip_dir
            )

            return data_ingestion_config

        except Exception as e:
            logger.error(f'Cannot get the data ingestion configuration {e}')
            raise TextSummarizerException(e,sys)

