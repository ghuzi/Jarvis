from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import subprocess
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        action = params.get('action', [''])[0]
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        if action == 'filemanager':
            subprocess.Popen(['xdg-open', '/home/muhammad-ghuzaif'])
        elif action == 'terminal':
            subprocess.Popen(['x-terminal-emulator'])
        elif action == 'youtube':
            subprocess.Popen(['xdg-open', 'https://youtube.com'])
        elif action == 'settings':
            subprocess.Popen(['gnome-control-center'])
        elif action == 'vscode':
            subprocess.Popen(['code'])
        elif action == 'firefox':
            subprocess.Popen(['firefox'])
        elif action == 'appcenter':
            subprocess.Popen(['gnome-software'])
        elif action == 'antigravity':
            subprocess.Popen(['antigravity'])
            
        self.wfile.write(json.dumps({'status': 'ok'}).encode())
    
    def log_message(self, format, *args):
        pass

print("Jarvis server running on port 8765...")
HTTPServer(('localhost', 8765), Handler).serve_forever()
