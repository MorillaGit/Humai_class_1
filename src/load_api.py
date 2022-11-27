import pandas as pd
from datetime import datetime
import logging


def load_data(df: pd.DataFrame) -> None:
    """Load data to csv"""
    logging.info("Start load data to csv")
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")                         # format date
    base_path_data = "data/"                                                    # Change this path to your path where you want to save the data
    df.to_csv( base_path_data + "data_" + date + ".csv", index=False)
    # print("The data was loaded successfully")
    logging.info("The data was loaded successfully")

    return None