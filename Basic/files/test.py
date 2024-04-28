import random

# principal = 10000
# rate = 0.05
# time = 5
# result = 10000

def write_result(principal, rate, time, result):
    """ This function appends the result to the file
    """
    with open("results.csv","a") as writer:
        writer.write(f"{principal},{rate},{time},{result}\n")

def print_result():
    with open("results.csv","r") as reader:
        for line in reader.readlines():
            print(line)
            
         
if __name__=="__main__":
    for index in range(10):
        p = random.randint(1000,10000)
        r = random.randint(6,24)
        t = random.randint(1,10)
        result = random.randint(1000,10000)
        write_result(p,r,t,result)
    print_result()
