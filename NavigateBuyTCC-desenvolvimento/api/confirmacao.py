from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type"]}}, supports_credentials=True)

# Configurações do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/bdnavigate'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'NavigateBuy')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class ConfirmationCode(db.Model):
    __tablename__ = 'confirmations'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(6), nullable=False)

# Função para enviar o email
def enviar_email(destinatario, assunto, corpo):
    remetente = "navigatebuy@gmail.com"
    senha = "k o s b x c h h z cu y y t y t"

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    
    # Garantir que o corpo do e-mail esteja em UTF-8
    corpo_email = MIMEText(corpo.encode('utf-8'), 'html', 'utf-8')
    msg.attach(corpo_email)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(remetente, senha)
            server.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Rota para enviar o código de confirmação
@app.route('/api/send_code', methods=['OPTIONS', 'POST'])
def send_code():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"error": "E-mail é obrigatório."}), 400
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "E-mail não encontrado."}), 404
    # Gerar o código de confirmação
    code = str(random.randint(100000, 999999))
    existing_code = ConfirmationCode.query.filter_by(email=email).first()
    if existing_code:
        existing_code.code = code
    else:
        new_code = ConfirmationCode(email=email, code=code)
        db.session.add(new_code)
    db.session.commit()
    # Enviar o código por e-mail
    corpo_email = f"""
    <h3>Código de Confirmação</h3>
    <p>Seu código de confirmação é: <strong>{code}</strong></p>
    <p>Use este código para confirmar o seu e-mail.</p>
    """
    enviar_email(email, "Código de Confirmação - Navigate Buy", corpo_email)
    return jsonify({"message": "Código de confirmação enviado para o seu e-mail."}), 200

# Rota para confirmar o código
@app.route('/api/confirm_code', methods=['POST'])
def confirm_code():
    data = request.get_json()
    email = data.get('email')
    code = data.get('code')

    if not email or not code:
        return jsonify({"error": "Dados insuficientes."}), 400

    confirmation = ConfirmationCode.query.filter_by(email=email, code=code).first()

    if confirmation:
        # Remover o código após confirmação bem-sucedida
        db.session.delete(confirmation)
        db.session.commit()
        return jsonify({"message": "Código confirmado com sucesso."}), 200
    else:
        return jsonify({"error": "Código de confirmação inválido."}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)
