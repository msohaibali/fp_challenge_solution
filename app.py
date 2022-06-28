import json
import pandas as pd
from fastapi import FastAPI
from datetime import datetime
from multiprocessing import Process
from Models.ResponseModel import ResponseModel
from Models.OperationsDictionary import OperationsDictionary
from BLC.FeaturesGenerator import FeaturesReader, MultiFeaturesGenerator


with open("config.json", "r", encoding="utf-8") as fl:
    config = json.loads(fl.read())

app = FastAPI()


@app.get("/")
async def root():
    """
    Landing/Index Page of API Server
    """
    return {"api": "Version 1.0"}


@app.get("/generate_features")
def features_generator(
    operations_dict: OperationsDictionary,
    features_path: str,
):
    """
    Route to grab the input and operation dict,
    Performs the Operations in Parallel,

    :param operations_dict: Dictionary with Operations List
    :param features_path: Path of the csv file
    :return dict: Processing Time and Updated COl_NAMES
    """

    # DATA READING BLOCK
    start_time = datetime.now()
    operations_dict = operations_dict.dict()
    data_obj = FeaturesReader(features_path)
    end_time = datetime.now()

    # DATA PROCESSING BLOCK
    start_ptime = datetime.now()
    features_generator_obj = MultiFeaturesGenerator()

    processes_list = list()
    for key, value in operations_dict.items():
        for single_window in value:

            single_process = Process(
                target=MultiFeaturesGenerator.RollingOperations,
                args=(
                    data_obj.data,
                    single_window,
                    key,
                ),
            )

            single_process.start()
            processes_list.append(single_process)

            features_generator_obj.RollingOperations(
                incoming_df=data_obj.data,
                rolling_window_size=single_window,
                operation_type=key,
            )

    # Wait For Running Processes to Finish
    for running_process in processes_list:
        running_process.join()

    # Add the New Feature Columns into main DataFrame
    final_df = pd.concat([data_obj.data, features_generator_obj.df], axis=1)

    # Export CSV File from DataFrame
    final_df.to_csv(config.get("export_csv_path"), index=False)

    end_ptime = datetime.now()

    return ResponseModel(
        Loading_Time=str(end_time - start_time),
        Processing_Time=str(end_ptime - start_ptime),
        Final_Features_List=final_df.columns.to_list(),
    )
