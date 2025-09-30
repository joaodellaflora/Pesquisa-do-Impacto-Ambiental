from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
CORS(app, origins=["*"])

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emissoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo (mesmo do __init__.py)
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

# Fatores de emissão
FATORES_EMISSAO = {
    "veiculo_proprio": {"gasolina": 165, "etanol": 95, "diesel": 180, "gnv": 120, "eletrico": 50},
    "carro_aplicativo": {"gasolina": 165, "etanol": 95, "diesel": 180, "gnv": 120, "eletrico": 50},
    "motocicleta": {"gasolina": 90, "etanol": 65, "eletrico": 30},
    "onibus": {"diesel": 80, "gnv": 60, "eletrico": 25},
    "bicicleta": {"nao_se_aplica": 0},
    "caminhando": {"nao_se_aplica": 0}
}

def get_categoria_emissao(emissao):
    if emissao == 0: return "Zero Emissão"
    elif emissao < 2: return "Muito Baixa"
    elif emissao < 5: return "Baixa"
    elif emissao < 15: return "Moderada"
    elif emissao < 30: return "Alta"
    else: return "Muito Alta"

def get_dica_sustentabilidade(meio_transporte, emissao):
    if meio_transporte in ["bicicleta", "caminhando"]:
        return "Parabéns! Você escolheu um meio de transporte sustentável e saudável!"
    elif emissao == 0: return "Excelente escolha! Transporte com zero emissão de carbono."
    elif emissao < 5: return "Boa escolha! Baixa emissão de carbono."
    elif emissao < 15: return "Considere usar transporte público ou compartilhar a viagem."
    else: return "Alta emissão! Considere alternativas mais sustentáveis como transporte público, bicicleta ou carona."

# Criar tabelas
with app.app_context():
    db.create_all()

def handler(request):
    """Endpoint para salvar dados sem retornar cálculos"""
    if request.method != 'POST':
        return jsonify({"error": "Método não permitido"}), 405
        
    try:
        data = request.get_json()
        
        # Validações
        matricula = data.get("matricula", "")
        endereco_origem = data.get("endereco_origem", "")
        endereco_destino = data.get("endereco_destino", "")
        distancia = float(data.get("distancia", 0))
        meio_transporte = data.get("meio_transporte", "")
        combustivel = data.get("combustivel", "nao_se_aplica")
        autorizacao = data.get("autorizacao", False)
        
        if not matricula or len(matricula) < 3:
            return jsonify({"error": "Matrícula deve ter pelo menos 3 caracteres"}), 400
        if not endereco_origem or not endereco_destino:
            return jsonify({"error": "Endereços são obrigatórios"}), 400
        if distancia <= 0:
            return jsonify({"error": "Distância deve ser maior que zero"}), 400
        if not meio_transporte:
            return jsonify({"error": "Meio de transporte é obrigatório"}), 400
        if not autorizacao:
            return jsonify({"error": "Autorização é obrigatória"}), 400
        
        # Calcular emissão
        fator_emissao = 0
        if meio_transporte in FATORES_EMISSAO:
            if combustivel in FATORES_EMISSAO[meio_transporte]:
                fator_emissao = FATORES_EMISSAO[meio_transporte][combustivel]
            else:
                fator_emissao = FATORES_EMISSAO[meio_transporte].get("gasolina", 0)
        
        emissao_total_kg = round((distancia * fator_emissao) / 1000, 2)
        categoria = get_categoria_emissao(emissao_total_kg)
        dica = get_dica_sustentabilidade(meio_transporte, emissao_total_kg)
        
        # Salvar no banco
        novo_registro = EmissaoRegistro(
            matricula=matricula,
            endereco_origem=endereco_origem,
            endereco_destino=endereco_destino,
            distancia=distancia,
            meio_transporte=meio_transporte,
            combustivel=combustivel,
            fator_emissao=fator_emissao,
            emissao_total=emissao_total_kg,
            categoria_emissao=categoria,
            dica_sustentabilidade=dica
        )
        
        db.session.add(novo_registro)
        db.session.commit()
        
        return jsonify({
            "sucesso": True,
            "mensagem": "Dados salvos com sucesso!",
            "registro_id": novo_registro.id
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500