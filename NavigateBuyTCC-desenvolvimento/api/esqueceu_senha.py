from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Configurações do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bdnavigate'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'sua_chave_secreta')

# Inicializar o SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Rota para solicitar a redefinição de senha
@app.route('/api/request-password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()

    if not data or 'email' not in data:
        return jsonify({"error": "Dados de entrada inválidos."}), 400

    email = data['email']
    user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({"message": "Usuário encontrado. Pode prosseguir para redefinir a senha."}), 200
    else:
        return jsonify({"error": "Email não encontrado."}), 404

# Rota para redefinir a senha
@app.route('/api/reset_password/<int:user_id>', methods=['POST'])
def reset_password(user_id):
    user = User.query.get(user_id)
    
    if user:
        data = request.get_json()  
        new_password = data.get('password')
        
        if new_password:
            user.set_password(new_password)
            db.session.commit()
            return jsonify({'message': 'Sua senha foi redefinida com sucesso!'}), 200
        else:
            return jsonify({'error': 'A nova senha não pode estar vazia.'}), 400
    else:
        return jsonify({'error': 'Usuário não encontrado.'}), 404
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)