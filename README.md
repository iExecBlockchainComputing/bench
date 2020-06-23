# bench
L'outil se compose de 3 onglets qui se complète.

## Wallet Manager
Permet la creation de wallet et leurs stockage.
Le mainWallet sera celui du MOC pour le déploiement de POA et les autres seront pour les validateurs.

Il est possible de sauvegarder une configuration de wallets vie le bouton "Export Wallets".
Les wallets sauvegardés se trouve dans `server/wallets/` et il est possible de recharger la configuration avec le bouton Reload Configuration en haut à droite.

## PoA Network
Permet de générer une configuration PoA Network pour lancer X noeuds d'une blockchain PoA.
Utilisable sur n'importe quel infrastructure qui permet d'utiliser ansible.

Il est important d'avoir la configuration des wallets chargée avant de générer la config.

/!\ recharger la page réinitialise les données de l'application, il faut donc "reload configuration" avec un rafraichissement de page web.

Le champs "validators nodes ip" doit être rempli sous le format suivant: ip,ip

## Scenario Creator
Permet de générer des scénarios de tests selon plusieurs templates.

On choisis le type de scénario et à quel moment il se lance puis on ajoute l'évènement.
A droite se trouve le résumé des scénario qui permet de configurer plus finement les évènements en cliquant dessus.

Un code python est généré coté serveur pour lancer les tests.

## Comment ça marche ?

### Démarrer le logiciel
`npm i` dans `client` et `server` puis `npm start` dans `client` et `server`.

### Lancer le déploiement
Pour lancer le déploiement il faut:
- Avoir préparé les wallet (ou juste reload la configuration)
- Avoir généré les fichiers de configuration de PoA.

Quand c'est fait il faut envoyer le dossier `server/repos/poa-deployement-bench/` sur une machine qui pourra accéder aux machines qui feront tourner les noeuds.
Cette machine doit avoir ansible et une clée ssh nommé bench qu'il faudra passer aux autres machines (kadeploy permet ça au lancement)

Quand c'est fait, lancer `ansible-playbook -i hosts site.yml` et la chaine se déploie automatiquement.