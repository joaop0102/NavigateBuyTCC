from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import hashlib
import secrets
from datetime import datetime, timedelta
import binascii

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Configurações do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bdnavigate'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'NavigateBuy')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    reset_token = db.Column(db.String(120))  
    token_expiration = db.Column(db.DateTime) 

    # método de hash para scriptar a senha
    def set_password(self, password):
        salt = os.urandom(16)
        key = hashlib.scrypt(
            password.encode(),
            salt=salt,
            n=16384,
            r=8,
            p=1,
            dklen=64
        )
        self.password = f'scrypt:{binascii.hexlify(salt).decode()}${binascii.hexlify(key).decode()}'

# Rota para solicitar a redefinição de senha
import secrets
from datetime import datetime, timedelta

@app.route('/api/request-password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({"error": "Dados de entrada inválidos."}), 400

    email = data['email']
    user = User.query.filter_by(email=email).first()

    if user:
        token = secrets.token_urlsafe(32)
        expiration = datetime.utcnow() + timedelta(hours=1)
        
        user.reset_token = token
        user.token_expiration = expiration
        db.session.commit()

        return jsonify({"token": token}), 200
    else:
        return jsonify({"error": "Email não encontrado."}), 404

@app.route('/api/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    print(f"Dados recebidos: {data}")  
    
    token = data.get('token')
    new_password = data.get('password')

    if not token or not new_password:
        return jsonify({'error': 'Token e nova senha são obrigatórios.'}), 400  

    user = User.query.filter_by(reset_token=token).first()

    if user and user.token_expiration > datetime.utcnow():
        user.password = new_password  
        user.reset_token = None  
        user.token_expiration = None
        db.session.commit()
        return jsonify({'message': 'Sua senha foi redefinida com sucesso!'}), 200
    else:
        return jsonify({'error': 'Token inválido ou expirado.'}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
