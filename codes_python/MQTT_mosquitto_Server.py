# Import de la bibliothèque Paho MQTT, time et keyboard
import paho.mqtt.client as mqtt
import time
import keyboard

# Définition d'une fonction callback qui sera appelée chaque fois qu'un message est reçu sur le topic abonné
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

# Définition de l'adresse IP du broker MQTT
broker_address="192.168.X.Y"

# Création d'une nouvelle instance du client MQTT
print("creation de la nouvelle instance")
client = mqtt.Client("client1") 

# Association de la fonction callback "on_message" au client MQTT
client.on_message=on_message 

# Connexion du client MQTT au broker MQTT et démarrage de la boucle de réception des messages
print("connection au broker")
client.connect(broker_address) 
client.loop_start()

# Abonnement du client MQTT au topic "salon/temp"
print("Inscription au topic","salon/temp")
client.subscribe("salon/temp")

# Boucle while pour laquelle l'utilisateur doit appuyer sur la touche "q" pour terminer le programme
fin = False
while fin == False:  
    if keyboard.is_pressed('q'):  
        print('On a fini!')
        fin = True
    #ToDo----------
    #FinToDo----------

# Arrêt de la boucle de réception des messages
client.loop_stop()
