import sys, socket, random
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((sys.argv[1], 12345))
print("Le serveur UDP attend un connexion ...")
cli = ""
op1 = 0
op2 = 0
resu = 0

fin = False
while not fin:
    msgClient, coordClient = UDPServerSocket.recvfrom(1024)
    if msgClient.decode("UTF-8") == "FIN":
        fin=True
    if cli == "":
        cli = coordClient
        op1 = random.randint(1, 10)
        UDPServerSocket.sendto(str(op1).encode('UTF-8'), coordClient)
    else :
        if op2 == 0:
            op2 = random.randint(1, 10)
            resu = op1 + op2
            UDPServerSocket.sendto(str(op2).encode('UTF-8'), coordClient)
        else :
            print("somme reçue :"+msgClient.decode("UTF-8"))
            if msgClient.decode("UTF-8") == str(resu) :
                UDPServerSocket.sendto("Bonne valeur".encode('UTF-8'), coordClient)
            else :
                UDPServerSocket.sendto("Redo".encode('UTF-8'), coordClient)
            cli = ""
            op1 = 0
            op2 = 0
            resu = 0
            
print("Fin du serveur")
UDPServerSocket.close()