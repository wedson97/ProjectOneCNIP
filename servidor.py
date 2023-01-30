import socket
import threading
import requests
import json

# """
#   Projeto #1 - Sockets
#   Grupo:  Wedson Cândido da Silva
#           Yagor Kalenieves
# """

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (HOST, PORT)


def handle_client(conn, addr, s):
    with conn:
        print(f'<NOVA CONEXÃO> {addr} conectado')
        conectado = True
        while conectado:
            try:
                data = conn.recv(2048).decode('utf-8')
                print(f'<{addr}> {data}')
                msg = ''
                if data.lower() == 'sair':
                    conectado = False
                    print(f'<CONEXÃO> {addr} desconectou')
                    msg = f'{addr} desconectou'
                elif data.lower() == 'fechar':
                    print(f'<SISTEMA> {addr} Tentou finalizar servidor')
                    print(f'<CONEXÃO> {addr} desconectou')
                    print(
                        f'<SISTEMA> Servidor irá fechar quando não houver mais conexões')
                    msg = "Conexão com o servidor interrompida. Digite <sair>"
                    s.close()
                    conectado = False

                elif data.lower() == 'dolar':
                    cotacao = requests.get(
                        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
                    cotacao = cotacao.json()
                    dolar = float(cotacao['USDBRL']["bid"])
                    msg = f'Dolar USD 1,00 = BRL R$ {dolar:.2f}\n'
                elif data.lower() == 'euro':
                    cotacao = requests.get(
                        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
                    cotacao = cotacao.json()
                    euro = float(cotacao['EURBRL']["bid"])
                    msg = f'Euro EUR 1,00 = BRL R$ {euro:.2f}\n'
                elif data.lower() == 'bitcoin':
                    cotacao = requests.get(
                        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
                    cotacao = cotacao.json()
                    bitcoin = float(cotacao['BTCBRL']["bid"])
                    msg = f'Bitcoin BTC 1,00 = BRL R$ {bitcoin:.2f}\n'
                elif data.lower() == 'cep':
                    datacep = conn.recv(2048).decode('utf-8')
                    print(f'<{addr}> CEP: {datacep}')
                    busca = requests.get(
                        'https://cep.awesomeapi.com.br/json/'+datacep)
                    busca = busca.json()
                    try:
                        estado = busca['state']
                        cidade = busca['city']
                        bairro = busca['district']
                        rua = busca['address']
                        msg = f"""CEP: {datacep} || Estado: {estado}
                           Cidade: {cidade}
                           Bairro: {bairro} 
                           {rua}"""
                    except:
                        msg = f'Não foi possivel localizar o cep informado'
                else:
                    msg = """
        *************************************************************************
        ***                                                                   ***
        ***   Para desconectar digite: <sair>                                 ***
        ***   Para ver a cotação do dolar digite: <dolar>                     ***
        ***   Para ver a cotação do euro digite: <euro>                       ***
        ***   Para ver a cotacação do Bitcoin digite : <bitcoin>              ***
        ***   Para pesquisar um Cep digite: <cep>                             ***
        ***   Para fechar o server digite: <fechar>                           ***
        ***    Obs: Servidor irá finalizar quando não houver mais conexões    ***
        ***                                                                   ***
        ************************************************************************* """
                conn.send(msg.encode('utf-8'))
            except:
                print(f'<CONEXÃO> {addr} perdeu conexão')
                conectado = False


print("<INICIANDO> Servidor iniciando...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()
print(f'<CONEXÃO> Servidor aguardando conexões em {HOST}:{PORT}')

while True:
    try:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, s))
        thread.start()
        print('< CONEXÕES >', threading.active_count() - 1)

    except:
        break
