from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

def gerar_dados_caldeira():
    dados = {
        'dispositivo': 'Caldeira_01',
        'temperatura': round(random.uniform(150, 200), 2),  # Temperatura em graus Celsius
        'pressao': round(random.uniform(2, 5), 2),  # Pressão em Bar
        'nivel_agua': round(random.uniform(30, 60), 2),  # Nível de água em porcentagem
        'estado': random.choice(['Ligado', 'Desligado']),
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    return dados

@app.route('/dados-caldeira')
def dados_caldeira():
    dados = gerar_dados_caldeira()
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
