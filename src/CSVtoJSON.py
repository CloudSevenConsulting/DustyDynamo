import csv
import json
from pprint import pprint
import os

stockData = ['RIO']

for i in range(0,len(stockData)):
    csvfile = open(stockData[i]+'.csv', 'r')

    fieldnames = ("NetworkTime","StockID","Open","High", "Low", "Close", "Adj Close", "Volume")
    reader = csv.DictReader( csvfile, fieldnames)

    data = open(stockData[i]+'.json', 'w')
    data.write('[\n')

    for row in reader:
        data.write('{ \n' \
                + '"MoteTimestamp": "%s",' %row['NetworkTime'] \
                + '\n"MoteID": %s,' %row['StockID'] \
                + '\n   "StockData":{' \
                + '\n   "OpenPrice": %s,' %row['Open'] \
                + '\n   "HighPrice": %s,' %row['High'] \
                + '\n   "LowPrice": %s,' %row['Low'] \
                + '\n   "ClosePrice": %s,' %row['Close'] \
                + '\n   "Adj Close": %s,' %row['Adj Close'] \
                + '\n   "VolumeNumber": %s' %row['Volume'] \
                + '\n   }' \
                + '\n},\n'
                )

    data.close()

    with open(stockData[i]+'.json', 'rb+') as filehandle:
        filehandle.seek(-3, os.SEEK_END)
        filehandle.truncate()
        filehandle.close()

    with open(stockData[i]+'.json', 'a') as filehandle:
        filehandle.write("\n]")


