import os
import logging
from pathlib import Path

logging.basicConfig(level= logging.INFO, format = "[%(asctime)s]: %(levelname)s: %(message)s")

project_name = 'TextSummarizer'

list_of_dir = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/components/init.py',
    f'src/{project_name}/utils/common_utils.py',
    f'src/{project_name}/utils/init.py',
    f'src/{project_name}/logger/init.py',
    f'src/{project_name}/logger/logger.py',
    f'src/{project_name}/exceptions/init.py',
    f'src/{project_name}/exceptions/customexception.py',
    f'src/{project_name}/config/init.py',
    f'src/{project_name}/config/configurations.py',
    f'src/{project_name}/entity/init.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/entity/artifacts_entity.py',
    f'src/{project_name}/constants/init.py',
    f'src/{project_name}/pipeline/init.py',
    f'src/{project_name}/pipeline/training_pipeline.py',
    f'src/{project_name}/pipeline/prediction_pipeline.py',
    'notebook/research.ipynb'
    'schema.yaml',
    'params.yaml',
    'config/config.yaml',
    'setup.py',
    'app.py',
    'template/index.html',
    'static/style.css',
    'Dockerfile'
]

for dir in list_of_dir:
    dir = Path(dir)
    filedir, filename = os.path.split(dir) ## splitting the directory

## creating empty directory
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"making dir of path {filedir} for the {filename}")

    ## creating the filename in the file directory
    if not (os.path.exists(dir)) or (os.path.getsize(dir)==0):
        with open (dir, 'w') as f:
            pass
        logging.info(f"Creating an empty file for: {dir}")

    else:
        logging.info(f"{dir} exists already")