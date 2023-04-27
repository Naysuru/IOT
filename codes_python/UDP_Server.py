# Import des modules sys, socket et random
import sys, socket, random

# Création d'un socket UDP
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Association du socket UDP à l'adresse et au port passés en argument lors du lancement du programme
UDPServerSocket.bind((sys.argv[1], 12345))

# Affichage d'un message pour indiquer que le serveur est en attente de connexion
print("Le serveur UDP attend un connexion ...")

# Initialisation de variables
cli = ""   # adresse IP du client connecté
op1 = 0    # première opérande de l'addition
op2 = 0    # deuxième opérande de l'addition
resu = 0   # résultat de l'addition

# Boucle while pour laquelle le serveur écoute les messages du client
fin = False
while not fin:
    # Attente de la réception d'un message du client
    msgClient, coordClient = UDPServerSocket.recvfrom(1024)
    
    # Vérification si le message reçu est "FIN" pour terminer la boucle
    if msgClient.decode("UTF-8") == "FIN":
        fin=True
    
    # Si aucun client n'est connecté, on enregistre l'adresse IP du client et on génère la première opérande
    if cli == "":
        cli = coordClient
        op1 = random.randint(1, 10)
        UDPServerSocket.sendto(str(op1).encode('UTF-8'), coordClient)
    else :
        # Si la première opérande a déjà été envoyée, on génère la deuxième opérande et on envoie le résultat de l'addition attendu
        if op2 == 0:
            op2 = random.randint(1, 10)
            resu = op1 + op2
            UDPServerSocket.sendto(str(op2).encode('UTF-8'), coordClient)
        else :
            # Si le client envoie la bonne valeur pour le résultat de l'addition, on envoie "Bonne valeur" sinon on envoie "Redo"
            print("somme reçue :"+msgClient.decode("UTF-8"))
            if msgClient.decode("UTF-8") == str(resu) :
                UDPServerSocket.sendto("Bonne valeur".encode('UTF-8'), coordClient)
            else :
                UDPServerSocket.sendto("Redo".encode('UTF-8'), coordClient)
            # Réinitialisation des variables pour une nouvelle opération
            cli = ""
            op1 = 0
            op2 = 0
            resu = 0
            
# Affichage d'un message pour indiquer que le serveur a terminé son exécution
print("Fin du serveur")

# Fermeture du socket UDP
UDPServerSocket.close()
