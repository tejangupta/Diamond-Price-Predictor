from diamond.entity.config_entity import DataTransformationConfig
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
import os
from diamond import logger
import joblib
import numpy as np


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    @staticmethod
    def get_data_transformation_obj():
        try:
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

            # Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',
                     OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                    ('scaler', StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_cols),
                ('cat_pipeline', cat_pipeline, categorical_cols)
            ])

            return preprocessor
        except Exception as e:
            raise e

    def initaite_data_transformation(self, dump_preprocessor=True):
        try:
            train_df = pd.read_csv(self.config.train_data_path)
            test_df = pd.read_csv(self.config.test_data_path)

            logger.info('Read train and test data completed')
            logger.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logger.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logger.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_obj()

            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']

            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            # Transforming using preprocessor obj
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logger.info("Applying preprocessing object on training and testing datasets.")

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            if dump_preprocessor:
                preprocessor_path = os.path.join(self.config.root_dir, 'preprocessor.joblib')
                joblib.dump(preprocessing_obj, preprocessor_path)

                logger.info('Preprocessor joblib file saved')

            return train_arr, test_arr
        except Exception as e:
            logger.error(f'Exception occured during data transformation component: {e}')
            raise e
