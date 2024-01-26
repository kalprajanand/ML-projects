from src.MLprojects.logger import logging
from src.MLprojects.exception import CustomException
from src.MLprojects.components.data_ingestion import DataIngestion 
from src.MLprojects.components.data_ingestion import DataIngestionConfig 
from src.MLprojects.components.data_transformatiom import DataTransformationConfig,DataTransformation
from src.MLprojects.components.model_trainer import ModelTrainerConfig, ModelTrainer

import sys

if __name__=="__main__":
    logging.info("The execution has started")
    
    
    
    try:
        ##data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
         #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        
        
        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as ex:
        logging.info("custom Exception")
        raise CustomException(ex,sys)
        