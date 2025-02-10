from flask import Flask
from db import db
from flask_migrate import Migrate
from models.paciente import Paciente
from models.farmaceutico import Farmaceutico
from models.prescricao import Prescricao
from routes.prescricoes import prescricoes_bp  

app = Flask(__name__)

# configurando a conexão com o Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aprendendoflask_user:9QkbesYJl3aaFZ5X9vuLPa3d8JskbmEI@dpg-cuja7bl6l47c73a2u2c0-a.oregon-postgres.render.com/aprendendoflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# criando as tabelas do Banco de Dados
db.init_app(app)
migrate = Migrate(app, db)

# Chamadnas as rotas que foram criadas no outro arquivo
app.register_blueprint(prescricoes_bp)

# Configurando para iniciar o projeto
if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080,
        host='0.0.0.0'
        )