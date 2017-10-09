from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

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

print("Data from MoteId 1")

response = table.query(
KeyConditionExpression=Key('MoteID').eq(3) & Key('MoteTimestamp').begins_with('2017'),
ScanIndexForward = False
)

MoteID = []
MoteTimestamp = []
OpenPrice = []

for i in response['Items']:
    MoteID.append(float(i['MoteID']))
    MoteTimestamp.append(i['MoteTimestamp'])
    OpenPrice.append(float(i['StockData']['OpenPrice']))
    print(i['MoteID'], ":", i['MoteTimestamp'], ":", i['StockData']['OpenPrice'])


##import plotly.plotly as py
##import plotly.graph_objs as go
##
##import pandas as pd
##
##data = [go.Scatter(
##          x=MoteTimestamp,
##          y=OpenPrice
##          )]
##
##py.iplot(data)
