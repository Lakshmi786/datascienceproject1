from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Tranformation Stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        
        try:
            with open(Path("artifacts/data_validation/status.txt"),'r') as f:
                status = f.read().split(" ")[-1]
            if status:
                config = ConfigurationManager()
                data_tranformation_config = config.get_data_transformation_config()
                data_tranformation = DataTransformation(config=data_tranformation_config)
                data_tranformation.train_test_split()
            else:
                raise Exception('Your data schema is not valid')
            
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<\n\n=========x")
    except Exception as e:
        logger.exception(e)
        raise e

