from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Fatores de emissão em kg CO2/km
            fatores_emissao = {
                'veiculo_proprio': {
                    'gasolina': 0.2271,
                    'etanol': 0.1544,
                    'diesel': 0.2680,
                    'gnv': 0.1950,
                    'eletrico': 0.0000,
                    'nao_se_aplica': 0.2271
                },
                'carro_aplicativo': {
                    'gasolina': 0.2271,
                    'etanol': 0.1544,
                    'diesel': 0.2680,
                    'gnv': 0.1950,
                    'eletrico': 0.0000,
                    'nao_se_aplica': 0.2271
                },
                'motocicleta': {
                    'gasolina': 0.0654,
                    'etanol': 0.0445,
                    'diesel': 0.0654,
                    'gnv': 0.0562,
                    'eletrico': 0.0000,
                    'nao_se_aplica': 0.0654
                },
                'onibus': {
                    'nao_se_aplica': 0.0330
                },
                'bicicleta': {
                    'nao_se_aplica': 0.0000
                },
                'caminhando': {
                    'nao_se_aplica': 0.0000
                }
            }
            
            # Resposta de sucesso
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            response = {
                'status': 'success',
                'fatores_emissao': fatores_emissao,
                'unidade': 'kg CO2/km',
                'fonte': 'Baseado em fatores do IPCC e dados brasileiros'
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