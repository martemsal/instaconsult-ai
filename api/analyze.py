import json

def handler(event, context=None):
    # O Vercel Runtime moderno espera statusCode e body em JSON
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "status": "completed"
        })
    }
