import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        area: int,
        bhk: str,
        furnishing:str,
        parking: int,
        status: str,
        transaction: str,
        type: str
        
        ):
        self.area = area
        self.bhk = bhk
        self.furnishing = furnishing
        self.parking = parking
        self.status = status
        self.transaction = transaction
        self.type = type
 

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                
                "Area": [self.area],
                "BHK": [self.bhk],
                "Furnishing": [self.furnishing],
                "Parking": [self.parking],
                
                "Status": [self.status],
                "Transaction": [self.transaction],
                "Type": [self.type],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
