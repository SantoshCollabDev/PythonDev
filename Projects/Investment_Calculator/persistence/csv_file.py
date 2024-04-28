"""this
"""
import csv
import os
RESULTS_FILE_PATH = "results.csv"

def write_result(principal, interest_rate, time, investment_type, future_value):
    """this
    """
    print(os.path.abspath(RESULTS_FILE_PATH))

    file_exists = False
    if os.path.exists(RESULTS_FILE_PATH):
        file_exists = True
    with open(RESULTS_FILE_PATH,'a',newline='',encoding=
              'utf-8') as filew:
        results_writer = csv.writer(filew)
        if not file_exists:
            results_writer.writerow(['principal', 'interest_rate', 'time', 'investment_type', 'future_value'])   
        results_writer.writerow([principal, interest_rate, time, investment_type, future_value])

def read_all_results():
    """this
    """
    with open(RESULTS_FILE_PATH,'r',newline='',encoding=
              'utf-8') as filer:
        results_reader = csv.writer(filer)
        for result in results_reader:
          yield result