# bench
L'outil se compose de 3 onglets qui se complètent.

## Wallet Manager
Permet la creation de wallet et leurs stockage.
Le mainWallet sera celui du MOC pour le déploiement de POA et les autres seront pour les validateurs.

Il est possible de sauvegarder une configuration des wallets via le bouton "Export Wallets".
Les wallets sauvegardés se trouvent dans `server/wallets/` et il est possible de recharger la configuration avec le bouton "Reload Configuration" en haut à droite.

## PoA Network
Permet de générer une configuration PoA Network pour lancer X noeuds d'une blockchain PoA.
Utilisable sur n'importe quel infrastructure qui permet d'utiliser ansible.

Il est important d'avoir la configuration des wallets chargée avant de générer la config.

/!\ recharger la page réinitialise les données de l'application, il faut donc "reload configuration" après un rafraichissement de page web.

Le champs "validators nodes ip" doit être rempli sous le format suivant: ip,ip

## Scenario Creator
Permet de générer des scénarios de test selon plusieurs templates.

On choisis le type d'évènement et à quel moment il se lance puis on ajoute l'évènement grâce au bouton.
A droite se trouve le scénario et permet de configurer plus finement les évènements en cliquant dessus.

Un code python est généré coté serveur pour lancer les tests dans `server/scenario/`

## Comment ça marche ?

### Démarrer le logiciel
`npm i` dans `client` et `server` puis `npm start` dans `client` et `server`.

### Lancer le déploiement
Pour lancer le déploiement il faut:
- Avoir préparé les wallets (ou juste reload la configuration)
- Avoir généré les fichiers de configuration de PoA.

Quand c'est fait il faut envoyer le dossier `server/repos/poa-deployement-bench/` sur une machine qui pourra accéder aux machines qui feront tourner les noeuds.
Cette machine doit avoir ansible et une clée ssh nommée bench qu'il faudra passer aux autres machines (kadeploy permet ça au lancement)

Quand c'est fait, lancer `ansible-playbook -i hosts site.yml` et la chaine se déploie automatiquement.