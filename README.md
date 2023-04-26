# **Projet IOT**



<a href="https://github.com/Takeapill/IOT"><strong>Explore the docs »</strong></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#m5-stack">M5 Stack</a>
      <ul>
        <li><a href="#capteur-de-présence">Capteur de présence</a></li>
		<li><a href="#capteur-de-lumière">Capteur de lumière</a></li>
		<li><a href="#capteur-de-couleur">Capteur de couleur</a></li>
      </ul>
    </li>
    <li>
      <a href="#broker">Broker</a>
      <ul>
        <li><a href="#serveur-http">Serveur HTTP</a></li>
        <li><a href="#bot-telegram">Bot Telegram</a></li>
		<li><a href="#serveur-udp">Serveur UDP</a></li>
      </ul>
    </li>
    <li><a href="#log-management">Log Management</a></li>
    <li><a href="#packet-tracer">Packet Tracer</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


# **Le projet:**

## M5 Stack
- ### Capteur de présence:
	- A chaque changement d'état, le capteur envoie l'information +
	- *Activer une alarme lorsqu'une présence est detecté*
- ### Capteur de lumière: 
	- Changements d'état + 
	- *Query pour connaitre l'état actuel* 
- ### Capteur de couleur: 
	- Changements d'état + 
	- *Query pour connaitre l'état actuel*

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Broker
### Serveur HTTP:
- Permettre l'affichage des logs de présence et de l'état de la lumière. 
- Gérer la lumière (couleur, allumé/éteint)
- Fonctionnalité supplémentaire: Afficher tous les logs, modifier certaines options.


### [Bot Telegram](t.me/HEGProjetCo_bot)
- Créer un bot telegram (java ou python?) qui affichera les changements d'état de présence 
et permettra de controler la lumière /lumiere (Bouttons éteindre/allumer), 
pour gérer la couleur créer une commande /couleur 


### Serveur UDP:
- Communication avec un une autre vm contenant packet tracer
- A définir: Sous quelle forme envoyer les informations


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Packet Tracer
### Pour rester dans le thème système IOT domotique:
- lumières à allumer éteindre + changer de couleur
- télévision à controller
- porte de garage
- etc... (*Le tout doit etre pilotable sur le frontend web et depuis telegram*)


## Log Management
### Afin de gérer les logs:
 - Installation de mongodb-org
 - Installation de OpenSearch
 - Installation de GrayLog pour le log management

 - *Les logs doivent comprendre **tous** les changements d'états*


<!-- CONTACT -->
# Contact
Mathis Bourinet - mathis.bourinet@hes-so.ch

Kenan Henzelin - kenan.henzelin@hes-so.ch


Julien Frey - julien.frey@hes-so.ch 

Project Link: [https://github.com/Takeapill/IOT](https://github.com/Takeapill/IOT)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>