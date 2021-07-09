# Campus_Contest_POO
Last Campus Contest 2020-2021 by Clément Raulin, B2 DEV.


LANCEMENT DE L'APPLICATION :

Pour télécharger les librairies nécessaires au bon fonctionnement de l'application, exécuter dans le terminal la commande : pip install uuid

Pour lancer l'application, exécuter le fichier main.py.


EXPLICATIONS :

Sur ce TD, je n'ai pas eu le temps de m'atteler à la limite de taille et à la complétion des fonctions sur les transactions. J'ai pu cependant faire des Wallets complets et fonctionnels ainsi que des Blocs fonctionnels, cependant pour le moment, un seul hash est présent dans un Block. Ce hash détient bien un hash, un hash parent et sa chaine de caractère avant qu'il ne soit hashé.

Au lancement de l'application, on crée Deux Wallets qui intéragissent entre eux. Etant écrit dans le dur, le code ne permet qu'une interaction qui transfère 3 unités du wallet 1 au wallet 2. Le code affiche tous les hash ressortis, et il ne garde que ceux qui commencent par 0000 et qui n'existent pas déjà, pour éviter que le temps d'exécution soit trop long, je limite le nombre de hash à 5.

Je n'ai malheureusement pas eu le temps de finir ce TP pourtant très intéressant, mais qui m'a demandé beaucoup de temps de compréhension (je n'y connaissais rien en Blockchain jusque la)