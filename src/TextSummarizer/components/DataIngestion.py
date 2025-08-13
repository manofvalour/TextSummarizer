import urllib.request as request
import zipfile
import os, sys

from src.TextSummarizer.logger.logger import logger
from src.TextSummarizer.exceptions.customexception import TextSummarizerException
from src.TextSummarizer.config.configurations import ConfigurationManager
from src.TextSummarizer.utils.common_utils import create_dir, read_yaml
from src.TextSummarizer.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config=config

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, header = request.urlretrieve(
                    url= self.config.source_url,
                    filename= self.config.local_data_file
                )
                logger.info(f"File has been downloaded to: {self.config.local_data_file}")
            else:
                logger.info('File already exists')

        except Exception as e:
            logger.error(f'Error downloading file {e}')
            raise TextSummarizerException(e,sys)

    def extract_zip_file(self):
        """ Extracts the zip file into the data directory

        zip_file_path: str
        
        
        returns: None
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            logger.info(f'unzip directory created successfully with path: {unzip_path}')

            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"file successfully extracted to {unzip_path}")

        except Exception as e:
            logger.error(f"Error unzipping the file {e}")
            raise TextSummarizerException(e,sys)

        