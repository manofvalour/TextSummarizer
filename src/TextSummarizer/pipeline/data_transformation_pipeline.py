from src.TextSummarizer.logger.logger import logger
from src.TextSummarizer.exceptions.customexception import TextSummarizerException
from src.TextSummarizer.config.configurations import ConfigurationManager
from src.TextSummarizer.utils.common_utils import create_dir, read_yaml
from src.TextSummarizer.entity.config_entity import DataTransformationConfig
from src.TextSummarizer.components.DataTransformation import DataTransformation

import sys

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        ## running the code
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transforamtion_config()
            logger.info(f"successfully initiated Data Transformation Configuration")

            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.convert()
            logger.info(f"Data Transformation Pipeline loaded successfully")
        
        except Exception as e:
            logger.error(f"Failed to Initiate Data Transformation {e}")
            raise TextSummarizerException(e,sys)