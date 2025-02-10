from flask import Blueprint, jsonify, request
from models.prescricao import Prescricao
from db import db

# criando a rota base
prescricoes_bp = Blueprint('prescricoes', __name__, url_prefix='/prescricoes')

#Rotas:
#Listar todas as prescrições
@prescricoes_bp.route('/listar', methods=['GET'])
def listar_prescricoes():
    prescrioes = Prescricao.query.all()
    return jsonify([prescricao.as_dict() for prescricao in prescrioes])

# Adicionar uma prescriçao nova
@prescricoes_bp.route('/adicionar', methods=['POST'])
def add_prescricao():
    data = request.get_json()
    newPrescricao = Prescricao(
        hc=data['hc'],
        lista_remedios = data['lista_remedios'],
        aprovacao=data['aprovacao'],
        id_farmaceutico=data['id_farmaceutico']
        )

    db.session.add(newPrescricao)
    db.session.commit()
    return jsonify({
        'message': 'Prescrição inserida com sucesso',

    }), 201

# Buscar prescrições por Id
@prescricoes_bp.route('/<prescricao_id>', methods=['GET'])
def get_book(prescricao_id):
    prescricao = Prescricao.query.get_or_404(prescricao_id)
    return jsonify(prescricao.as_dict()), 200

# Aprovar a prescrição
@prescricoes_bp.route('/aprovar/<prescricao_id>', methods=['PATCH'])
def aprovar_prescricao(prescricao_id):
    prescricao = Prescricao.query.get_or_404(prescricao_id)
    prescricao.aprovacao = True

    db.session.commit()
    return jsonify({'Message': 'Prescricao aprovada com sucesso'}), 200

# Deletar a prescrição
@prescricoes_bp.route('/deletar/<prescricao_id>', methods=['DELETE'])
def delete_book(prescricao_id):
    prescricao = Prescricao.query.get_or_404(prescricao_id)
    db.session.delete(prescricao)
    db.session.commit()
    return jsonify({'Message': 'Prescricao deletada com sucesso'}), 200