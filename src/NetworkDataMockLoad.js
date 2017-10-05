var AWS = require("aws-sdk");
var fs = require('fs');

var stockData = ["BHP", "WPL", "RIO"];

for (i=0;i<=stockData.length;i++){
	AWS.config.update({
	region: "ap-southeast-1"
	});
	var docClient = new AWS.DynamoDB.DocumentClient();
	console.log("Importing movies into DynamoDB. Please wait.");
	var allStock = JSON.parse(fs.readFileSync(stockData[i]+'.json', 'utf8'));
	allStock.forEach(function(WSN) {
	var params = {
	TableName: "NetworkData",
	Item: {
	"Timestamp": NetworkData.Timestamp,
	"DeviceID": NetworkData.DeviceID,
	"Data": NetworkData.Data
	}
	};
	docClient.put(params, function(err, data) {
	if (err) {
	console.error("Unable to add timestamp", WSN.Timestamp, ". Error JSON:",
	JSON.stringify(err, null, 2));
	} else {
	console.log("PutItem succeeded:", WSN.Timestamp);
	}
	});
	});
}