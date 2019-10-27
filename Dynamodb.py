import boto3
from boto3.dynamodb.conditions import Key, Attr

tableName = "OptiRoll"
Primary_Key = "Adrian"
Primary_Name= "Name"
columns = ["isPresent"]

client = boto3.client('dynamodb').list_tables()
print(client)
db = boto3.resource('dynamodb')
table = db.Table(tableName)

table.put_item(
    Item = {Primary_Name: "Uday's Computer",
            columns[0]: False
            }
    )