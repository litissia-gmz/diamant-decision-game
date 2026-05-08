# Simulation d'Environnement Décisionnel - Jeu Diamant

Ce projet, réalisé dans le cadre de la Licence Informatique à l'Université d'Angers, consiste en la modélisation complète d'un jeu de société, le développement d'agents autonomes dotés de capacités décisionnelles, ainsi qu'une présentation interactive via un site web.
**[Voir le site de présentation interactif en direct ici](https://litissia-gmz.github.io/diamant-decision-game/)**


## Présentation du projet
L'objectif était de concevoir un moteur de jeu robuste en **Python** capable de gérer des cycles de manches stochastiques (aléatoires) et d'y intégrer une intelligence artificielle heuristique. En complément, un **site web vitrine** a été développé en **HTML/CSS** pour présenter l'univers du jeu, ses règles et son fonctionnement de manière ergonomique.

## Intelligence Artificielle & Stratégie
Le cœur du projet repose sur la fonction `startegie_litissia`, un agent intelligent qui évalue le risque en temps réel selon plusieurs facteurs :
- **Analyse de l'environnement :** Observation du nombre de pièges déjà révélés (`pieges_vus`).
- **Évaluation du gain :** Calcul du ratio rubis en main vs danger potentiel.
- **Adaptabilité :** La prise de risque évolue dynamiquement au fil des 5 manches pour optimiser le score final.

## Présentation Web
Le projet inclut une interface de présentation réalisée en **HTML5** et **CSS3**. Ce site permet de :
- Consulter les règles détaillées du jeu.
- Découvrir l'histoire et le contexte du développement.
- Visualiser l'identité visuelle du projet "Diamant".

## Compétences techniques validées
- **Programmation Python :** Fonctions, boucles complexes, gestion de l'aléatoire.
- **Développement Web :** Structure sémantique HTML, mise en forme et responsive design en CSS.
- **Structures de données :** Utilisation avancée de dictionnaires, listes et sets.
- **Architecture logicielle :** Découplage entre le moteur de jeu (backend) et l'interface de présentation (frontend).
- 
Projet réalisé en binôme par Litissia - Étudiante en L1 Informatique
