import os
from urllib import request
from src.dataScience import logger
import zipfile
from src.dataScience.entity.config_entity import (DataIngestionConfig)

#component-data-ingestion
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config
        
    def donwload_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers=request.urlretrieve(
                url=self.config.source_URL, 
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} download! with following info: \n{headers}')
        else:
            logger.info(f'file already exists')
    
    def extract_zip(self):
            unzip_path=self.config.unzip_data_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            