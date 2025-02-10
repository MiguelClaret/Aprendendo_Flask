from sqlalchemy.dialects.postgresql import  UUID, TEXT, ENUM, ARRAY
from sqlalchemy import func
from db import db

#Criando a tabela de prescrição
class Prescricao(db.Model):
    __tablename__ = 'prescricao'

    id = db.Column(db.Integer, nullable = False, primary_key=True)
    hc = db.Column(db.String(255), db.ForeignKey('paciente.hc'), nullable=False)
    lista_remedios = db.Column(ARRAY(db.Integer), nullable=True)
    aprovacao = db.Column(db.Boolean, default=False)
    id_farmaceutico = db.Column(db.Integer, db.ForeignKey('farmaceutico.id'), nullable=False)

    # Fazendo a conexão com as outras tabelas
    paciente = db.relationship('Paciente', backref=db.backref('prescricoes', lazy=True))
    farmaceutico = db.relationship('Farmaceutico', backref=db.backref('prescricoes', lazy=True))



    def as_dict(self):
        return{
            'id': self.id,
            'HC': self.hc,
            'lista_remedios': self.lista_remedios,
            'id_farmaceutico': self.id_farmaceutico,
            'aprovacao':self.aprovacao
        }