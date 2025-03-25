
#from flask import Flask, jsonify

#app = Flask(__name__)

#usuarios = [
    #{'id': 1, 'nome': 'pietro', 'cpf': '123456789'},
    #{'id': 2, 'nome': 'richard', 'cpf': '222222222'},
    #{'id': 3, 'nome': 'thimotio', 'cpf': '33333333'},
    #{'id': 4, 'nome': 'matheus', 'cpf': '44444444'},
    #{'id': 5, 'nome': 'pedro', 'cpf': '555555555'}
    
#]

#@app.route('/')
#def index():
    #return 'api on fire 💥'


#@app.route('/usuarios', methods=['POST'])
#def lista():
    #return jsonify(usuarios), 200

#@app.route('/usuarios/<campo>/<busca>', methods=['GET'])
#def busca(campo, busca):
    

    #if campo not in ['id','nome','cpf']:
        #return jsonify ({'mensagem': 'erro. campo não encontrado'}), 404

    #if campo == 'id':
        #busca = int(busca)
    

    #for usuario in usuarios:
        #if usuario[campo] == busca:
            #return jsonify(usuario), 200
    #else:
        #return jsonify({'mensagem': 'Erro. Usuário não encontrado'}), 404

#if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000) 