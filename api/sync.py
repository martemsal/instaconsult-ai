from http.server import BaseHTTPRequestHandler
import json
import requests

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Pegar dados do pedido
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data)
        
        insta_handle = payload.get('insta_handle')
        company_id = payload.get('company_id')

        # SIMULAÇÃO DE INTELIGÊNCIA ARTIFICIAL (Para teste imediato)
        # Em breve aqui entra a chamada real para o ChatGPT/Meta API
        insights = {
            "reach": "12.4K",
            "engagement": "4.8%",
            "top_posts": ["Post 1", "Post 2"],
            "strategy": "Aumentar frequência de Reels no nicho de Consultoria."
        }

        # Resposta de Sucesso
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "status": "success",
            "company_id": company_id,
            "data": insights
        }
        self.wfile.write(json.dumps(response).encode())
