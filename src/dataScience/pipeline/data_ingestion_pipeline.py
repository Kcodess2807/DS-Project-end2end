from src.dataScience.config.configuration import ConfigurationManager
from src.dataScience.components.data_ingestion import DataIngestion
from src.dataScience import logger


STAGE='data ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.donwload_file()
        data_ingestion.extract_zip()
        
if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>{STAGE}<<<<<<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>stage {STAGE} completed <<<<<<< ')
    except Exception as e:
        logger.exception(e)
        raise e   

