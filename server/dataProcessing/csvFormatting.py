import csv
import os

dir_path = os.path.join(os.path.dirname(os.path.abspath(
    __file__)), "data")


def process_messages(message):
    with open(os.path.join(dir_path, message["sender_id"])+".csv", "a+", newline="") as csvfile:
        dictionary = message["data"]
        writer = csv.DictWriter(csvfile, fieldnames=dictionary.keys())
        if os.path.getsize(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"), message["sender_id"])+".csv") == 0:
            writer.writeheader()
        writer.writerow(dictionary)


def clear_data(sensor_numbers: int | list | None = None) -> None:
    sensor_template = "sensor14"
    if not sensor_numbers:
        for i in range(1, 10):
            file_path = os.path.join(
                dir_path, sensor_template) + str(i) + ".csv"
            if os.path.exists(file_path):
                os.remove(file_path)
    else:
        for sensor_number in sensor_numbers:
            if not isinstance(sensor_number, int):
                continue
            sensor_name = "sensor" + str(sensor_number)
            file_path = os.path.join(
                dir_path, sensor_name) + ".csv"
            if os.path.exists(file_path):
                os.remove(file_path)
