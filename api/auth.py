from http.server import BaseHTTPRequestHandler
import requests
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        # Dados do seu App (Vindos do Meta)
        APP_ID = "1534487318249003"
        APP_SECRET = "f4cf5b0ca333853089bfb1e632b09ca6"
        REDIRECT_URI = "https://instaconsult-ai.vercel.app/dashboard.html"
        
        # Troca o "code" por um Token Real
        token_url = f"https://api.instagram.com/oauth/access_token"
        payload = {
            'client_id': APP_ID,
            'client_secret': APP_SECRET,
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'code': data.get('code')
        }
        
        response = requests.post(token_url, data=payload)
        
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(response.content)
