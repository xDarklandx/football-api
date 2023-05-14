import boto3
import json
from custom_encoder import CustomEncoder
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamoTableName = "football_league"
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(dynamoTableName)

getMethod = "GET"
postMethod = "POST"
patchMethod = "PATCH"
deleteMethod = "DELETE"
healthPath = "/health"
matchPath = "/match"
matchesPath = "/matches"
seasonPath = "/season"
championPath = "/champion"
championsPath = "/champions"


def lambda_handler(event, context):
    logger.info(event)
    logger.info("Received event: " + json.dumps(event))
    httpMethod = event.get("httpMethod")
    path = event.get("path")
    # Health
    if httpMethod == getMethod and path == healthPath:
        response = buildResponse(200)
    # All Matches
    elif httpMethod == getMethod and path == matchesPath:
        response = getMatches()
    # Match CRUD
    elif httpMethod == getMethod and path == matchPath:
        response = getMatch(
            event["queryStringParameters"]["seasonId"],
            event["queryStringParameters"]["sortKey"],
        )
    elif httpMethod == postMethod and path == matchPath:
        response = saveMatch(json.loads(event["body"]))
    elif httpMethod == patchMethod and path == matchPath:
        requestBody = json.loads(event["body"])
        logger.info(requestBody)
        response = modifyMatch(
            requestBody["seasonId"],
            requestBody["sortKey"],
            requestBody["updateKey"],
            requestBody["updateValue"],
        )
    elif httpMethod == deleteMethod and path == matchPath:
        if "body" in event and event["body"]:
            requestBody = json.loads(event["body"])
            response = deleteMatch(requestBody["seasonId"], requestBody["sortKey"])
        else:
            response = buildResponse(400, {"message": "Empty request body"})

    # Season
    elif httpMethod == getMethod and path == seasonPath:
        response = getSeason(event["queryStringParameters"]["seasonId"])
    # Champion
    elif httpMethod == getMethod and path == championPath:
        response = getChampion(
            event["queryStringParameters"]["seasonId"],
            event["queryStringParameters"]["sortKey"],
        )
    elif httpMethod == postMethod and path == championPath:
        response = saveChampion(json.loads(event["body"]))
    elif httpMethod == patchMethod and path == championPath:
        requestBody = json.loads(event["body"])
        response = modifyChampion(
            requestBody["seasonId"],
            requestBody["sortKey"],
            requestBody["updateKey"],
            requestBody["updateValue"],
        )
    elif httpMethod == deleteMethod and path == championPath:
        requestBody = json.loads(event["body"])
        response = deleteChampion(requestBody["seasonId"], requestBody["sortKey"])
    # All Champions
    elif httpMethod == getMethod and path == championsPath:
        response = getChampions()
    else:
        response = buildResponse(404, "Not Found")

    return response


# All Matches


def getMatches():
    try:
        response = table.scan()
        result = response["Items"]

        while "LastEvaluatedKey" in response:
            response = table.scan(ExclusiveStartKey=response["LastEvaluateKey"])
            result.extend(response["Items"])

        body = {"matches": result}
        return buildResponse(200, body)
    except:
        logger.exception("Error")


# Match


def getMatch(partitionKey, sortKey):
    try:
        response = table.get_item(Key={"seasonId": partitionKey, "sortKey": sortKey})
        if "Item" in response:
            return buildResponse(200, response["Item"])
        else:
            return buildResponse(404, {"Message": "sortKey: %s not found" % sortKey})
    except:
        logger.exception("Error")


def saveMatch(requestBody):
    try:
        table.put_item(Item=requestBody)
        body = {"Operation": "SAVE", "Message": "SUCCESS", "Item": requestBody}
        return buildResponse(200, body)
    except:
        logger.exception("Error")


def modifyMatch(partitionKey, sortKey, updateKey, updateValue):
    jsonData = getMatch(partitionKey, sortKey)
    currentData = json.loads(jsonData["body"])[updateKey]
    logger.info(currentData)
    try:
        response = table.update_item(
            Key={"seasonId": partitionKey, "sortKey": sortKey},
            UpdateExpression="SET #attr = :value",
            ConditionExpression="attribute_exists(seasonId)",
            ExpressionAttributeNames={"#attr": updateKey},
            ExpressionAttributeValues={":value": currentData | updateValue},
            ReturnValues="ALL_NEW",
        )
        updated_item = response.get("Attributes", {})
        body = {
            "Operation": "UPDATE",
            "Message": "SUCCESS",
            "UpdatedItem": updated_item,
        }
        return buildResponse(200, body)
    except:
        logger.exception("Error")


def deleteMatch(partitionKey, sortKey):
    try:
        response = table.delete_item(
            Key={"seasonId": partitionKey, "sortKey": sortKey}, ReturnValues="ALL_OLD"
        )
        deleted_item = response.get("Attributes", {})
        body = {
            "Operation": "DELETE",
            "Message": "SUCCESS",
            "DeletedItem": deleted_item,
        }
        return buildResponse(200, body)
    except:
        logger.exception("Error")


# Season


def getSeason(seasonId):
    try:
        response = table.get_item(Key={"seasonId": seasonId})
        if "Item" in response:
            return buildResponse(200, response["Item"])
        else:
            return buildResponse(404, {"Message": "seasonId: %s not found" % seasonId})
    except:
        logger.exception("Error")


# Champion


def getChampion(partitionKey, sortKey):
    try:
        response = table.get_item(Key={"seasonId": partitionKey, "sortKey": sortKey})
        if "Item" in response:
            return buildResponse(200, response["Item"])
        else:
            return buildResponse(404, {"Message": "sortKey: %s not found" % sortKey})
    except:
        logger.exception("Error")


def saveChampion(requestBody):
    try:
        table.put_item(Item=requestBody)
        body = {"Operation": "SAVE", "Message": "SUCCESS", "Item": requestBody}
        return buildResponse(200, body)
    except:
        logger.exception("Error")


def modifyChampion(partitionKey, sortKey, updateKey, updateValue):
    jsonData = getMatch(partitionKey, sortKey)
    currentData = json.loads(jsonData["body"])[updateKey]
    logger.info(currentData)
    try:
        response = table.update_item(
            Key={"seasonId": partitionKey, "sortKey": sortKey},
            UpdateExpression="SET #attr = :value",
            ConditionExpression="attribute_exists(seasonId)",
            ExpressionAttributeNames={"#attr": updateKey},
            ExpressionAttributeValues={":value": currentData | updateValue},
            ReturnValues="ALL_NEW",
        )
        updated_item = response.get("Attributes", {})
        body = {
            "Operation": "UPDATE",
            "Message": "SUCCESS",
            "UpdatedItem": updated_item,
        }
        return buildResponse(200, body)
    except:
        logger.exception("Error")


def deleteChampion(partitionKey, sortKey):
    try:
        response = table.delete_item(
            Key={"seasonId": partitionKey, "sortKey": sortKey}, ReturnValues="ALL_OLD"
        )
        deleted_item = response.get("Attributes", {})
        body = {
            "Operation": "DELETE",
            "Message": "SUCCESS",
            "DeletedItem": deleted_item,
        }
        return buildResponse(200, body)
    except:
        logger.exception("Error")


# All Champions


def getChampions():
    try:
        response = table.scan()
        result = response["Items"]

        while "LastEvaluatedKey" in response:
            response = table.scan(ExclusiveStartKey=response["LastEvaluateKey"])
            result.extend(response["Items"])

        body = {"champions": result}
        return buildResponse(200, body)
    except:
        logger.exception("Error")


# Response Builder


def buildResponse(statusCode, body=None):
    response = {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
    }
    if body is not None:
        response["body"] = json.dumps(body, cls=CustomEncoder)
        return response
    else:
        return response
