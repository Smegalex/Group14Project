import csv
import os 
def process_messages(message):
    with open(os.path.join( os.path.join(os.path.dirname(os.path.abspath(__file__)),"data"),message["sender_id"])+".csv","a+", newline="") as csvfile:
        dictionary = message["data"]
        writer = csv.DictWriter(csvfile, fieldnames=dictionary.keys())
        if os.path.getsize(os.path.join( os.path.join(os.path.dirname(os.path.abspath(__file__)),"data"),message["sender_id"])+".csv") == 0:
            writer.writeheader()
        writer.writerow(dictionary)


# testdata = {'sender_id': 'sensor141', 'data': {'temperature': 26.12, 'eCO2Value': 483, 'iaqScore': 55, 'iaqPercent': 89, 'humidity': 23}, 'receiver_id': 'server14S'}
# process_messages(testdata)
