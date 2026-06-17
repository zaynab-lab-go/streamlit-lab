# streamlit-lab

Le développement de cette application a été une expérience formatrice, ponctuée par plusieurs étapes clés :

1. Initialisation et configuration
Tout a commencé par la mise en place de mon environnement de travail. J'ai d'abord configuré mon espace local et établi une liaison directe entre VS Code et GitHub pour garantir un versionnage efficace de mon code. Avant de me lancer dans le cœur du projet, j'ai réalisé une phase de prototypage via test_app.py, où j'ai pu expérimenter les différents widgets de Streamlit et valider leur comportement.

Le document joint présente quelques premières étapes de réalisation du projet. Même s'il n'est pas complet, il témoigne du respect de la démarche préconisée dans le guide du projet. 

3. Itération et montée en charge
La phase de développement a été un processus itératif. J'ai testé plusieurs architectures de code, cherchant à trouver l'équilibre idéal entre lisibilité et performance. Ce n'est qu'après plusieurs sessions de tests et d'ajustements que j'ai pu stabiliser la structure actuelle, permettant l'ajout progressif des 7 visualisations pertinentes.

4. Défis techniques et compromis
Le projet a également été l'occasion de faire face à des limites techniques :

    - Gestion des ressources : Initialement, j'avais envisagé d'utiliser la bibliothèque transformers pour l'analyse de sentiment. Cependant, sa lourdeur et la complexité de sa manipulation dans un environnement de déploiement léger m'ont poussé à la remplacer par TextBlob.

    - Intégration des données : Bien que j'aie réussi à fusionner les données de GitHub et ProductHunt, l'ajout d'une troisième source de données s'est avéré plus complexe que prévu, notamment en raison de restrictions d'accès API. Cette limite m'a permis de me concentrer davantage sur la qualité de l'analyse des deux sources principales, garantissant ainsi un dashboard robuste.


