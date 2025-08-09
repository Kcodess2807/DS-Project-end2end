from src.dataScience import logger
from src.dataScience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.dataScience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.dataScience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.dataScience.pipeline.model_train_pipeline import ModelTrainerTrainingPipeline

STAGE= "data ingesiton pipeline"
try:
        logger.info(f">>>>>>>>{STAGE}<<<<<<<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f'>>>>>>>>>stage {STAGE} completed <<<<<<< ')
except Exception as e:
        logger.exception(e)
        raise e   


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.initiate_data_validation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

logger.info('welcome to our custom logging data science') 

STAGE_NAME= "Data Transformation Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion=DataTransformationPipeline()
        data_ingestion.initiate_data_transformation
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        raise e

STAGE_NAME= "Model Trainer Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion=ModelTrainerTrainingPipeline()
        data_ingestion.initiate_model_training()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        raise e