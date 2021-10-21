from flask import Flask, request, jsonify
import json

from flask.wrappers import Response

app = Flask(__name__)

tarefas =[
    {
        'id':0,
        'responsavel': 'rafael',
        'tarefa': 'Desenvolvedor Método GET',
        'status': 'concluido'
    },
     {
        'id':1,
        'responsavel': 'lucas',
        'tarefa': 'melhorar o front',
        'status': 'pendente'
    }
]
    #GET, PUT E DELETE DAS TAREFAS
@app.route("/tarefas/<int:id>/", methods = ['GET', 'PUT', 'DELETE'])
    
    
def tarefa(id):
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não existe hein'.format(id)
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    
    elif request.method == 'PUT':
        dados  = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'STATUS': 'SUCESSO', 'MENSAGEM': 'DEVIDAMENTE DELETADO'})

@app.route('/tarefas/', methods = ['POST', 'GET'])

def posta_tarefas():

    if request.method == 'POST':
        dados = json.loads(request.data)
        position = len(tarefas)
        dados['id'] = position
        tarefas.append(dados)
        return jsonify(tarefas[position])

    elif request.method == 'GET':
        return jsonify(tarefas)

@app.route('/status/', methods = ['PUT'])

def altera_status():
    
    tarefas['status'] = json.loads(request.data)

    tarefas[id]['status'] = 'concluido'

if __name__ == '__main__':
    app.run(debug=True)


