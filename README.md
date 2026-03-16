# Simulation d'Environnement Décisionnel - Jeu Diamant

Ce projet, réalisé dans le cadre de la Licence Informatique à l'Université d'Angers, consiste en la modélisation complète d'un jeu de société et le développement d'agents autonomes dotés de capacités décisionnelles.

## Présentation du projet
L'objectif était de concevoir un moteur de jeu robuste en **Python** capable de gérer des cycles de manches stochastiques (aléatoires) et d'y intégrer une intelligence artificielle heuristique.

##  Intelligence Artificielle & Stratégie
Le cœur du projet repose sur la fonction `startegie_litissia`, un agent intelligent qui évalue le risque en temps réel selon plusieurs facteurs :
- **Analyse de l'environnement :** Observation du nombre de pièges déjà révélés (`pieges_vus`).
- **Évaluation du gain :** Calcul du ratio rubis en main vs danger potentiel.
- **Adaptabilité :** La prise de risque évolue dynamiquement au fil des 5 manches pour optimiser le score final.

##  Compétences techniques validées
- **Programmation Python :** Fonctions, boucles complexes, gestion de l'aléatoire.
- **Structures de données :** Utilisation avancée de dictionnaires, listes et sets.
- **Architecture logicielle :** Découplage entre le moteur de jeu (backend) et l'agent décisionnel.

---
*Projet réalisé par Litissia - Étudiante en L1 Informatique à Angers.*
