import csv


def read_csv(file_path):
    csv_data = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_data.append(row)
    return csv_data
