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
    return {"api": "Version 1.0"}


@app.get("/generate_features")
def features_generator(
    operations_dict: OperationsDictionary,
    features_path: str,
):

    # DATA READING BLOCK
    start_time = datetime.now()
    operations_dict = operations_dict.dict()
    data_obj = FeaturesReader(features_path)
    end_time = datetime.now()

    # DATA PROCESSING BLOCK
    start_ptime = datetime.now()
    features_generator_obj = MultiFeaturesGenerator()

    all_threads = []
    for key, value in operations_dict.items():
        for single_window in value:

            th = Process(
                target=MultiFeaturesGenerator.RollingOperations,
                args=(
                    data_obj.data,
                    single_window,
                    key,
                ),
            )

            th.start()
            all_threads.append(th)

            features_generator_obj.RollingOperations(
                incoming_df=data_obj.data,
                rolling_window_size=single_window,
                operation_type=key,
            )

    for process in all_threads:
        process.join()

    final_df = pd.concat([data_obj.data, features_generator_obj.df], axis=1)
    final_df.to_csv(config.get("export_csv_path"), index=False)
    end_ptime = datetime.now()

    return ResponseModel(
        Loading_Time=str(end_time - start_time),
        Processing_Time=str(end_ptime - start_ptime),
        Final_Features_List=final_df.columns.to_list(),
    )
