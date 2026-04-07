from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Validação do Facebook (Obrigatória)
        query = self.path.split('?')[-1]
        params = dict(qc.split('=') for qc in query.split('&'))
        
        challenge = params.get('hub.challenge')
        verify_token = params.get('hub.verify_token')
        
        if verify_token == 'instaconsult_secret_123':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(challenge.encode())
