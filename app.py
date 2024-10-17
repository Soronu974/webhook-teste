from flask import Flask, request, jsonify

app = Flask(__name__)

# Cardápio
menu = {
    "Comidas": {
        "Bacon com ovos": 8.59,
        "Pão com manteiga": 6.5,
        
    },
    "Bebidas": {
        "Achocolatado": 8,
        "Suco Natural": 10,
        
    }
}

def calcular_total(pedido):
    total = 0
    for item, detalhes in pedido.items():
        preco = menu[detalhes['categoria']][item]
        total += preco * detalhes['quantidade']
    return total

@app.route('/calcular', methods=['POST'])
def calcular_pedido():
    pedido = request.get_json()
    total = calcular_total(pedido)
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(debug=True)