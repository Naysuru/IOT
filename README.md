# Etapes de réalisation du projet IOT:

## 1. Préparer les M5:
	idées: activer une alarme lorsqu'une présence est detecté
	A. Capteur de présence: A chaque changement d'état, le capteur envoie l'information
	B. Capteur de lumière: Same than A + Query pour connaitre l'état actuel
	C. Capteur de couleur: Same than B


## 2. Préparer le broker (Machine Kenan_Ubuntu_IOT; log: User=? passwd=julienlpbdu69)
	A. Serveur HTTP:
		But: permettre l'affichage des logs de présence et de l'état de la lumière. 
		Gérer la lumière (couleur, allumé/éteint)
		Fonctionnalité supplémentaire: Afficher tous les logs, modifier certaines options.


	B. Telegram (Bot=t.me/HEGProjetCo_bot token=6065858871:AAHjrJiUkfzCn0tcn2JP0Y5lysmpHjhT35w):
		Créer un bot telegram (java ou python?) qui affichera les changements d'état de présence 
		et permettra de controler la lumière /lumiere (Bouttons éteindre/allumer), 
		pour gérer la couleur créer une commande /couleur 

	C. Serveur UDP:
		Communication avec un une autre vm contenant packet tracer
		A définir: Sous quelle forme envoyer les informatiosn

## 3.	Capteur packet:
	Idées: pour rester dans le thème système IOT domotique avec:
		lumières à allumer éteindre + changer de couleur
		télévision à controller
		porte de garage
		etc.
		Le tout doit etre controlables sur le frontend web et par telegram



### Codes disponibles dans le git:
	
	-Serveur MQTT et UDP