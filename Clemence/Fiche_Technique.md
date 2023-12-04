# PLAN.MD	03-12-2023
## YNOV BREAKOUT - Python
## Lien repo github : https://github.com/Hapixs/escape_from_ynov

## Equipe :
+ Sarouille Alexandre
- Durand Samy
+ Skander Salim
- Coste Clémence

### Sommaire :

  - Description du projet
  - Problématique
  - Objectifs
  - Solution proposée
  - Valeurs ajoutées
  - Conclusion et perspectives

### Description du projet

Ynov Breakout est un jeu se déroulant dans l'enceinte de l'école d'Ynov Campus Bordeaux, associé a la filière d'informatique. Le but étant de combattre le professeur de Python afin de finir le jeu. Pour cela, il faut augmenter en niveau pour avoir de nouvelles capacités de combtas, de combattre et de trouver certains objets pour avancer dans le jeu. 
Le projet consiste alors a créé en python un jeu lié à un dé et a des choix proposés aux joueurs. 

### Problématique

Quelles innovations peuvent être mises en place sur le nouveau site du serveur ?

### Objectifs

Les objectifs du projet sont :

- La réalisation d’idée pour agrémenter le jeu : objets, nouvelles ataques...
- Utiliser Python pour faire un projet en programmation orienté objet (POO)
- Le respect des regles de la POO
- Créer une histoire logique

Les contraintes rencontrées lors de la conception de ces objectifs sont nombreuses. La charte graphique du client Battle Adventure doit être respecter et l’image ne doit pas être dégradé. De plus les solutions apportées se doivent d’être sécurisé pour tout les utilisateurs afin de ne pas faire fuiter leur donnée personnelle. Enfin les différentes fonctionnalités apportées ne doivent pas être trop gourmande en ressource auquel cas leur bon fonctionnement ne serait pas garanti sur le long terme.

### Solution proposée :

Notre solution comprend plusieurs fonctionnalités innovantes en répondant à la problématique. Pour les fonctionnalités nous en proposons plusieurs qui pourrait faciliter l’expérience utilisateur mais aussi en tant que joueur. On propose un lien informationnel et relationnel entre serveur de jeux et serveur WEB.

- AUTHLINK : permet aux utilisateurs d’utiliser les identifiants du serveur de jeux afin de se connecter au site.
- USERLINK : permet de récupérer toutes les informations d’un joueur (statistiques de jeu, information de l’économie, faction, inventaire, positions connues, …)
- ECOLINK : permet de récupérer les informations de la partie économique du serveur (hôtel de vente, shops, top eco, …)
- FACLINK : permet de récupérer les informations portantes sur les factions et ainsi afficher les listes de faction sur le site, possibilité d’afficher le top faction en fonction de ses filtres ou encore rechercher une faction.

Des fonctionnalités avancées sont donc proposées, celles dites « Link » peuvent travailler entre elles.
USER + FAC LINK : Cette collaboration permet aux joueurs de gérer leurs factions depuis le site (recrutement, gestion du personnelle, position connue, économie, messages)
ECO + USER LINK : Cette collaboration permet aux joueurs de pouvoir interagir avec l’économie depuis le site sans avoir à se connecter.

Ces fonctionnalités « Link » favorisent une meilleur expérience utilisateur pour tous les joueurs de Battle Adventure, de plus elles s’ouvrent à tous les joueurs en leur proposant d’accéder à une multitude d’information sur leur compte/faction sans même se connecter sur le serveur si cela n’est pas possible pour eux. Grace à ce lien informationnel et relationnel entre serveur de jeux et serveur WEB les joueurs de Battle Adventure auront une expérience unique du PvP Faction.

Plus spécifiquement pour le côté WEB un Forum personnalisé est mis à disposition pour les joueurs de tout type. Un forum est idéal pour instaurer le partage entre joueurs. Il permet à certains de poster leurs idées/question et donc à d’autre de s’en instruire, les améliorer et aussi de répondre. Ce dernier porte sur le serveur avec une modération strict mais aussi sur des sujets plus vague sur la thématique de Minecraft. Afin de rendre le forum unique et indispensable aux yeux des joueurs, une gamification y est ajouté, un système de point donné en fonction de réaction sur différents post, mais aussi grâce aux réponses apporter, aux abonnées et aux vues. Cela donnera envie au joueur de participer à l’avancement du projet et à l’entre aide du serveur. Des récompenses en jeux / Boutique peuvent être distribués pour motiver les utilisateurs à participer.
Directement sur le site web de Battle Adventure, des mini jeux compétitifs tous les jours avec un score final en fin de semaine permettent de gagner des points boutique/récompenses en jeux. De plus une roue journalière est disponible pour tous les utilisateurs avec des récompenses, cela donnerait envie aux utilisateurs de se connecter régulièrement sur le site web de Battle Adventure afin de récupérer leurs gains.
Deux autres fonctionnalités innovantes sont disponibles sur le site pour les utilisateurs :
Battle Adventure ADDS : regarder des pubs contre des récompenses en jeux.
Battle Adventure MAP : carte du monde interactive (sans construction de joueur) personnelle/faction permettant de mettre des points et voir les informations récupérer par le USERLINK.

Les technologies utilisées pour la conception de ces fonctionnalités sont : Java, Golang, JavaScript, Figma

### Valeurs ajoutées

Afin de remettre à neuf le serveur, une refonte graphique est proposée tout en restant dans les codes du site web initial.

Sur la page d'accueil un bouton Discord a été ajouter à coté de l'adresse Ip du serveur, à l'heure actuelle il y a près de 175 000 joueurs uniques et seulement 4000 membres sur le discord, en mettant ce dernier plus en évidence les joueurs seront plus aptes à le rejoindre.

Dans la boutique les images ont été changer pour des images plus "lisse" et attrayante.

Grâce au AuthLink les joueurs auront directement un compte sur le site web, cela inciterait les joueurs à s'y rendre plus fréquemment pour gagner en plus de ça diverses récompenses via les différents mini-jeux comme la "Roue de la Fortune" ce qui augmenterait la fréquentation du serveur.

Le EcoLink et donc l'HDV rend l'économie du serveur plus accessible pour les joueurs, pouvoir vendre et acheter librement depuis le site web, grâce à cela il peut y avoir plus d'interaction et cela même en dehors du jeu.
La gestion de la Faction depuis les sites web permet d'inviter des joueurs et de gérer les grades de n'importe où et à n'importe quel moment.

Ces deux solutions rendent également le jeu plus accessible au nouveau joueur qui n'auront pas besoin de connaître toutes les commandes afin d'évoluer dans le jeu.

Le UserLink permet de récupérer les informations d'un joueur ce qui rendra possible la relation entre jeu et site web, le joueur pourra alors consulter tout ce qui est relié de près ou de loin à son compte sur le serveur. Que ce soit sa Faction avec ses membres, ou encore son inventaire, tout sera consultable depuis le site web.

Le FacLink rendra le côté PvP Faction plus innovant et donnera une expérience utilisateur unique car il pourra gérer et/ou consulter sa Faction directement depuis le site web et non forcèment en étant en jeu, ce qui est pratique pour des joueurs qui ne peuvent pas jouer régulièrement ou qui doivent s'absenter. De plus, si un joueur recherche une Faction pour l'intégrer ou savoir combien de Membres et qui la compose, il pourra consulter ces informations depuis le site Web.

Le BA Adds qui permet au utilisateur du site web de regarder des Pubs afin d'avoir des récompenses en jeu, est aussi avantageant pour le client Battle Adventure car il permettra de générer des revenus.

Le BA Map qui est la carte intéractive du monde disponible sur le site web, permet aux joueurs de consulter en direct l'emplacement des membres de leur faction, mais aussi de savoir ou se situe certain biome ou encore les coordonnées de leur home. Du côté du client Battle Adventure, c'est un gros point positif apportant une innovation dans le PvP Faction pour leurs joueurs. Au niveau des ressources cette fonctionnalité ne sera pas trop gourmande car cette map n'est pas générée en continu, elle est générée une seule fois sur un autre serveur afin d'avoir la map du serveur totalement vierge sans construction des joueurs ni des bases des autres.

### Conclusion et perspectives

En conclusion, la proposition pour le projet Battle Adventure représente une avancée significative dans le domaine des serveurs Minecraft PvP Faction. Les objectifs ambitieux visent à offrir une expérience utilisateur novatrice et immersive, tout en respectant les contraintes liées à la charte graphique, à la sécurité des données et à l'efficacité des fonctionnalités.

Les fonctionnalités "Link" proposées, telles qu'AUTHLINK, USERLINK, ECOLINK et FACLINK, établissent un lien crucial entre le serveur de jeu et le site web, offrant ainsi aux joueurs un accès aisé à une multitude d'informations sur leur compte et leur faction. Cette approche favorise une expérience utilisateur améliorée et ouverte à tous les joueurs, qu'ils soient connectés ou non au serveur.

Le forum personnalisé gamifié constitue un espace d'échange dynamique, propice au partage d'idées et à l'entraide au sein de la communauté. Les mini-jeux compétitifs et la roue journalière sur le site web renforcent l'engagement des utilisateurs et stimulent la fréquentation.

En termes de valeur ajoutée, la refonte graphique et l'ajout du bouton Discord sur la page d'accueil visent à renforcer la visibilité du serveur et à encourager la participation active des joueurs. Les améliorations apportées à la boutique ainsi que les fonctionnalités EcoLink et la gestion de Faction depuis le site web simplifient l'expérience des joueurs et élargissent l'accessibilité du jeu.

Dans l'ensemble, ces propositions innovantes promettent une évolution remarquable pour Battle Adventure. Elles visent à créer une communauté plus engagée et à offrir une expérience de jeu exceptionnelle à une audience toujours plus nombreuse. Avec ces améliorations, le projet est bien positionné pour atteindre de nouveaux sommets et consolider sa position de leader dans le monde des serveurs Minecraft PvP Faction.