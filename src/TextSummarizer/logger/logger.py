import os, sys
from datetime import datetime
import logging

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

## creating the directory for the Logfile (./log/LOG_FILE_NAME/LOG_FILE_NAME)

log_dir= os.path.join(os.getcwd(), 'logs', LOG_FILE_NAME)
os.makedirs(log_dir, exist_ok=True)

##path to the file name
file_name = os.path.join(log_dir, LOG_FILE_NAME)

logging.basicConfig(
    format= "[ %(asctime)s ]: %(name)s: %(levelname)s: %(module)s: %(lineno)s: %(message)s",
    level= logging.INFO,

    handlers= [
        logging.FileHandler(file_name),
        logging.StreamHandler(sys.stdout)
        ]
    )

logger= logging.getLogger('textsummarizer')