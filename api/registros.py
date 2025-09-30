from http.server import BaseHTTPRequestHandler
import json
import sqlite3
import os
from urllib.parse import parse_qs

# Inicialização do banco de dados
def init_database():
    """Inicializa o banco de dados SQLite."""
    db_path = '/tmp/emissao.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emissao_registro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula TEXT NOT NULL,
            endereco_origem TEXT NOT NULL,
            endereco_destino TEXT NOT NULL,
            distancia REAL NOT NULL,
            meio_transporte TEXT NOT NULL,
            combustivel TEXT NOT NULL,
            autorizacao BOOLEAN NOT NULL,
            emissao_co2 REAL NOT NULL,
            data_registro DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Inicializar banco se necessário
            init_database()
            
            # Conectar ao banco
            db_path = '/tmp/emissao.db'
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Buscar todos os registros
            cursor.execute('''
                SELECT id, matricula, endereco_origem, endereco_destino, 
                       distancia, meio_transporte, combustivel, autorizacao, 
                       emissao_co2, data_registro
                FROM emissao_registro 
                ORDER BY data_registro DESC
            ''')
            
            registros = cursor.fetchall()
            conn.close()
            
            # Converter para formato JSON
            dados = []
            for registro in registros:
                dados.append({
                    'id': registro[0],
                    'matricula': registro[1],
                    'endereco_origem': registro[2],
                    'endereco_destino': registro[3],
                    'distancia': registro[4],
                    'meio_transporte': registro[5],
                    'combustivel': registro[6],
                    'autorizacao': bool(registro[7]),
                    'emissao_co2': registro[8],
                    'data_registro': registro[9]
                })
            
            # Resposta de sucesso
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            response = {
                'status': 'success',
                'total_registros': len(dados),
                'registros': dados
            }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False, indent=2).encode('utf-8'))
            
        except Exception as e:
            # Resposta de erro
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            error_response = {
                'status': 'error',
                'error': str(e)
            }
            
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        # Resposta para preflight CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()