from pathlib import Path
from diamond.config.configuration import ConfigurationManager
from diamond.components.data_transformation import DataTransformation
from diamond import logger


STAGE_NAME = 'Data Transformation Stage'


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status = f.read().split(' ')[-1]

            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                _, _ = data_transformation.initaite_data_transformation()
            else:
                raise Exception('Your data schema is not valid')
        except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e
