import socket

# , protocolo de datagrama
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, )

print("client socket criado com sucesso")

host = 'localhost'
port = 5050

menssagem = 'olá mundo do UDP'

try:
    print(f'cliente: {menssagem}')
    s.sendto(menssagem.encode(),(host, port))
    
    dados,servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'client: {dados}')
finally:
    print('cliente: fechando a conexão')
    s.close()