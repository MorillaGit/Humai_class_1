import requests
import logging



def get_data(number_consult: int) -> str:
    """Get data from API"""
    # use logging to log the data
    logging.info("Start get data from API")
    url_basic = "http://numbersapi.com/"
    consult_number = str(number_consult)
    data = requests.get(url_basic + consult_number)
    # print("The data was obtained successfully")
    logging.info("The data was obtained successfully")

    return data.text