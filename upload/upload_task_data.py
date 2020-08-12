import json
import csv
import os

from db.mongo import MongoDatabase

FILEPATH = os.path.abspath('task_data.csv')
db_client = MongoDatabase("temperature-logs")

def load_csv_to_db():
    csv_row_generator = convert_csv_to_dict(FILEPATH)
    document = []
    result = {}
    
    for item in csv_row_generator:
        for key, val in item.items():
            result[key] = val
        document.append(result)

        result = {}

    db_client.insert_many(document)


def convert_csv_to_dict(file_path):
    reader = csv.DictReader(open(file_path, 'r'))
    for row in reader:
        yield row


if __name__ == '__main__':
    db_names = db_client.client.list_database_names()
    if 'smart_steel_db' in db_names:
        db_client.client.drop_database('smart_steel_db')
    load_csv_to_db()
    print("CSV imported successfully")
