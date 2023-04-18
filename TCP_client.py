import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("10.136.1.27", 65432))
print ("Connexion ouverte")

for i in range(1,5):
    print ("Envoi "+str(i))
    socket.sendall(str(i).encode("UTF-8"))
    print(socket.recv(1024).decode("UTF-8"))
socket.send(b"")
print("Fermeture connexion")
socket.close()