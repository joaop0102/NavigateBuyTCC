from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Configurar conexão com o banco de dados
def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='bdnavigate',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Função para enviar o e-mail de confirmação
def send_confirmation_email(email, code):
    sender_email = os.getenv('EMAIL_USER')
    sender_password = os.getenv('EMAIL_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Código de Confirmação'

    body = f'Seu código de confirmação é: {code}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')

# Rota para enviar o código de confirmação
@app.route('/api/send_code', methods=['POST'])
def send_code():
    data = request.json
    email = data.get('email')

    if email:
        # Verificar se o e-mail está cadastrado
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM users WHERE email=%s'
                cursor.execute(sql, (email,))
                user = cursor.fetchone()

                if not user:
                    return jsonify(message='E-mail não encontrado.'), 400

                code = random.randint(100000, 999999)  # Gerar código de confirmação
                send_confirmation_email(email, code)

                # Armazenar o código de confirmação no banco de dados
                sql = 'INSERT INTO confirmations (email, code) VALUES (%s, %s)'
                cursor.execute(sql, (email, code))
                connection.commit()

                return jsonify(message='Código de confirmação enviado para o seu e-mail.'), 200
        finally:
            connection.close()
    return jsonify(message='E-mail é obrigatório.'), 400

# Rota para confirmar o código
@app.route('/api/confirm_code', methods=['POST'])
def confirm_code():
    data = request.json
    email = data.get('email')
    code = data.get('code')

    if email and code:
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM confirmations WHERE email=%s AND code=%s'
                cursor.execute(sql, (email, code))
                confirmation = cursor.fetchone()

                if confirmation:
                    # Remover o código após confirmação bem-sucedida
                    sql = 'DELETE FROM confirmations WHERE email=%s AND code=%s'
                    cursor.execute(sql, (email, code))
                    connection.commit()
                    return jsonify(message='Código confirmado com sucesso.'), 200
                else:
                    return jsonify(message='Código de confirmação inválido.'), 400
        finally:
            connection.close()
    return jsonify(message='Código de confirmação inválido.'), 400

if __name__ == '__main__':
    app.run(port=5000)