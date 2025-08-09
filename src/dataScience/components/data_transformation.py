from src.dataScience.config.configuration import DataTransformationConfig
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.dataScience import logger

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config=config
        
        
    #here we can do, different methods 
    
    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)
        
        train, test=train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, 'train_csv'), index=False)
        train.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info('splitting of data completed!!')
        logger.info(train.shape)
        logger.info(test.shape)
        
        print(train.shape)
        print(test.shape)
        