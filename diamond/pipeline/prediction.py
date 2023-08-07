from pathlib import Path
from diamond.utils import load_bin
from diamond import logger
import pandas as pd


class PredictionPipeline:
    @staticmethod
    def predict(features):
        try:
            preprocessor = load_bin(Path('artifacts/data_transformation/preprocessor.joblib'))
            model = load_bin(Path('artifacts/model_trainer/model.joblib'))

            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled)

            return prediction
        except Exception as e:
            logger.exception('Exception occurred in prediction')
            raise e


class CustomData:
    def __init__(self,
                 carat: float,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float,
                 cut: str,
                 color: str,
                 clarity: str):

        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat': [self.carat],
                'depth': [self.depth],
                'table': [self.table],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z],
                'cut': [self.cut],
                'color': [self.color],
                'clarity': [self.clarity]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logger.info('Dataframe Gathered')

            return df
        except Exception as e:
            logger.exception('Exception Occurred in prediction pipeline')
            raise e
