from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#criar lista de desenvolvedores
desenvolvedores = [
    {'id': '0',
    'nome': 'Rafael',
    'habilidades': ['Python', 'Flask']
    },
    {'id': '1',
     'nome': 'Rosana',
     'habilidades': ['Python', 'Django']
     }
]

#devolve um desenvolvedor pelo id, tb altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro',
                        'mensagem': 'Desenvolvedor de ID {} não existe'.format(id)}
        except Exception:
            response = {'status': 'erro',
                        'mensagem': 'Erro desconhecido. Procure o administrador da API'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados) #alterei o registro
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})

#lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    #e agora vamos consultar todos os desenvolvedores
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)