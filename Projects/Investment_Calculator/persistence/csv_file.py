"""this
"""
import csv
RESULTS_FILE_PATH = "results.csv"

def write_result(principal, interest_rate, time, future_Value):
  """this
  """
  with open(RESULTS_FILE_PATH,'a',newline='',encoding=
            'utf-8') as filew:
      results_writer = csv.writer(filew)
      results_writer.writerow(principal, interest_rate, time, future_Value)


def read_all_results():
  """this
  """
  with open(RESULTS_FILE_PATH,'r',newline='',encoding=
            'utf-8') as filer:
      results_reader = csv.writer(filer)
      for result in results_reader:
         yield result
