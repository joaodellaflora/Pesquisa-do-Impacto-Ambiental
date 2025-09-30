from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app, origins=["*"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emissoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

with app.app_context():
    db.create_all()

def handler(request):
    """Endpoint para estatísticas gerais"""
    try:
        total_registros = EmissaoRegistro.query.count()
        
        if total_registros == 0:
            return jsonify({
                "total_registros": 0,
                "emissao_total": 0,
                "emissao_media": 0,
                "meio_transporte_mais_usado": None,
                "categoria_mais_comum": None
            })
        
        # Emissão total e média
        emissao_total = db.session.query(db.func.sum(EmissaoRegistro.emissao_total)).scalar() or 0
        emissao_media = db.session.query(db.func.avg(EmissaoRegistro.emissao_total)).scalar() or 0
        
        # Meio de transporte mais usado
        meio_mais_usado = db.session.query(
            EmissaoRegistro.meio_transporte,
            db.func.count(EmissaoRegistro.meio_transporte).label('count')
        ).group_by(EmissaoRegistro.meio_transporte).order_by(db.text('count DESC')).first()
        
        # Categoria mais comum
        categoria_mais_comum = db.session.query(
            EmissaoRegistro.categoria_emissao,
            db.func.count(EmissaoRegistro.categoria_emissao).label('count')
        ).group_by(EmissaoRegistro.categoria_emissao).order_by(db.text('count DESC')).first()
        
        return jsonify({
            "total_registros": total_registros,
            "emissao_total": round(float(emissao_total), 2),
            "emissao_media": round(float(emissao_media), 2),
            "meio_transporte_mais_usado": meio_mais_usado[0] if meio_mais_usado else None,
            "categoria_mais_comum": categoria_mais_comum[0] if categoria_mais_comum else None
        })
        
    except Exception as e:
        return jsonify({"error": f"Erro ao gerar estatísticas: {str(e)}"}), 500