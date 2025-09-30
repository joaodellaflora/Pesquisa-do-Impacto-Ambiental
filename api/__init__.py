from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Configuração para Vercel
app = Flask(__name__)
CORS(app, origins=["*"])  # Permitir todas as origens para Vercel

# Configuração do banco de dados (SQLite funciona na Vercel)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emissoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo do banco de dados
class EmissaoRegistro(db.Model):
    __tablename__ = 'emissao_registros'
    
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(50), nullable=False)
    endereco_origem = db.Column(db.Text, nullable=False)
    endereco_destino = db.Column(db.Text, nullable=False)
    distancia = db.Column(db.Float, nullable=False)
    meio_transporte = db.Column(db.String(50), nullable=False)
    combustivel = db.Column(db.String(30), nullable=False)
    fator_emissao = db.Column(db.Integer, nullable=False)
    emissao_total = db.Column(db.Float, nullable=False)
    categoria_emissao = db.Column(db.String(30), nullable=False)
    dica_sustentabilidade = db.Column(db.Text)
    data_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'matricula': self.matricula,
            'endereco_origem': self.endereco_origem,
            'endereco_destino': self.endereco_destino,
            'distancia': self.distancia,
            'meio_transporte': self.meio_transporte,
            'combustivel': self.combustivel,
            'fator_emissao': self.fator_emissao,
            'emissao_total': self.emissao_total,
            'categoria_emissao': self.categoria_emissao,
            'dica_sustentabilidade': self.dica_sustentabilidade,
            'data_registro': self.data_registro.isoformat() if self.data_registro else None
        }

# Fatores de emissão por tipo de veículo e combustível (g CO₂/km)
FATORES_EMISSAO = {
    "veiculo_proprio": {
        "gasolina": 165,
        "etanol": 95,
        "diesel": 180,
        "gnv": 120,
        "eletrico": 50
    },
    "carro_aplicativo": {
        "gasolina": 165,
        "etanol": 95,
        "diesel": 180,
        "gnv": 120,
        "eletrico": 50
    },
    "motocicleta": {
        "gasolina": 90,
        "etanol": 65,
        "eletrico": 30
    },
    "onibus": {
        "diesel": 80,  # Por passageiro
        "gnv": 60,
        "eletrico": 25
    },
    "bicicleta": {
        "nao_se_aplica": 0
    },
    "caminhando": {
        "nao_se_aplica": 0
    }
}

def get_categoria_emissao(emissao):
    if emissao == 0:
        return "Zero Emissão"
    elif emissao < 2:
        return "Muito Baixa"
    elif emissao < 5:
        return "Baixa"
    elif emissao < 15:
        return "Moderada"
    elif emissao < 30:
        return "Alta"
    else:
        return "Muito Alta"

def get_dica_sustentabilidade(meio_transporte, emissao):
    if meio_transporte in ["bicicleta", "caminhando"]:
        return "Parabéns! Você escolheu um meio de transporte sustentável e saudável!"
    elif emissao == 0:
        return "Excelente escolha! Transporte com zero emissão de carbono."
    elif emissao < 5:
        return "Boa escolha! Baixa emissão de carbono."
    elif emissao < 15:
        return "Considere usar transporte público ou compartilhar a viagem."
    else:
        return "Alta emissão! Considere alternativas mais sustentáveis como transporte público, bicicleta ou carona."

# Criar tabelas
with app.app_context():
    db.create_all()

# Função principal para Vercel
def handler(request):
    return app(request.environ, lambda status, headers: None)