import json
import os
import time
import uuid

import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
bedrock = boto3.client("bedrock-runtime", region_name=os.environ.get("AWS_REGION"))


def handler(event, _context):
    try:
        body = json.loads(event.get("body") or "{}")
        prompt = body.get("prompt", "").strip()
        if not prompt:
            return response(400, {"error": "prompt is required"})

        result = bedrock.converse(
            modelId=os.environ["MODEL_ID"],
            messages=[{"role": "user", "content": [{"text": prompt}]}],
        )
        content = result["output"]["message"]["content"][0]["text"]
        item = {"id": str(uuid.uuid4()), "createdAt": int(time.time()), "prompt": prompt, "content": content}
        table.put_item(Item=item)
        return response(200, item)
    except (ValueError, KeyError) as exc:
        return response(400, {"error": str(exc)})
    except Exception:
        return response(500, {"error": "content generation failed"})


def response(status, body):
    return {"statusCode": status, "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}, "body": json.dumps(body)}
