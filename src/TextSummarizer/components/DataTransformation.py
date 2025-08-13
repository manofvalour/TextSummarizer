import pandas as pd
from transformers import AutoTokenizer
from datasets import load_from_disk

from src.TextSummarizer.constants import *
from src.TextSummarizer.utils.common_utils import read_yaml, create_dir
from src.TextSummarizer.exceptions.customexception import TextSummarizerException
from src.TextSummarizer.logger.logger import logger
from src.TextSummarizer.config.configurations import ConfigurationManager
from src.TextSummarizer.entity.config_entity import DataTransformationConfig
from pathlib import Path
import os, sys


class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config= config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name) ## initializing the Tokenizer

    def convert_examples_to_features(self,example_batch):
        try:
            input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True ) ## Tokenizing the input data

            with self.tokenizer.as_target_tokenizer():
                target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

            return {
                'input_ids' : input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']}
        
        except Exception as e:
            logger.error("failed to tokenize the dataset")
            raise TextSummarizerException(e,sys)

    def convert(self):
        try:
            dataset_samsum = load_from_disk(self.config.data_path)
            dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
            dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))

        except Exception as e:
            logger.error('failed to load dataset')
            raise TextSummarizerException(e,sys)