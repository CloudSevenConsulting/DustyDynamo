var AWS = require("aws-sdk");
var fs = require('fs');

var stockData = ['BHP.AX.json', 'RIO.json', 'WPL.json'];

AWS.config.update({
region: "ap-southeast-1"
});
var docClient = new AWS.DynamoDB.DocumentClient();
console.log("Importing stock data into DynamoDB. Please wait.");
var allStock = JSON.parse(fs.readFileSync('WPL.AX.json', 'utf8'));
allStock.forEach(function(engData) {
var params = {
TableName: "NetworkData",
Item: {
"MoteTimestamp": engData.MoteTimestamp,
"MoteID": engData.MoteID,
"StockData": engData.StockData
}
};
docClient.put(params, function(err, data) {
if (err) {
console.error("Unable to add timestamp", engData.MoteTimestamp, ". Error JSON:",
JSON.stringify(err, null, 2));
} else {
console.log("PutItem succeeded:", engData.MoteTimestamp);
}
});
});
