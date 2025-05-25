import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

#import Sklear
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestConfig:
    train_data_path: str = os.path.join('artifacts','train_csv')
    test_data_path: str = os.path.join('artifacts','test_csv')
    raw_data_path: str = os.path.join('artifacts','data_csv')


#Data Ingestion

class DataIngest:
    def __init__(self):
        self.ingestion_config = DataIngestConfig()

    def intiate_data_ingest(self):
        logging.info("Enter the Data ingestion method or component")
        try:
            df = pd.read_csv(r'C:\Projects\mlprojects\notebook\data\stud.csv')
            logging.info('Read the Datasets as data frame')

            #Create the folders
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info("Train, Test, Split intiated")

            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)


            logging.info("Ingesting of the data is completed")


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngest()
    obj.intiate_data_ingest()
