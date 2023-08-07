from diamond.entity.config_entity import ModelEvaluationConfig
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
from diamond import logger
from diamond.config.configuration import ConfigurationManager
from diamond.components.data_transformation import DataTransformation
import mlflow
from urllib.parse import urlparse
from diamond.utils import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    @staticmethod
    def eval_metrics(actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2

    def log_into_mlflow(self, model_name: str):
        try:
            # Load the model
            model = joblib.load(self.config.model_path)

            config = ConfigurationManager()

            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            _, test_array = data_transformation.initaite_data_transformation(dump_preprocessor=False)

            test_x = test_array[:, :-1]
            test_y = test_array[:, -1]

            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():
                predicted_qualities = model.predict(test_x)

                rmse, mae, r2 = self.eval_metrics(test_y, predicted_qualities)

                # Saving metrics as local
                scores = {"rmse": rmse, "mae": mae, "r2": r2}
                save_json(path=Path(self.config.metric_file_name), data=scores)

                mlflow.log_params(self.config.all_params)

                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)

                # Model registry does not work with file store
                if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(model, "model", registered_model_name=model_name)
                else:
                    mlflow.sklearn.log_model(model, "model")
        except Exception as e:
            logger.error(f'Exception occured during model evaluation component: {e}')
            raise e
