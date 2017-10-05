var AWS = require("aws-sdk");
AWS.config.update({
region: "ap-southeast-1"
});
var dynamodb = new AWS.DynamoDB();
var params = {
TableName : "ConfigurationData"
};
dynamodb.deleteTable(params, function(err, data) {
if (err) {
console.error("Unable to delete table. Error JSON:", JSON.stringify(err, null,
2));
} else {
console.log("Deleted table. Table description JSON:", JSON.stringify(data,
null, 2));
}
});