import http.server
import socketserver
import json
import os
import sys

# Add execution to sys path if needed
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from execution.manage_companies import load_db, save_db

PORT = 8001

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/companies':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            db = load_db()
            new_company = {
                "id": data.get("id"),
                "name": data.get("name"),
                "niche": data.get("niche"),
                "plan": "Pro",
                "username": data.get("username"),
                "password": data.get("password"),
                "insta_handle": data.get("insta_handle"),
                "status": "Active",
                "analysis_pending": False,
                "history": []
            }
            db.append(new_company)
            save_db(db)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success"}')

        elif self.path == '/api/request_analysis':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            db = load_db()
            found = False
            for c in db:
                if c['username'] == data.get('username'):
                    c['analysis_pending'] = True
                    found = True
            save_db(db)

            if found:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"status": "success"}')
            else:
                self.send_response(404)
                self.end_headers()
                
        elif self.path == '/api/delete_company':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            db = load_db()
            db = [c for c in db if c['id'] != data.get('id')]
            save_db(db)
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success"}')
            
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving custom API and static files at port", PORT)
    httpd.serve_forever()
