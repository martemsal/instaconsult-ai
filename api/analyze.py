import json

def handler(request):
    # O Dashboard espera ver 'status': 'completed'
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps({"status": "completed"})
    }
