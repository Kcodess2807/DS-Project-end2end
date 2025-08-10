from src.dataScience.config.configuration import ConfigurationManager
from src.dataScience.components.model_evaluation import ModelEval
from src.dataScience import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEval(config=model_evaluation_config)
        model_evaluation.login_to_mlflow()