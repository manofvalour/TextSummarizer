from src.TextSummarizer.logger.logger import logger
from src.TextSummarizer.exceptions.customexception import TextSummarizerException
from src.TextSummarizer.config.configurations import ConfigurationManager
from src.TextSummarizer.utils.common_utils import create_dir, read_yaml
from src.TextSummarizer.entity.config_entity import DataIngestionConfig
from src.TextSummarizer.components.DataIngestion import DataIngestion

import sys

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        ## running the code
        try:
            config= ConfigurationManager()
            ingestion_config= config.get_data_ingestion_config()
            logger.info(f"successfully initiated Data Ingestion Configuration")

            data_ingestion = DataIngestion(ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info(f"Data Ingestion Pipeline loaded successfully")
        
        except Exception as e:
            logger.error(f"Failed to Initiate Data Ingestion {e}")
            raise TextSummarizerException(e,sys)