import csv
import os 
def process_messages(message):
    with open(os.path.join( os.path.join(os.path.dirname(os.path.abspath(__file__)),"data"),message["sender_id"])+".csv","a+", newline="") as csvfile:
        dictionary = message["data"]
        writer = csv.DictWriter(csvfile, fieldnames=dictionary.keys())
        if os.path.getsize(os.path.join( os.path.join(os.path.dirname(os.path.abspath(__file__)),"data"),message["sender_id"])+".csv") == 0:
            writer.writeheader()
        writer.writerow(dictionary)


#testdata = {"sender_id":"sensor140","receiver_id":"14S","data":{"temperature":50,"humidity":25}}
#process_messages(testdata)