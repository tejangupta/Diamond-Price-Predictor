from diamond.entity.config_entity import DataValidationConfig
import pandas as pd
from diamond import logger


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break
                else:
                    data_type = data[col].dtype.name
                    schema_type = all_schema[col]

                    if data_type != schema_type:
                        validation_status = False
                        break

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            logger.error(f'Exception occured during data validation component: {e}')
            raise e
