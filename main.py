from diamond import logger
from diamond.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from diamond.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from diamond.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from diamond.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from diamond.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f'Exception occured during data ingestion pipeline: {e}')
    raise e


STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f'Exception occured during data validation pipeline: {e}')
    raise e


STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f'Exception occured during data transformation pipeline: {e}')
    raise e


STAGE_NAME = 'Model Trainer Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f'Exception occured during model trainer pipeline: {e}')
    raise e


STAGE_NAME = 'Model Evaluation Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.error(f'Exception occured during model evaluation pipeline: {e}')
    raise e
