from flask import Flask, jsonify
import random

app = Flask(__name__)

charadas = [
    {'id': 1, 'charada': 'O que é, o que é? Tem olhos, mas não pode ver.', 'resposta': 'O cego'},
    {'id': 2, 'charada': 'O que é, o que é? Quanto mais se tira, maior fica.', 'resposta': 'O buraco'},
    {'id': 3, 'charada': 'O que é, o que é? Sempre cai em pé e corre deitado.', 'resposta': 'A chuva'},
    {'id': 4, 'charada': 'O que é, o que é? Tem dentes, mas não morde.', 'resposta': 'O pente'},
    {'id': 5, 'charada': 'O que é, o que é? Anda com os pés na cabeça.', 'resposta': 'O piolho'},
    {'id': 6, 'charada': 'O que é, o que é? Fica cheio durante o dia e vazio à noite.', 'resposta': 'O sapato'},
    {'id': 7, 'charada': 'O que é, o que é? É feito para andar e não anda.', 'resposta': 'A rua'},
    {'id': 8, 'charada': 'O que é, o que é? Tem asas, mas não voa; tem bico, mas não bica.', 'resposta': 'O bule'},
    {'id': 9, 'charada': 'O que é, o que é? Tem um rio, mas não tem água.', 'resposta': 'O mapa'},
    {'id': 10, 'charada': 'O que é, o que é? Dá muitas voltas e não sai do lugar.', 'resposta': 'O relógio'},
    {'id': 11, 'charada': 'O que é, o que é? Corre, mas não tem pernas.', 'resposta': 'O rio'},
    {'id': 12, 'charada': 'O que é, o que é? Tem cabeça e tem dente, mas não é bicho nem gente.', 'resposta': 'O alho'},
    {'id': 13, 'charada': 'O que é, o que é? Tem pescoço, mas não tem cabeça.', 'resposta': 'A garrafa'},
    {'id': 14, 'charada': 'O que é, o que é? Sobe, mas nunca desce.', 'resposta': 'A idade'},
    {'id': 15, 'charada': 'O que é, o que é? Fica no meio do céu.', 'resposta': 'A letra "e"'},
    {'id': 16, 'charada': 'O que é, o que é? Quanto mais quente, mais fresco é.', 'resposta': 'O pão'},
    {'id': 17, 'charada': 'O que é, o que é? Não é doce, mas todos dizem que é.', 'resposta': 'O sal'},
    {'id': 18, 'charada': 'O que é, o que é? Tem coroa, mas não é rei.', 'resposta': 'O abacaxi'},
    {'id': 19, 'charada': 'O que é, o que é? Tem chave, mas não abre.', 'resposta': 'O teclado'},
    {'id': 20, 'charada': 'O que é, o que é? Dá uma volta em torno do sol em um ano.', 'resposta': 'A Terra'},
    {'id': 21, 'charada': 'O que é, o que é? Está sempre na frente do trem.', 'resposta': 'A letra "t"'},
    {'id': 22, 'charada': 'O que é, o que é? Não tem asas, mas pode voar.', 'resposta': 'O avião'},
    {'id': 23, 'charada': 'O que é, o que é? Fica menor quando está de pé e maior quando deitado.', 'resposta': 'O número 8'},
    {'id': 24, 'charada': 'O que é, o que é? Tem patas, mas não anda.', 'resposta': 'A mesa'},
    {'id': 25, 'charada': 'O que é, o que é? Sempre quebra, mas nunca cai.', 'resposta': 'A onda'},
    {'id': 26, 'charada': 'O que é, o que é? Tem um pé, mas não anda.', 'resposta': 'A letra "p"'},
    {'id': 27, 'charada': 'O que é, o que é? Tem barba, mas não é homem.', 'resposta': 'O milho'},
    {'id': 28, 'charada': 'O que é, o que é? Tem orelha, mas não ouve.', 'resposta': 'A espiga de milho'},
    {'id': 29, 'charada': 'O que é, o que é? Tem coroa, mas não é rei.', 'resposta': 'O dente'},
    {'id': 30, 'charada': 'O que é, o que é? Tem bico e não é ave.', 'resposta': 'O bule'},
    {'id': 31, 'charada': 'O que é, o que é? Tem folha, mas não é árvore.', 'resposta': 'O livro'},
    {'id': 32, 'charada': 'O que é, o que é? Tem cabeça, mas não pensa.', 'resposta': 'O prego'},
    {'id': 33, 'charada': 'O que é, o que é? Tem forma de peixe, mas não nada.', 'resposta': 'A chave'},
    {'id': 34, 'charada': 'O que é, o que é? Tem letra, mas não escreve.', 'resposta': 'A placa'},
    {'id': 35, 'charada': 'O que é, o que é? Tem vidro, mas não se vê através.', 'resposta': 'A lâmpada'},
    {'id': 36, 'charada': 'O que é, o que é? Pode ser de sol, mas não esquenta.', 'resposta': 'O girassol'},
    {'id': 37, 'charada': 'O que é, o que é? Vive caindo, mas nunca se machuca.', 'resposta': 'A chuva'},
    {'id': 38, 'charada': 'O que é, o que é? Tem cabeça e passa o dia correndo.', 'resposta': 'O prego'},
    {'id': 39, 'charada': 'O que é, o que é? Tem casco, mas não é tartaruga.', 'resposta': 'A garrafa'},
    {'id': 40, 'charada': 'O que é, o que é? Tem linha, mas não costura.', 'resposta': 'O telefone'},
    {'id': 41, 'charada': 'O que é, o que é? Dá voltas, mas não sai do lugar.', 'resposta': 'A roda'},
    {'id': 42, 'charada': 'O que é, o que é? Anda devagar, mas nunca para.', 'resposta': 'O tempo'},
    {'id': 43, 'charada': 'O que é, o que é? Tem braços, mas não abraça.', 'resposta': 'A cruz'},
    {'id': 44, 'charada': 'O que é, o que é? Tem luz, mas não brilha.', 'resposta': 'O vaga-lume'},
    {'id': 45, 'charada': 'O que é, o que é? Tem corda, mas não amarra.', 'resposta': 'O violão'},
    {'id': 46, 'charada': 'O que é, o que é? Anda sem pernas.', 'resposta': 'O tempo'},
    {'id': 47, 'charada': 'O que é, o que é? Se quebra quando se fala.', 'resposta': 'O segredo'},
    {'id': 48, 'charada': 'O que é, o que é? Tem folha, mas não é planta.', 'resposta': 'O papel'},
    {'id': 49, 'charada': 'O que é, o que é? Tem raiz, mas não é árvore.', 'resposta': 'A equação'},
    {'id': 50, 'charada': 'O que é, o que é? Quanto mais quente, mais fresco fica.', 'resposta': 'O pão'}
]



@app.route('/')
def index():
    return 'api on fire 💥'

@app.route('/charadas', methods=['GET'])
def lista():
    return jsonify(charadas), 200

@app.route('/charadas/id/<int:id>', methods=['GET'])
def busca(id):
    for charada in charadas:
        if charada['id'] == id:
            return jsonify(charada), 200
    else:
        return jsonify({'mensagem': 'Erro. charada não encontrada'}), 404

@app.route('/charadas/aleatoria', methods=['GET'])
def aleatoria():
    charada = random.choice(charadas)
    return jsonify(charada), 200

if __name__ == '__main__':
    app.run(debug=True)


    
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