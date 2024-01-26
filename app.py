from src.MLprojects.logger import logging
from src.MLprojects.exception import CustomException
from src.MLprojects.components.data_ingestion import DataIngestion 
from src.MLprojects.components.data_ingestion import DataIngestionConfig 

import sys

if __name__=="__main__":
    logging.info("The execution has started")
    
    
    
    try:
        ##data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as ex:
        logging.info("custom Exception")
        raise CustomException(ex,sys)
        