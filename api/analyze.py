import json
import requests

def handler(event, context=None):
    try:
        body = json.loads(event.get('body', '{}'))
        token = body.get('access_token')
    except:
        return {"statusCode": 400, "body": "Invalid Request"}

    # 1. Puxar dados básicos do Perfil Real
    # Usamos o endpoint /me para ver quem está conectado
    me_url = f"https://graph.instagram.com/me?fields=id,username,media_count,account_type&access_token={token}"
    
    try:
        res = requests.get(me_url)
        profile = res.json()
        
        # 2. Retorno para o Frontend
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "status": "completed",
                "insights": {
                    "username": profile.get("username"),
                    "media_count": profile.get("media_count"),
                    "score": 8.9, # Score de exemplo gerado pela "IA"
                    "reach": 15400 # Mock de alcance (precisa de permissão business)
                }
            })
        }
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
