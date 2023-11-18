import csv
from datetime import datetime, timedelta
import random
import string
import json

def generate_dummy_logs(num_logs=100):
    log_data = []

    subjects = ["The system", "A process", "The application", "The server"]
    actions = ["encountered an issue", "completed a task", "is running smoothly", "experienced a failure"]
    contexts = ["while processing data", "during routine maintenance", "at peak load times", "without any specific trigger"]

    for _ in range(num_logs):

        log_entry = {
            "level": random.choice(["info", "warn", "error", "debug"]),
            "message": f"{random.choice(subjects)} {random.choice(actions)} {random.choice(contexts)}.",
            "resourceId": "server-" + ''.join(random.choices(string.digits, k=4)),
            "timestamp": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat() + "Z",
            "traceId": ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
            "spanId": "span-" + ''.join(random.choices(string.digits, k=3)),
            "commit": ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)),
            "metadata": {
                "parentResourceId": "server-" + ''.join(random.choices(string.digits, k=4)) 
            }
        }
        log_data.append(log_entry)

    return log_data

def write_logs_to_csv(log_data, csv_file_path='dummy_logs.csv'):
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ["level", "message", "resourceId", "timestamp", "traceId", "spanId", "commit", "metadata"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write log entries
        writer.writerows(log_data)

def write_logs_to_logs_file(log_data, logs_file_path='dummy_logs.log'):
    with open(logs_file_path, 'w') as file:
        for log_entry in log_data:
            file.write(json.dumps(log_entry))
            file.write('\n')

if __name__ == "__main__":
    num_logs_to_generate = 10000
    logs_data = generate_dummy_logs(num_logs_to_generate)
    write_logs_to_logs_file(logs_data)
