from src.TextSummarizer.exceptions.customexception import TextSummarizerException
from src.TextSummarizer.logger.logger import logger
from src.TextSummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
import os, sys


STAGE_NAME = 'Data Ingestion stage'

if __name__== "__main__":
    try:
        logger.info(f"{STAGE_NAME} initiated")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f"{STAGE_NAME} completed")

    except Exception as e:
        raise TextSummarizerException(e,sys)