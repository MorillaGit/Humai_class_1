from src import utils, extract_api, transform_api, load_api
import logging

# Create and configure logger
base_path_logfile = "logfile/" 
path_logfile = base_path_logfile + "logfile.log"
logging.basicConfig(
    # save log in folder logfile        
    filename = path_logfile,
    format="%(asctime)s %(message)s",
    filemode="w"
)

def main() -> None:
    
    args = utils.make_parser().parse_args()
    
    data = extract_api.get_data(args.number)

    data_transform = transform_api.transform(data)

    load_api.load_data(data_transform)


if __name__ == "__main__":
    # Creating an object
    logger = logging.getLogger()
    # Setting the threshold of logger to info
    logger.setLevel(logging.INFO)

    main()
