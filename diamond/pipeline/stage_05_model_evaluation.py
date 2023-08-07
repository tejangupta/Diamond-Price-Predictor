import os
from diamond.config.configuration import ConfigurationManager
from diamond.components.model_evaluation import ModelEvaluation
from diamond import logger

# Set the MLflow tracking URI and credentials here
os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/tejangupta/Diamond-Price-Predictor.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME'] = "tejangupta"
os.environ['MLFLOW_TRACKING_PASSWORD'] = "57e005d59df3df13219b857a79fa2e6076750e4f"


STAGE_NAME = 'Model Evaluation Stage'


class ModelEvaluationTrainingPipeline:
    @staticmethod
    def main():
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config('LinearRegression')
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow('LinearRegressionModel')


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e
