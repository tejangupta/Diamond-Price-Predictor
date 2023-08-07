from diamond.entity.config_entity import ModelTrainerConfig
from diamond import logger
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
import os
import joblib


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self, train_array, test_array):
        try:
            logger.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
            }

            best_model = None
            best_model_name = None
            best_model_score = float('-inf')

            for model_name, model in models.items():
                model.fit(X_train, y_train)
                r2_score = model.score(X_test, y_test)

                if r2_score > best_model_score:
                    best_model_score = r2_score
                    best_model_name = model_name
                    best_model = model

            logger.info(f"{best_model_name} model trained with R2 score: {best_model_score}")

            # Save the best model using joblib
            model_filepath = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(best_model, model_filepath)

            logger.info(f"Model {self.config.model_name} training completed and saved with joblib")
        except Exception as e:
            logger.error(f'Exception occured during model trainer component: {e}')
            raise e
