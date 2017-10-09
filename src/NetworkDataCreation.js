var AWS = require("aws-sdk");
AWS.config.update({
region: "ap-southeast-1"
});
var dynamodb = new AWS.DynamoDB();
var params = {
TableName : "NetworkData",
KeySchema: [
{ AttributeName: "MoteID", KeyType: "HASH" }, //Partition key
{ AttributeName: "MoteTimestamp", KeyType: "RANGE"} //Sort key
],
AttributeDefinitions: [
{ AttributeName: "MoteID", AttributeType: "N" },
{ AttributeName: "MoteTimestamp", AttributeType: "S" }
],
ProvisionedThroughput: {
ReadCapacityUnits: 10,
WriteCapacityUnits: 10
}
};
dynamodb.createTable(params, function(err, data) {
if (err) {
console.error("Unable to create table. Error JSON:", JSON.stringify(err, null,
2));
} else {
console.log("Created table. Table description JSON:", JSON.stringify(data,
null, 2));
}
});

