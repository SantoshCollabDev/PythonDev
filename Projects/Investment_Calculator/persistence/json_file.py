""" This mdule will have utilities to write the data in json format
Author: Santosh
"""
import json
import os
RESULTS_FILE_PATH = "results.json"

def write_results(principal,
                  interest_rate,
                  time,
                  investment_type,
                  future_value):
    """
      This function writes the results to a csv file
    """
    records = []
    if os.path.exists(RESULTS_FILE_PATH):
        with open(RESULTS_FILE_PATH, 'r') as reader:
            records = json.load(reader)

    record = {
        "principal": principal,
        "interest_rate": interest_rate,
        "time": time,
        "investment_type": investment_type,
        "future_value": future_value
    }

    records.append(record)
    with open(RESULTS_FILE_PATH,'w',encoding='utf-8') as filew:
        filew.write(json.dumps(records,indent=2))