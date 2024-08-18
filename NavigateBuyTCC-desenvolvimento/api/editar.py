from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuração do CORS
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "OPTIONS"], "supports_credentials": True}})

# Configurações do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bdnavigate'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'NavigateBuy') 
app.config['SESSION_COOKIE_SECURE'] = False  
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        print(f"Usuário {user.id} autenticado e sessão criada.")
        return jsonify({'message': 'Login realizado com sucesso!'}), 200
    else:
        return jsonify({'error': 'Email ou senha incorretos.'}), 401

@app.route('/api/perfil', methods=['GET'])
def get_perfil():
    if 'user_id' not in session:
        return jsonify({'error': 'Usuário não autenticado.'}), 401

    user = User.query.get(session['user_id'])
    if user:
        return jsonify({
            'username': user.username,
            'email': user.email
        }), 200
    return jsonify({'error': 'Usuário não encontrado.'}), 404

@app.route('/api/perfil', methods=['POST'])
def editar_perfil():
    if 'user_id' not in session:
        return jsonify({'error': 'Usuário não autenticado.'}), 401

    user = User.query.get(session['user_id'])
    if not user:
        return jsonify({'error': 'Usuário não encontrado.'}), 404

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if username and username != user.username:
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Nome de usuário já em uso.'}), 400
        user.username = username

    if email and email != user.email:
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email já em uso.'}), 400
        user.email = email

    if password:
        user.set_password(password)

    db.session.commit()
    return jsonify({'message': 'Perfil atualizado com sucesso!'}), 200

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout realizado com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)