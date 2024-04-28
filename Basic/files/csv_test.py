import csv
import random

def write_record(path,p,r,t,result):
        file_exists = False
        # if os.path.exists(path):
        #     file_exists = True
        with open(path,"a",newline="",encoding='utf-8') as filew:
            results_writer = csv.writer(filew)
            results_writer.writerow([p,r,t,result])

def read_results(file_path):
     with open(file_path,'r') as filer:
          result_reader = csv.reader(filer)
          for record in result_reader:
               print(record)

def write_random_data(csv_path):
    # csv_path = "results.csv"
    for index in range(5):
        p = random.randint(1000,10000)
        r = random.randint(6,24)
        t = random.randint(1,10)
        result = random.randint(1000,10000)
        write_record(csv_path,p,r,t,result)

if __name__=="__main__":
    csv_path = "results.csv"
    write_random_data(csv_path)
    read_results(csv_path)
    