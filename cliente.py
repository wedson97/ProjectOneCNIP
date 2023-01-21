import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555
ADDR = (HOST, PORT)


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
            c.connect((HOST, PORT))
            print(f' <CONECTADO> Cliente conectado ao server {HOST}:{PORT}')
            print(""" <SERVER>
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
        ************************************************************************* """)

            conectado = True
            while conectado:
                try:
                    msg = input(">>> ")
                    if msg == '':
                        print(" Conexão Perdida! ")
                        break
                    c.send(msg.encode('utf-8'))

                    if msg.lower() == 'sair':
                        msg = c.recv(2048).decode('utf-8')
                        print(f" <SERVER> {msg}")
                        conectado = False
                    elif msg.lower() == 'cep':
                        msg2 = str(input('Digite o cep: '))
                        c.send(msg2.encode('utf-8'))
                        msg2 = c.recv(2048).decode('utf-8')
                        print(f' <SERVER> {msg2}')
                    else:
                        msg = c.recv(2048).decode('utf-8')
                        print(f" <SERVER> {msg}")
                except:
                    print(" Desconectado do servidor")
                    conectado = False
    except:
        print(" Não foi possivel conectar ao servidor")


if __name__ == '__main__':
    main()
