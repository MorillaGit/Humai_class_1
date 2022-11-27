import pandas as pd
# from IPython.display import display
import logging


def transform(data: str) -> pd.DataFrame:
    """Transform data to DataFrame"""
    # Create a empty DataFrame whit a columns "number" and "description"
    logging.info("Start transform data to DataFrame")
    df = pd.DataFrame(columns=["number", "description"])
    elements_response = data.split(' ', 1)
    df = pd.concat([df, pd.DataFrame({'number': elements_response[0], 'description': elements_response[1].capitalize()}, index=[0])], ignore_index=False)
    # print("The data was transformed successfully")
    # display(df)
    logging.info("The data was transformed successfully")

    return df