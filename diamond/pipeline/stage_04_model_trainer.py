from diamond.config.configuration import ConfigurationManager
from diamond.components.model_trainer import ModelTrainer
from diamond.components.data_transformation import DataTransformation
from diamond import logger


STAGE_NAME = 'Model Trainer Stage'


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()

        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)

        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)

        train_array, test_array = data_transformation.initaite_data_transformation(dump_preprocessor=False)
        model_trainer.train(train_array, test_array)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e
