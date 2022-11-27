
# Basic ETL
## Introduction
This repository has the function obtain data from a simple API from [Number API](http://numbersapi.com/#42)
and load it csv file.

<img title="output"  src="assets/api_image.png">

## Organization

The organization of this repository is as follows:

<pre>
├───src
│   ├─── extract_api.py
│   ├─── load_api.py
│   ├─── transform_api.py
│   └─── utils.py
├───data
├───logfile
├─── README.md
└─── requirements.txt
</pre>

# Installation instructions
### Create a virtualenv or conda environment
    python -m venv path\to\myenv
    conda create -n myenv python=3.7

### Clone the project repository
    git clone https://github.com/MorillaGit/ETL_basic

#### move to the project directory
    cd ETL_basic

### Install the requirements
    pip install -r requirements.txt

# Run the project
    python src/main.py


## Expected output

<img title="output"  src="assets/output.png">