import csv

with open('test.csv') as f:
    a = [{k: str(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]	

