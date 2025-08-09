from src.dataScience.config.configuration import ConfigurationManager
from src.dataScience.components.data_transformation import DataTransformation
from src.dataScience import logger
from pathlib import Path
STAGE_NAME='data transformation'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status_str = f.read().split(" ")[-1].strip()
                status = status_str.lower() == "true"

            if status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception('Your data schema is not valid')
        except Exception as e:
            raise e

                

    
                