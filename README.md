# fp_challenge_solution
This repository contains solution of GitHub [fp_challenge](https://github.com/k-edge/FP_python_challenge)


## PROJECT STRUCTURE
```bash
.
├── .gitignore              # List of Files/Folders to ignore while commits
├── BLC                     # Bussiness Logic (contains Processing/Feature Generation Class)
├── docker                  # Docker File
├── Models                  # Pydantic Models (contains Models for Incoming Data Model and Response Model)
├── output                  # Output Files (contains Generated CSV File)
├── utils                   # Tools and utilities
├── app.py                  # Main Startup File (contains API Routes and Multi-processing Implementation)
├── LICENSE
├── README.md
├── requirements.txt
├── config.json             # Configuration Files (contains export_csv_file path, api server host_address & port)
└── run.bat                 # To Run the Server Locally
```

## Followings are the Features of this Solution

- File Reader Class to load the directory directly into pandas dataframe either from File or Local Directory
- Features Generator Class to Generate multiple new features wrt passed Operations Dictionary. Example
```
{
    "Average": [200, 300],
    "Standard_deviation": [100, 300],
    "Exponential_average": [500,700]
}
```

- Adding New Features Columns in base csv and saving in output folder
- [FASTAPI](https://fastapi.tiangolo.com/) to make API Service of Application
- Dockerized Solution

## Pre-requisites to run the solution
- Docker Desktop
- Python 3.6+ (3.8 recommended) ```**Optional**, Not required if you want to run via Docker```
- clone this repository into your local system or any cloud instance 
```git clone https://github.com/msohaibali/fp_challenge_solution.git```

## HOW TO RUN SERVER
The Solution can be run in 2 ways

### 1. Using Docker
Build the Solution, Grab Pre-installed FAST-API and Python 3.8 Ubuntu Image


Run this command in the project folder
```
docker build -t fp_challenge_app:latest -f docker/Dockerfile .
```

Once the build is finished Successfully Run this Command
```
docker run -p 80:80 fp_challenge_app:latest
```

After that, you should get a message similar to this one containing the URL to your API.
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80(Press CTRL+C toquit)
```


### 2. Run Locally
If you want to run the server locally, install the required packages first by
```
pip install -r requirements.txt
```

then start server by clicking ```run.bat``` file or by using the command ```python run.py```


## Send Requests on Server
Once the Server is up and running you can make request by using any api client [Thunder Client](https://www.thunderclient.com/) or [Postman](https://www.postman.com/)
Enter this url into the browser or API Client to Verify the API Server is Up & Running
### URL: 
```http://localhost (For Local)```

```docker_ip_address (For Docker)```


## Request Features Generation
### ENDPOINT: 

```http://localhost/generate_features?features_path=https://raw.githubusercontent.com/k-edge/FP_python_challenge/master/data/data.csv```

### METHOD: ```GET```

### REQUEST BODY:

Request body is dynamic and features are generated on the basis of values passed in this dictionary,
key_names should be same or API will return validation error.
```
{
    "Average": [200, 300],
    "Standard_deviation": [100, 300],
    "Exponential_average": [500,700]
}
```

Once the Request is successfully completed, you can see the script Execution Time & Newly Generated Column Names List as Response
A CSV File will also be generated with filename ```features.csv``` in folder (Can be changed in config.json file)
```
output/
```


# BONUS
The solution is already an Api Service and Dockerized so is Deployment Ready.
All you need to do is Run the Above mentioned steps on cloud.
For input parameters its already using github generated csv link to load data, that can be changed with an instance uploaded file link.

Output file will be generated on the instance on which the Server is running. 
