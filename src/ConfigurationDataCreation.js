var AWS = require("aws-sdk");
AWS.config.update({
region: "ap-southeast-1"
});
var dynamodb = new AWS.DynamoDB();
var params = {
TableName : "ConfigurationData",
KeySchema: [
{ AttributeName: "MoteTimestamp", KeyType: "HASH" }, //Partition key
{ AttributeName: "MoteID", KeyType: "RANGE"} //Sort key
],
AttributeDefinitions: [
{ AttributeName: "MoteTimestamp", AttributeType: "S" },
{ AttributeName: "MoteID", AttributeType: "N" }
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