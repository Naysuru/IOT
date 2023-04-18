import socket
TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerSocket.bind(('192.168.100.28', 65432))
TCPServerSocket.listen(1)
while True:
    print('Attente de connexion')
    connexion, addr = TCPServerSocket.accept()
    fin=False
    while not fin:
        donnees = connexion.recv(1024).decode("UTF-8")
        if donnees != "":
            print(donnees)
            connexion.sendall(("réponse: "+donnees).encode('UTF-8'))
        else:
            print('Fin de connexion')
            fin=True
    connexion.close()
TCPServerSocket.close()