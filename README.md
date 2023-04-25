# **Projet IOT**



<a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="Etapes de réalisation">Préparer les M5</a>
      <ul>
        <li><a href="#built-with">Capteur de présence</a></li>
		<li><a href="#built-with">Capteur de lumière</a></li>
		<li><a href="#built-with">Capteur de couleur</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Préparer le broker</a>
      <ul>
        <li><a href="#prerequisites">Serveur HTTP</a></li>
        <li><a href="#installation">Bot Telegram</a></li>
		<li><a href="#installation">Serveur UDP</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


# **Le projet:**

## 1. Préparer les M5
___
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

## 2. Préparer le broker
___
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

## 3. Capteur packet:
___
Pour rester dans le thème système IOT domotique:
- lumières à allumer éteindre + changer de couleur
- télévision à controller
- porte de garage
- etc... (*Le tout doit etre pilotable sur le frontend web et depuis telegram*)


<!-- CONTACT -->
# Contact
___
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