from diamond.entity.config_entity import DataIngestionConfig
import os
import urllib.request as request
from diamond import logger
from diamond.utils import get_size
from pathlib import Path
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} download! with following info: \n{headers}')
        else:
            logger.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    def train_test_splitting(self):
        data = pd.read_csv(os.path.join(self.config.root_dir, 'gemstone.csv'))

        # Split the data into training and test sets. (0.70, 0.30) split.
        train, test = train_test_split(data, test_size=0.3, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info('Splited data into training and test sets')
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
