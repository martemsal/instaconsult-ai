import json

def handler(request):
    # O Dashboard espera "completed" no status para avançar
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "status": "completed",
            "message": "Analise Concluida com Sucesso!"
        })
    }

