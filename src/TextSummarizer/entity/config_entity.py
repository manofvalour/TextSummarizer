from dataclasses import dataclass
from pathlib import Path


#################### DATA INGESTION CONFIGURATION ENTITY #####################
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir: Path

#################### DATA TRANSFORMATION CONFIGURATION ENTITY #####################
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str