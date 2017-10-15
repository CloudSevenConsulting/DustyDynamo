from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import numpy as np

### Helper class to convert a DynamoDB item to JSON.
##class DecimalEncoder(json.JSONEncoder):
##    def default(self, o):
##        if isinstance(o, decimal.Decimal):
##            if o % 1 > 0:
##                return float(o)
##            else:
##                return int(o)
##        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

table = dynamodb.Table('NetworkData')

print("MoteID = 2, Data from 2017")

response = table.query(
KeyConditionExpression=Key('MoteID').eq(2) & Key('MoteTimestamp').begins_with('2017'),
ScanIndexForward = False
)

MoteID1 = []
MoteTimestamp1 = []
OpenPrice1 = []

for i in response['Items']:
    MoteID1.append(float(i['MoteID']))
    MoteTimestamp1.append(i['MoteTimestamp'])
    OpenPrice1.append(float(i['StockData']['OpenPrice']))
    # print(i['MoteID'], ":", i['MoteTimestamp'], ":", i['StockData']['OpenPrice'])


print("MoteID = 2, Data from 2016")

response = table.query(
KeyConditionExpression=Key('MoteID').eq(2) & Key('MoteTimestamp').begins_with('2016'),
ScanIndexForward = False
)

for i in response['Items']:
    MoteID1.append(float(i['MoteID']))
    MoteTimestamp1.append(i['MoteTimestamp'])
    OpenPrice1.append(float(i['StockData']['OpenPrice']))
    # print(i['MoteID'], ":", i['MoteTimestamp'], ":", i['StockData']['OpenPrice'])

# Sensor Data fabrication
MoteID1 = list(1/2*np.array(MoteID1))
MoteID2 = list(1/2*2*np.array(MoteID1))
MoteID3 = list(1/2*3*np.array(MoteID1))
MoteID4 = list(1/2*4*np.array(MoteID1))
MoteID5 = list(1/2*5*np.array(MoteID1))
MoteID6 = list(1/2*6*np.array(MoteID1))
MoteID7 = list(1/2*7*np.array(MoteID1))

OpenPrice1 = list(np.array(OpenPrice1))
OpenPrice2 = list(0.9*np.array(OpenPrice1))
OpenPrice3 = list(0.8*np.array(OpenPrice1))
OpenPrice4 = list(1.05*np.array(OpenPrice1))
OpenPrice5 = list(1.1*np.array(OpenPrice1))
OpenPrice6 = list(1.2*np.array(OpenPrice1))
OpenPrice7 = list(1.3*np.array(OpenPrice1))

MoteTimestamp1 = MoteTimestamp1
MoteTimestamp2 = MoteTimestamp1
MoteTimestamp3 = MoteTimestamp1
MoteTimestamp4 = MoteTimestamp1
MoteTimestamp5 = MoteTimestamp1
MoteTimestamp6 = MoteTimestamp1
MoteTimestamp7 = MoteTimestamp1


data = open('testing.csv', 'w')

for i in range(0,len(MoteID1)):
    data.write("%s," %MoteID1[i] + "%s," %MoteTimestamp1[i] + "%s," %OpenPrice1[i] +
               "%s," %MoteID2[i] + "%s," %MoteTimestamp2[i] + "%s," %OpenPrice2[i] +
               "%s," %MoteID3[i] + "%s," %MoteTimestamp3[i] + "%s," %OpenPrice3[i] +
               "%s," %MoteID4[i] + "%s," %MoteTimestamp4[i] + "%s," %OpenPrice4[i] +
               "%s," %MoteID5[i] + "%s," %MoteTimestamp5[i] + "%s," %OpenPrice5[i] +
               "%s," %MoteID6[i] + "%s," %MoteTimestamp6[i] + "%s," %OpenPrice6[i] +
               "%s," %MoteID7[i] + "%s," %MoteTimestamp7[i] + "%s, \n" %OpenPrice7[i]
               )

data.close()
