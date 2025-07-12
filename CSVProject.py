import csv

import os
print("Current working directory:", os.getcwd())

def summary(file, field_name: str):
    return f"field_name: {field_name} min: {sum_min(file,field_name)}, max: {sum_max(file,field_name)}, mean: {sum_mean(file,field_name):.2f}"

def sum_min(file, field_name):
    data_points = []
    for dp in file:
        data_points.append(float(dp[field_name]))
    return min(data_points)

def sum_max(file, field_name):
    data_points = []
    for dp in file:
        data_points.append(float(dp[field_name]))
    return max(data_points)

def sum_mean(file, field_name):
    data_points_total = 0
    for dp in file:
        data_points_total += float(dp[field_name])
    return data_points_total 

# ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

with open('iris.csv','r') as file:
    file_reader = csv.DictReader(file)
    data = [obs for obs in file_reader]

    print(summary(data,'sepal_width'))
    