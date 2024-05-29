
# L'Art de l'Ingénierie des Prompts : Maîtriser l'Art de Donner des Instructions aux Modèles de Langage

## Introduction

L'ingénierie des prompts est la pratique consistant à créer des prompts efficaces pour tirer le meilleur parti des grands modèles de langage (LLMs). En fournissant les bonnes instructions, exemples et contextes, vous pouvez orienter le modèle pour générer des sorties de meilleure qualité et plus pertinentes pour votre cas d'utilisation spécifique.

Dans ce tutoriel, nous couvrirons une gamme de techniques de prompting, des plus basiques aux plus avancées. Pour chacune d'elles, je fournirai des exemples clairs, des explications sur ce qu'elle vise à accomplir, des instructions étape par étape et des conseils sur quand l'appliquer. À la fin, vous aurez une solide compréhension des fondamentaux de l'ingénierie des prompts et serez capable de tirer parti des LLMs plus efficacement pour vos applications.

## Table des Matières

1. Attribution des Rôles et Responsabilités
2. Entrée et Sortie Structurées
3. Préremplissage des Réponses du Modèle
4. N-Shot Prompting
5. Chain-of-Thought Prompting
6. Division des Prompts en Étapes Plus Petites
7. Placement Optimal du Contexte
8. Rédaction d'Instructions Efficaces
9. Atténuation des Hallucinations
10. Utilisation de Séquences d'Arrêt
11. Sélection d'une Température Optimale
12. Enchaînement de Prompts
13. Réglage des Prompts
14. Ensemble de Prompts
15. Augmentation des Prompts
16. Décomposition des Prompts
17. Fine-Tuning Basé sur les Prompts

## Technique 1 : Attribution des Rôles et Responsabilités

### Exemple

```text
Vous êtes un modérateur de contenu expert responsable de l'identification des aspects nuisibles dans les prompts des utilisateurs. Examinez attentivement le prompt suivant : {...}
```

### Explication
Attribuer au modèle un rôle et une responsabilité spécifiques fournit un contexte qui oriente ses réponses en termes de contenu, de ton, de style, etc. Cela encourage le modèle à incarner cette perspective.

### Comment Faire
1. Décidez d'un rôle ou d'une responsabilité pertinent pour la tâche
2. Indiquez-le clairement au début du prompt
3. Optionnellement, insistez sur les aspects clés comme "Vous êtes un expert en..." ou "Vous êtes responsable de..."
4. Fournissez l'entrée que le modèle doit traiter en fonction de ce rôle

### Quand l'Utiliser
- Lorsqu'un ton, un style ou une expertise de domaine spécifique est nécessaire
- Pour améliorer la qualité des sorties sur des tâches comme la modération de contenu, la vérification des faits, l'analyse, etc.

### Études de Cas Réelles
- Un chatbot de service client a été amélioré en lui attribuant le rôle d'un agent empathique et résolvant les problèmes, ce qui a entraîné des scores de satisfaction client plus élevés.
- Un assistant d'écriture AI a été assigné au rôle d'un éditeur expérimenté, fournissant des retours plus constructifs et exploitables aux utilisateurs.

## Technique 2 : Entrée et Sortie Structurées

### Exemple

```text
Extrayez les attributs <nom>, <taille>, <prix> et <couleur> de cette description de produit :
<description>
Le SmartHome Mini est un assistant domestique intelligent compact disponible en noir ou blanc pour seulement 49,99 $...
</description>
```

### Explication
Une entrée structurée aide le modèle à mieux comprendre la tâche et les données d'entrée. Une sortie structurée rend les réponses du modèle plus faciles à analyser et à intégrer dans les systèmes en aval.

### Comment Faire
1. Identifiez les données d'entrée et les champs de sortie souhaités
2. Représentez les données d'entrée avec des balises sémantiques comme XML ou JSON
3. Spécifiez les champs de sortie et le format dans les instructions
4. Analysez la réponse structurée du modèle en aval

### Quand l'Utiliser
- Lors du traitement de données comme les informations sur les produits, les avis des utilisateurs, les entrées de base de connaissances, etc.
- Pour simplifier l'intégration des sorties du modèle dans les bases de données, les API, les interfaces utilisateur

### Études de Cas Réelles
- Une entreprise de commerce électronique a utilisé des données de produits structurées pour entraîner un modèle AI à générer des descriptions de produits convaincantes, augmentant les taux de clics et les ventes.
- Un cabinet d'avocats a utilisé des résumés de cas structurés pour créer un assistant de recherche juridique alimenté par l'AI, économisant des heures de révision de documents pour les avocats.

## Technique 3 : Préremplissage des Réponses du Modèle

### Exemple

```text
Extrayez les attributs <nom>, <taille>, <prix> et <couleur>. Répondez en utilisant les balises <response> :
<response>
<name>
```

### Explication
Préremplir le début de la réponse du modèle garantit qu'il commencera par le texte fourni. Cela est utile pour inciter à un format de sortie spécifique et simplifier l'analyse.

### Comment Faire
1. Décidez du texte ou du format de départ souhaité
2. Ajoutez-le au début de la réponse du "assistant" ou du modèle
3. Assurez-vous qu'il est formulé comme une phrase partielle que le modèle peut continuer

### Quand l'Utiliser
- Pour imposer un format de sortie cohérent
- Lorsque la sortie doit être analysée ou désérialisée d'une certaine manière

### Études de Cas Réelles
- Une application de santé mentale a prérempli les réponses de son thérapeute AI avec des phrases empathiques, créant une expérience utilisateur plus engageante et de soutien.
- Un outil d'automatisation des ventes a prérempli des modèles d'e-mails avec des salutations personnalisées et des appels à l'action, améliorant les taux de réponse et les conversions.

## Technique 4 : N-Shot Prompting

### Exemple

```text
"Classifiez le sentiment de cette critique de film :
Critique : L'intrigue était captivante et le jeu d'acteur superbe. J'étais sur le bord de mon siège !
Sentiment : Positif

Critique : L'histoire n'avait aucun sens et les personnages étaient totalement invraisemblables. Une perte de temps.
Sentiment : Négatif

Critique : Cela a commencé de manière intrigante mais est tombé à plat. Quelques bons moments mais globalement décevant.
Sentiment : Mitigé

Critique : {Nouvelle Critique}
Sentiment :"
```

### Explication
Fournir plusieurs exemples d'entrée-sortie montre au modèle comment effectuer la tâche et le format de réponse souhaité. Cela conditionne le modèle à suivre le même schéma.

### Comment Faire
1. Collectez un ensemble diversifié d'exemples représentant les entrées de production attendues
2. Assurez-vous que les exemples capturent les formats clés, les cas limites, etc.
3. Fournissez au moins une douzaine d'exemples, plus pour les tâches complexes
4. Placez les exemples avant l'entrée réelle à traiter

### Quand l'Utiliser
- Pour la plupart des tâches, car cela améliore la qualité et la cohérence des sorties
- Lorsqu'un format ou un style de réponse spécifique doit être suivi

### Études de Cas Réelles
- Un agrégateur de nouvelles a utilisé le n-shot prompting pour entraîner son AI à catégoriser les articles par sujet, améliorant la précision des recommandations et l'engagement des utilisateurs.
- Une startup de technologie RH a appliqué le n-shot prompting pour créer un filtre de CV AI, permettant une sélection des candidats plus rapide et plus cohérente.

## Technique 5 : Chain-of-Thought Prompting

### Exemple

```text
"Voici une transcription de réunion :
<transcript>
{Texte de la Transcription}
</transcript>

Réfléchissez à la manière de résumer cela :
<sketchpad>
- Identifiez les décisions clés prises et qui en est responsable
- Notez les points de discussion importants et les conclusions
- Déterminez l'objectif global et le résultat de la réunion
</sketchpad>

Sur la base du <sketchpad>, fournissez un résumé de la réunion :
<summary>"
```

### Explication
Le chain-of-thought prompting encourage le modèle à décomposer son raisonnement en étapes intermédiaires avant de fournir un résultat final. Cela améliore souvent la qualité des sorties, en particulier pour les tâches complexes.

### Comment Faire
1. Spécifiez l'entrée et la tâche
2. Fournissez un "sketchpad" ou "scratchpad" pour que le modèle montre son travail
3. Optionnellement, incluez des instructions détaillées pour le processus de raisonnement
4. Demandez au modèle de générer une sortie finale basée sur les étapes intermédiaires

### Quand l'Utiliser
- Pour les tâches impliquant plusieurs étapes, du raisonnement ou des calculs
- Pour améliorer la transparence et l'interprétabilité des sorties du modèle
- Lorsque la factualité et la fidélité à l'entrée sont cruciales

### Études de Cas Réelles
- Une application éducative a utilisé le CoT prompting pour créer un tuteur AI capable de guider les étudiants à travers des étapes de résolution de problèmes complexes, améliorant les résultats d'apprentissage.
- Une société d'analyse financière a utilisé le CoT prompting pour créer un conseiller en investissement AI capable d'expliquer ses choix d'actions, augmentant la confiance et la fidélité des clients.

## Technique 6 : Division des Prompts en Étapes Plus Petites

### Exemple

```text
Tout d'abord, extrayez tous les noms mentionnés :
<names>
{Noms Extraits}
</names>

Ensuite, extrayez les événements clés et leurs dates :
<events>
{Événements Extraits}
</events>

Enfin, résumez les relations entre les noms et événements extraits :
<summary>
{Résumé Final}
</summary>
```

### Explication
Décomposer un prompt complexe en une série de prompts plus petits et ciblés peut améliorer la qualité de la sortie finale. Cela permet au modèle de se concentrer sur une tâche à la fois.

### Comment Faire
1. Identifiez les sous-tâches nécessaires pour générer la sortie finale
2. Rédigez des prompts ciblés pour chaque sous-tâche
3. Demandez au modèle étape par étape, en utilisant les sorties précédentes comme entrées pour l'étape suivante
4. Combinez les résultats en une sortie finale

### Quand l'Utiliser
- Pour les tâches complexes nécessitant plusieurs étapes de traitement
- Lorsqu'une grande entrée doit être décomposée et analysée morceau par morceau
- Pour réduire les hallucinations en ancrant chaque étape dans les sorties précédentes du modèle

### Études de Cas Réelles
- Une agence de marketing a divisé ses prompts de génération de contenu en étapes d'idéation, de planification et de rédaction, produisant des articles de blog et des contenus de médias sociaux de meilleure qualité.
- Une équipe de développement logiciel a décomposé ses prompts de génération de code en étapes de définition de fonction, de docstring et d'implémentation, conduisant à un code plus modulaire et maintenable.

## Technique 7 : Placement Optimal du Contexte

### Exemple

```text
Vous êtes un assistant de réunion expert responsable de la rédaction de comptes rendus de réunion précis.

<transcript>
{Transcription de la Réunion}
</transcript>

Identifiez les décisions clés, les points de discussion et les prochaines étapes. Résumez le tout de manière concise.

<minutes>
```

### Explication
Pour de meilleurs résultats, fournissez le contexte d'entrée au début du prompt, après avoir spécifié le rôle du modèle mais avant de donner des instructions détaillées. Cela concentre le modèle sur l'entrée.

### Comment Faire
1. Spécifiez d'abord le rôle ou les responsabilités du modèle
2. Fournissez le contexte ou les informations à traiter
3. Donnez des instructions détaillées sur ce qu'il faut faire avec le contexte
4. Optionnellement, spécifiez un format de sortie

### Quand l'Utiliser
- Dans la plupart des prompts, car cette séquence tend à bien fonctionner
- Surtout pour les tâches où le contexte d'entrée est crucial

### Études de Cas Réelles
- Une plateforme d'événements virtuels alimentée par l'AI a optimisé ses prompts en plaçant les détails clés de l'événement en premier, ce qui a entraîné des recommandations de sessions plus pertinentes et engageantes pour les participants.
- Un site de réservation de voyages a amélioré les réponses de son chatbot en plaçant les préférences et contraintes de voyage tôt dans le prompt, fournissant un support client plus personnalisé et efficace.

## Technique 8 : Rédaction d'Instructions Efficaces

### Exemple

```text
"Résumez les points clés de la transcription ci-dessous.

Utilisez des phrases courtes et concises.

Organisez le résumé en sections 'Décisions', 'Actions' et 'Autres Notes'.

<transcript>
{Transcription}
</transcript>

<summary>"
```

### Explication
Des instructions efficaces sont essentielles pour obtenir de bons résultats des LLMs. Les instructions doivent être claires, spécifiques et formatées pour une lecture facile par le modèle.

### Comment Faire
1. Utilisez des phrases courtes et ciblées
2. Séparez les instructions par des sauts de ligne
3. Mettez en gras ou en évidence les parties clés si le modèle le permet
4. Évitez les instructions très basiques ou trop évidentes
5. Révisez et reformulez périodiquement les prompts pour les garder concis

### Quand l'Utiliser
- Toujours ! Investir dans la rédaction de bonnes instructions se traduit par de meilleures sorties du modèle.

### Études de Cas Réelles
- Une entreprise de recherche UX a affiné ses prompts avec des instructions plus claires et spécifiques, obtenant des retours d'utilisateurs plus perspicaces et exploitables.
- Une organisation à but non lucratif a optimisé ses prompts de génération de propositions de subventions, obtenant plus de financements en alignant les sorties avec les priorités et les directives des bailleurs de fonds.

## Technique 9 : Atténuation des Hallucinations

### Exemple

```text
"Sur la base des informations fournies dans <context>, répondez à la question. S'il n'y a pas assez d'informations pour répondre de manière concluante, répondez par 'Je ne sais pas.'

<context>
{Contexte}
</context>

Question : {Question}

Réponse :"
```

### Explication
Les modèles peuvent parfois "halluciner" ou fabriquer des informations non présentes dans l'entrée. Nous pouvons réduire cela en demandant au modèle d'exprimer des incertitudes lorsque cela est approprié.

### Comment Faire
1. Rappelez au modèle de répondre uniquement sur la base du contexte fourni
2. Demandez-lui de dire "Je ne sais pas" ou similaire si l'entrée ne contient pas assez d'informations
3. Demandez au modèle d'exprimer sa confiance et de ne répondre que s'il est très confiant
4. Utilisez le chain-of-thought prompting pour permettre au modèle de vérifier son travail

### Quand l'Utiliser
- Pour les tâches de question-réponse ou de récupération de connaissances
- Lorsque l'exactitude factuelle est cruciale et que les hallucinations doivent être minimisées
- En combinaison avec d'autres techniques comme le CoT prompting

### Études de Cas Réelles
- Un AI de diagnostic médical a réduit les faux positifs en demandant au modèle de ne faire des prédictions que lorsqu'il est confiant sur la base de preuves symptomatiques claires, améliorant la sécurité des patients.
- Un système de détection de fausses nouvelles a atténué les fausses alertes en demandant au modèle de se concentrer sur les affirmations vérifiables et les sources crédibles, améliorant sa fiabilité et sa confiance.

## Technique 10 : Utilisation de Séquences d'Arrêt

### Exemple

```text
"Résumez la transcription de réunion suivante :

<transcript>
{transcription}
</transcript>

Fournissez un résumé concis :
<summary>"

Séquences d'Arrêt : ["</summary>"]
```

### Explication
Les séquences d'arrêt sont des mots ou des phrases qui signalent au modèle d'arrêter de générer du contenu supplémentaire. Elles aident à éviter le texte superflu et à rendre les réponses plus faciles à analyser.

### Comment Faire
1. Identifiez un mot ou une phrase d'arrêt unique
2. Incluez-le à la fin de la sortie attendue du prompt
3. Fournissez la séquence d'arrêt comme paramètre lors de l'appel de l'API du modèle
4. Analysez la sortie du modèle jusqu'à la séquence d'arrêt

### Quand l'Utiliser
- Pour obtenir des sorties de modèle plus propres et plus prévisibles
- Lorsque la réponse doit être analysée de manière programmatique
- Pour éviter de payer pour des tokens générés inutiles


## Technique 11 : Sélection d'une Température Optimale

### Exemple

```text
Température = 0.2 # Pour des sorties précises et ciblées
Température = 0.8 # Pour des sorties plus diverses et créatives
```

### Explication
La température est un paramètre du modèle qui contrôle la "créativité" des sorties. Des valeurs plus basses produisent des réponses plus ciblées et déterministes, tandis que des valeurs plus élevées donnent des résultats plus divers et imprévisibles.

### Comment Faire
1. Comprenez votre tâche et les caractéristiques de sortie souhaitées
2. Commencez avec une température de 0.8, puis ajustez au besoin
3. Utilisez des températures plus basses (0.2-0.5) pour des tâches précises, analytiques ou à choix multiples
4. Utilisez des températures plus élevées (0.7-1.0) pour des tâches ouvertes, créatives ou basées sur des opinions

### Quand l'Utiliser
- Toujours définir ce paramètre pour votre cas d'utilisation, ne vous contentez pas du défaut
- Ajustez-le en fonction du niveau de concentration ou de créativité nécessaire

### Études de Cas Réelles
- Un générateur de recettes AI a trouvé le juste milieu entre créativité et cohérence en ajustant sa température, produisant des idées de repas plus diverses mais fiables.
- Une startup de mode a optimisé la température de son modèle de recommandation de tenues pour trouver un équilibre entre nouveauté et portabilité, augmentant la satisfaction et l'engagement des utilisateurs.

## Technique 12 : Enchaînement de Prompts

### Exemple

```text
Générez trois idées d'histoires créatives basées sur le thème 'amitié inattendue' :
<ideas>
1. {Idée 1}
2. {Idée 2}
3. {Idée 3}
</ideas>
```

```text
Sélectionnez l'idée la plus originale et développez-la en un résumé de l'intrigue :
<plot>
{Résumé de l'intrigue}
</plot>
```

```text
Peaufinez l'écriture et ajoutez des détails vivants pour créer une ouverture d'histoire engageante :
<story>
{Paragraphes d'ouverture}
</story>
```

### Explication
L'enchaînement de prompts consiste à utiliser la sortie d'un prompt comme entrée pour un prompt suivant. Cela permet de guider le modèle à travers un processus génératif en plusieurs étapes pour affiner et améliorer progressivement la sortie.

### Comment Faire
1. Décomposez votre tâche en une série de prompts, chacun s'appuyant sur le précédent
2. Spécifiez le format d'entrée et de sortie pour chaque étape
3. Utilisez la sortie du modèle d'une étape comme entrée pour la suivante
4. Répétez jusqu'à obtenir une sortie finale satisfaisante

### Quand l'Utiliser
- Pour des tâches génératives complexes pouvant être décomposées en étapes
- Pour permettre au modèle d'affiner et d'améliorer progressivement sa sortie
- Lorsqu'un seul prompt serait trop compliqué ou contraignant

### Études de Cas Réelles
- Un studio de jeux a utilisé l'enchaînement de prompts pour générer des histoires de personnages riches, des quêtes et des dialogues, créant des expériences RPG plus immersives et engageantes.
- Une agence de publicité a utilisé l'enchaînement de prompts pour concevoir, affiner et visualiser des concepts publicitaires, produisant des campagnes plus créatives et percutantes en moins de temps.

## Technique 13 : Réglage des Prompts

### Exemple

```prompt
Ajustez un prompt pour reproduire le comportement suivant :

Utilisateur : Comment faire des cookies aux pépites de chocolat maison ?
Assistant : Voici une recette simple pour de délicieux cookies aux pépites de chocolat faits maison :

Ingrédients :
- 2 1/4 tasses de farine tout usage
- 1 c. à thé de bicarbonate de soude
- 1 c. à thé de sel
- 1 tasse de beurre non salé, ramolli
- 3/4 tasse de sucre granulé
- 3/4 tasse de sucre brun compacté
- 1 c. à thé d'extrait de vanille
- 2 gros œufs
- 2 tasses de pépites de chocolat mi-sucré

Instructions :
1. Préchauffez le four à 375°F et tapissez des plaques à pâtisserie de papier sulfurisé.
2. Dans un bol, mélangez la farine, le bicarbonate de soude et le sel ; réservez.
3. Dans un grand bol ou un batteur sur socle, battez le beurre et les deux sucres jusqu'à ce qu'ils soient crémeux.
4. Incorporez la vanille et les œufs jusqu'à ce qu'ils soient combinés.
5. Incorporez progressivement le mélange de farine aux ingrédients humides.
6. Incorporez les pépites de chocolat à la main.
7. Déposez des cuillerées à soupe de pâte arrondies sur les plaques à pâtisserie préparées.
8. Faites cuire pendant 9 à 11 minutes ou jusqu'à ce qu'ils soient dorés.
9. Laissez refroidir sur les plaques à pâtisserie pendant 2 minutes, puis transférez-les sur des grilles pour refroidir complètement.

Dégustez vos cookies aux pépites de chocolat maison chauds et fondants avec un verre de lait froid !

Utilisateur : Quelle est la meilleure façon d'enlever une tache de vin rouge ?
Assistant : Pour enlever une tache de vin rouge, suivez ces étapes :

1. Tamponnez immédiatement la tache avec un chiffon propre pour absorber autant de vin que possible. Évitez de frotter, car cela peut étendre la tache.
2. Saupoudrez généreusement du sel sur la tache encore humide. Le sel absorbera le vin et aidera à éliminer la couleur. Laissez reposer pendant 2-3 minutes, puis brossez le sel.
3. Étirez le tissu sur un bol et fixez-le avec un élastique. Versez de l'eau bouillante sur la tache à environ 20 cm de hauteur - la hauteur donne de la force pour éliminer la tache.
4. Si la tache persiste, mélangez 1 part de savon à vaisselle et 2 parts de peroxyde d'hydrogène. Testez d'abord sur une zone discrète. Appliquez sur la tache et laissez reposer pendant 30 minutes. Rincez abondamment.
5. Pour les taches tenaces, faites tremper le vêtement dans un nettoyant enzymatique ou un agent de blanchiment sans danger pour les couleurs et de l'eau froide pendant la nuit. Puis lavez comme d'habitude.
6. Si le vêtement est uniquement nettoyable à sec, tamponnez la tache et apportez-le au nettoyeur à sec dès que possible. Indiquez la tache et précisez qu'il s'agit de vin rouge.

La clé est d'agir rapidement, d'utiliser de l'eau froide (l'eau chaude peut fixer la tache) et d'être patient en répétant les traitements si nécessaire. Avec ces étapes, vous avez de bonnes chances d'éliminer cette tache de vin rouge gênante.

Utilisateur : {Nouvelle Entrée Utilisateur}
Assistant :
```

### Explication
Le réglage des prompts utilise l'apprentissage automatique pour optimiser les prompts en fonction d'un ensemble de conversations d'exemple. En fournissant des exemples de haute qualité de comportements souhaités, vous pouvez "ajuster" un prompt de base pour reproduire de manière fiable ces comportements dans de nouvelles conversations.

### Comment Faire
1. Collectez un ensemble de conversations d'exemple démontrant le comportement idéal du modèle
2. Formatez les conversations pour le réglage, généralement sous forme de séries d'échanges utilisateur-assistant
3. Utilisez un outil comme [DSPY](https://github.com/stanfordnlp/dspy) pour ajuster un prompt sur les exemples
4. Testez le prompt ajusté sur de nouvelles entrées et collectez plus d'exemples pour l'affiner de manière itérative

### Quand l'Utiliser
- Lorsque vous disposez d'un grand ensemble de conversations d'exemple à partir desquelles apprendre
- Pour découvrir des prompts optimisés plus rapidement que par itération manuelle
- Pour des cas d'utilisation où un comportement de modèle très fiable et cohérent est crucial

### Études de Cas Réelles
- Une plateforme d'apprentissage en ligne a ajusté ses prompts sur des données d'interaction des apprenants pour créer des contenus de cours et des évaluations plus personnalisés et efficaces.
- Une startup de santé mentale a ajusté ses prompts sur des conversations thérapeute-patient pour développer un compagnon AI plus empathique et soutenant pour ses utilisateurs.

Bien sûr, je vais reprendre la traduction à partir de la section Technique 14.

## Technique 14 : Ensemble de Prompts

### Exemple

```text
Prompt 1 - Ton Formelle :
Réécrivez cet e-mail pour qu'il soit plus professionnel et poli :
<email>
Salut Bob,
J'ai besoin de ces rapports TPS sur mon bureau d'ici vendredi, sinon nous allons manquer la date limite. Fais-le.
</email>
```

```text
<formal>
Cher Bob,
Je voulais faire un suivi concernant les rapports TPS. Pour nous assurer de respecter la date limite à venir, pourriez-vous les fournir d'ici la fin de la journée vendredi ? Faites-moi savoir si vous avez des questions ou avez besoin d'aide.
Merci pour votre attention à cette affaire.
Cordialement,
</formal>
```

```text
Prompt 2 - Ton Empathique :
Réécrivez cet e-mail pour qu'il soit plus compréhensif et empathique :
<email>
Salut Bob,
J'ai besoin de ces rapports TPS sur mon bureau d'ici vendredi, sinon nous allons manquer la date limite. Fais-le.
</email>
```

```text
<empathetic>
Salut Bob,
Je sais que tu travailles dur sur les rapports TPS. J'apprécie vraiment ton effort, car je sais que c'est une tâche difficile. La date limite est ce vendredi et je suis inquiet de l'impact si nous la manquons. Y a-t-il quelque chose que je puisse faire pour t'aider ou te soutenir pour les terminer à temps ? Fais-le moi savoir.
Merci pour ton dévouement,
</empathetic>
```

```text
Prompt 3 - Combiner Formelle et Empathique :
Combinez les meilleurs éléments de <formal> et <empathetic> pour trouver un équilibre idéal entre professionnalisme et compréhension :
```

```text
<combined>
Cher Bob,
Je voulais faire un suivi concernant les rapports TPS. Je sais combien d'efforts tu y mets et j'apprécie énormément ton travail acharné.
En même temps, je suis préoccupé par le respect de la date limite de vendredi. Je suis heureux de fournir tout soutien ou ressources dont tu as besoin pour terminer les rapports dans les délais. Fais-le moi savoir comment je peux aider.
Merci pour ton dévouement à ce projet important.
Cordialement,
</combined>
```

### Explication Détaillée

L'ensemble de prompts est une technique qui combine les sorties de plusieurs prompts pour produire une réponse finale qui intègre les meilleurs aspects de chaque sortie individuelle. L'idée est de tirer parti des forces et de compenser les faiblesses des différentes approches de prompting en générant des réponses candidates à partir de prompts avec différents tons, styles, domaines d'intérêt ou perspectives, puis en les combinant intelligemment.

Il y a quelques étapes clés pour l'ensemble de prompts :

1. **Conception des Prompts** : Créez plusieurs prompts qui capturent chacun un aspect différent souhaité, un ton ou un style pour la sortie. Ces prompts doivent être conçus pour se compléter et fournir un ensemble diversifié de réponses candidates. Par exemple, vous pourriez avoir un prompt qui se concentre sur un ton formel et professionnel, un autre qui met l'accent sur une perspective empathique et compréhensive, et un troisième qui privilégie la concision et la clarté.

2. **Génération de Candidats** : Utilisez chacun de ces prompts séparément pour générer une réponse candidate à partir du modèle de langage. Cela vous donnera un ensemble de réponses avec des caractéristiques différentes basées sur les prompts spécifiques utilisés.

3. **Combinaison des Réponses** : Utilisez un prompt supplémentaire pour évaluer et combiner les meilleurs éléments de chaque réponse candidate. Ce prompt doit instruire le modèle sur la manière de sélectionner les parties les plus pertinentes de chaque candidat et de les intégrer dans une réponse finale cohérente. Alternativement, vous pouvez utiliser différentes méthodes d'échantillonnage, températures ou autres paramètres de génération pour chaque prompt, puis combiner les sorties de manière stochastique ou via une moyenne pondérée.

Le principal avantage de l'ensemble de prompts est qu'il permet d'injecter plusieurs caractéristiques souhaitées dans la sortie du modèle, ce qui peut être difficile à réaliser avec un seul prompt. En générant des réponses sous différents angles, puis en les combinant, la sortie finale peut être plus nuancée, complète et bien équilibrée.

### Exemple Détaillé

Prenons un exemple concret d'utilisation de l'ensemble de prompts pour générer une réponse à une plainte de client par e-mail. Nous utiliserons trois prompts différents pour capturer différents aspects d'une réponse idéale.

```text
E-mail du Client :
"Je suis extrêmement frustré par votre service. J'essaie d'obtenir un remboursement pour le produit défectueux que j'ai reçu depuis des semaines, mais chaque fois que j'appelle le service client, je suis baladé. C'est inacceptable. Si je n'obtiens pas mon remboursement dans les 48 heures, je vais cesser de faire affaire avec vous et déposer une plainte auprès du Better Business Bureau."
```

Prompt 1 - Ton Empathique :
```text
Écrivez une réponse à cet e-mail de plainte client qui soit très empathique et compréhensive de leur frustration :
<empathetic_response>
Cher client,
Je suis profondément désolé d'apprendre les difficultés que vous avez rencontrées avec notre service et la frustration que cela a causée. Je veux vous assurer que nous prenons vos préoccupations très au sérieux et nous nous engageons à rectifier cette situation.
Je ne peux qu'imaginer à quel point il doit être exaspérant de devoir gérer un produit défectueux et ensuite faire face à des défis pour obtenir un remboursement en temps opportun. Ce n'est pas le niveau de service que nous nous efforçons de fournir, et je m'excuse sincèrement pour cet échec.
Sachez que je vais escalader ce problème à notre équipe de gestion du support client pour garantir que votre remboursement soit traité rapidement et que vous receviez l'attention et les soins que vous méritez. Vous pouvez vous attendre à recevoir votre remboursement dans les 48 heures.
Nous apprécions vraiment votre entreprise et sommes reconnaissants de l'opportunité de vous servir. Si je peux vous aider de quelque manière que ce soit, n'hésitez pas à me le faire savoir. Nous sommes là pour vous aider.
Avec mes plus sincères excuses,
[Votre Nom]
Représentant du Service Client
</empathetic_response>
```

Prompt 2 - Orienté Solution :
```text
Écrivez une réponse à cet e-mail de plainte client qui soit axée sur la fourniture d'une solution claire et des prochaines étapes concrètes :
<solution_response>
Cher [Nom du Client],
Merci de nous avoir signalé ce problème. Je m'excuse pour le retard inacceptable dans le traitement de votre remboursement pour le produit défectueux que vous avez reçu.
Voici les étapes que nous allons suivre pour résoudre ce problème immédiatement :
1. J'ai escaladé votre dossier à notre équipe de gestion du support client avec un statut de haute priorité. Ils examineront votre dossier et s'assureront que votre remboursement soit traité le plus rapidement possible.
2. Vous pouvez vous attendre à recevoir votre remboursement complet dans les 48 heures. Nous vous enverrons un e-mail de confirmation une fois le remboursement effectué.
3. En guise d'excuses pour les désagréments causés, nous souhaitons vous offrir une réduction de 20 % sur votre prochain achat chez nous. Le code de réduction sera inclus dans votre e-mail de confirmation de remboursement.
4. Si vous rencontrez d'autres problèmes ou avez des préoccupations supplémentaires, veuillez répondre à cet e-mail et je m'assurerai personnellement que vos besoins soient satisfaits.
Nous nous engageons pleinement à votre satisfaction et nous excusons sincèrement pour la frustration que cette expérience vous a causée. Merci de nous donner l'opportunité de rectifier cela.
Cordialement,
[Votre Nom]
Représentant du Service Client
</solution_response>
```

Prompt 3 - Combiner Empathique et Orienté Solution :
```text
Combinez les parties les plus pertinentes de <empathetic_response> et <solution_response> pour créer une réponse finale au client qui soit à la fois compréhensive et fournisse des prochaines étapes claires. Assurez-vous que le ton reste cohérent et que la réponse soit fluide.
<final_response>
Cher [Nom du Client],
Je suis profondément désolé d'apprendre la frustration et les désagréments que vous avez rencontrés en raison du retard dans le traitement de votre remboursement pour le produit défectueux que vous avez reçu. Je veux vous assurer que nous prenons vos préoccupations très au sérieux et nous nous engageons à résoudre ce problème à votre entière satisfaction.
Voici les étapes immédiates que nous allons suivre :
1. J'ai escaladé votre dossier à notre équipe de gestion du support client avec une priorité élevée. Ils s'assureront que votre remboursement soit traité dans les 48 heures. Vous recevrez un e-mail de confirmation une fois le remboursement effectué.
2. En guise de sincères excuses, nous inclurons un code de réduction de 20 % pour votre prochain achat dans l'e-mail de confirmation de remboursement.
3. Si vous avez d'autres préoccupations ou problèmes, veuillez répondre directement à cet e-mail et je m'assurerai personnellement que vos besoins soient satisfaits rapidement.
Nous apprécions profondément votre entreprise et la confiance que vous nous accordez. Je suis vraiment désolé que nous n'ayons pas respecté notre engagement à fournir un service exceptionnel dans ce cas. Merci de nous donner l'opportunité de corriger cela et de vous fournir les soins et l'attention que vous méritez.
Avec mes plus sincères excuses et ma gratitude,
[Votre Nom]
Représentant du Service Client
</final_response>
```

Dans cet exemple, le premier prompt se concentre sur l'expression de l'empathie et de la compréhension de la frustration du client, tandis que le deuxième prompt met l'accent sur la fourniture d'une solution claire et des prochaines étapes concrètes. Le troisième prompt combine ensuite les éléments les plus pertinents de chaque réponse pour créer une réponse finale qui est à la fois empathique et orientée solution.

En utilisant l'ensemble de prompts, nous avons pu générer une réponse client plus complète et nuancée que ce qu'un seul prompt pourrait probablement réaliser. La réponse finale reconnaît la frustration du client, prend la responsabilité de l'échec du service, fournit un calendrier clair et des étapes pour résoudre le problème, et offre un geste d'excuse, tout en maintenant un ton cohérent et attentionné.

### Quand Utiliser l'Ensemble de Prompts

L'ensemble de prompts est particulièrement utile dans les situations où vous souhaitez que la sortie du modèle présente plusieurs caractéristiques ou couvre différents aspects qui sont difficiles à capturer avec un seul prompt. Quelques cas d'utilisation spécifiques où l'ensemble de prompts peut être bénéfique incluent :

- **Service Client** : Comme démontré dans l'exemple ci-dessus, l'ensemble de prompts peut aider à générer des réponses qui sont empathiques, axées sur la solution et qui trouvent le bon ton pour la situation.
- **Création de Contenu** : Pour générer des articles de blog, des articles ou des copies marketing, vous pouvez combiner des prompts qui se concentrent sur différents aspects comme la narration, la persuasion, l'optimisation SEO et la voix de la marque pour créer un contenu plus convaincant et complet.
- **Incarnation de Persona** : Si vous souhaitez que le modèle réponde en tant que persona spécifique, vous pouvez combiner des prompts qui capturent différents aspects de l'arrière-plan, des connaissances, de la personnalité et du style de communication de ce persona.
- **Perspectives Équilibrées** : Pour des sujets qui bénéficient de la prise en compte de plusieurs points de vue, combiner des prompts avec différentes positions ou angles peut aider à produire une réponse plus équilibrée et bien arrondie.
- **Écriture Créative** : Combiner des prompts ajustés pour différents styles d'écriture, tons ou genres peut aider à générer des sorties d'écriture créative plus uniques et engageantes.

L'essentiel est d'identifier les aspects distincts que vous souhaitez injecter dans la sortie du modèle, de créer des prompts ciblés pour chacun, puis de les combiner de manière à tirer parti de leurs forces individuelles.

### Conseils pour un Ensemble de Prompts Efficace

Pour tirer le meilleur parti de l'ensemble de prompts, gardez ces conseils à l'esprit :

1. **Prompts Complémentaires** : Concevez vos prompts individuels pour qu'ils soient complémentaires plutôt que redondants. Chaque prompt doit se concentrer sur un aspect distinct ou une caractéristique que les autres ne capturent pas pleinement.
2. **Combinaison Équilibrée** : Lorsque vous combinez les réponses candidates, visez un équilibre entre les différents aspects. Évitez de sur-emphasiser la sortie d'un prompt au détriment des autres.
3. **Cohérence et Consistance** : Assurez-vous que la réponse finale combinée maintienne une structure cohérente et un ton consistant. La sortie doit se lire comme un tout unifié plutôt que comme des parties disjointes.
4. **Itération et Test** : Développer des ensembles efficaces nécessite souvent de l'itération et des tests. Expérimentez avec différentes combinaisons de prompts, paramètres de génération et stratégies de combinaison pour voir ce qui produit les meilleurs résultats pour votre cas d'utilisation spécifique.
5. **Contrôle de Qualité** : Bien que l'ensemble de prompts puisse aider à améliorer la qualité des sorties, ce n'est pas une solution miracle. Assurez-vous de revoir les sorties finales pour vérifier leur exactitude factuelle, leur cohérence et leur alignement avec le ton et l'intention souhaités.

En concevant et en combinant de manière réfléchie des prompts complémentaires, l'ensemble de prompts peut être un outil puissant pour générer des sorties de modèle nuancées, complètes et de haute qualité. Il permet de tirer parti des forces de différentes approches de prompting et de compenser leurs faiblesses individuelles. Comme pour toute technique d'ingénierie de prompts, l'expérimentation et l'itération sont essentielles pour trouver l'ensemble optimal pour votre cas d'utilisation spécifique.

## Technique 15 : Augmentation des Prompts

### Exemple

```text
"Rédigez une déclaration de mission pour une marque de produits de nettoyage écologiques.

Contexte de l'entreprise :
- Fondée en 2010 à Portland, Oregon
- Spécialisée dans les solutions de nettoyage à base de plantes et biodégradables
- Donne 1 % de ses bénéfices à des associations de conservation des océans
- A une chaîne d'approvisionnement neutre en carbone et utilise des emballages recyclés
- Certifiée B-Corp et membre de 1% for the Planet

Déclaration de mission :
<mission>
{Déclaration de mission générée}
</mission>
```

### Explication
L'augmentation des prompts consiste à injecter des informations ou un contexte pertinent dans le prompt lui-même, plutôt que de se fier uniquement aux connaissances inhérentes du modèle. En fournissant des faits clés sur le sujet, vous pouvez aider le modèle à produire une sortie plus informée et personnalisée qui s'aligne avec le cas d'utilisation spécifique.

### Comment Faire
1. Identifiez les informations les plus importantes pour la tâche, telles que les faits clés, les exigences ou le contexte
2. Organisez ces informations de manière claire et concise
3. Incorporez le contexte supplémentaire dans le prompt, avant l'instruction réelle
4. Ajustez les informations au besoin en fonction des sorties du modèle

### Quand l'Utiliser
- Lors de la génération de contenu nécessitant des connaissances très spécifiques ou de niche
- Pour personnaliser les sorties du modèle à un cas d'utilisation particulier, comme une entreprise ou un individu
- Dans les cas où les connaissances par défaut du modèle peuvent être obsolètes, incomplètes ou mal alignées

### Études de Cas Réelles
- Une entreprise de listes immobilières a augmenté ses prompts de description de propriété avec des détails clés comme l'emplacement, les commodités et le prix pour générer des annonces plus convaincantes et informatives.
- Une plateforme de journalisme sportif a injecté des statistiques de joueurs, des moments forts de jeux et des historiques d'équipes pertinents dans ses prompts d'articles, produisant un contenu plus riche et engageant.

Bien sûr, je vais reprendre la traduction à partir de la section Technique 16.

## Technique 16 : Décomposition des Prompts

### Exemple

```text
Analysez les forces et les faiblesses de cet essai argumentatif.

Thèse de l'essai : {Thèse de l'essai}

Évaluez les aspects suivants de l'essai :

Structure :
<structure>
- L'essai a-t-il une introduction, un corps et une conclusion clairs ?
- Chaque paragraphe est-il centré sur une idée principale ?
- Les paragraphes sont-ils ordonnés de manière logique pour construire l'argument ?
</structure>

Preuves :
<evidence>
- L'essai fournit-il des preuves pertinentes et convaincantes pour chaque affirmation ?
- Les preuves sont-elles correctement citées à partir de sources crédibles ?
- Les preuves sont-elles bien expliquées et analysées ?
</evidence>

Raisonnement :
<reasoning>
- L'essai présente-t-il un argument cohérent et bien raisonné ?
- Y a-t-il des erreurs logiques ou des sauts dans l'argumentation ?
- L'essai aborde-t-il et réfute-t-il efficacement les contre-arguments ?
</reasoning>

Clarté :
<clarity>
- L'écriture est-elle claire, concise et facile à suivre ?
- Les termes et concepts clés sont-ils adéquatement expliqués ?
- L'essai maintient-il un ton formel et académique ?
</clarity>

Conclusion :
<conclusion>
- Résumez les forces et les faiblesses clés de l'essai en fonction des analyses de <structure>, <evidence>, <reasoning> et <clarity>.
- Fournissez des suggestions constructives pour l'amélioration.
</conclusion>
```

### Explication

La décomposition des prompts est une technique qui consiste à décomposer un prompt complexe en plusieurs sous-prompts plus ciblés. Au lieu d'essayer de traiter un problème multifacette avec un seul prompt global, vous créez des prompts ciblés pour chaque aspect ou composant clé de l'entrée. Cela permet au modèle d'analyser chaque partie plus en profondeur et de produire une sortie finale plus complète et nuancée.

Le processus de décomposition des prompts implique généralement les étapes suivantes :

1. **Analyse de la Tâche** : Commencez par analyser soigneusement la tâche globale et identifiez les composants, aspects ou dimensions clés qui doivent être abordés. Ceux-ci formeront la base de vos sous-prompts.
2. **Création de Sous-Prompts** : Pour chaque composant identifié, créez un sous-prompt spécifique qui se concentre uniquement sur cet aspect. Le sous-prompt doit fournir des instructions claires sur ce qu'il faut analyser et comment formater la sortie.
3. **Analyse Ciblée** : Utilisez chaque sous-prompt séparément pour générer une analyse ciblée du modèle sur ce composant spécifique. Cela permet au modèle d'approfondir chaque aspect sans être submergé ou confus par la complexité de la tâche complète.
4. **Prompt de Synthèse** : Après avoir généré des sorties pour tous les sous-prompts, créez un prompt final qui demande au modèle de synthétiser les points clés des analyses précédentes en une sortie globale cohérente. Ce prompt doit fournir des indications sur la manière de prioriser et d'intégrer les informations.
5. **Itération et Affinement** : Révisez la sortie finale pour évaluer si elle couvre de manière exhaustive la tâche initiale. S'il y a des lacunes ou des faiblesses, itérez sur vos sous-prompts pour couvrir ces aspects. Vous devrez peut-être ajouter, supprimer ou modifier des sous-prompts en fonction de ce que vous observez.

Le principal avantage de la décomposition des prompts est qu'elle permet au modèle de concentrer son attention et sa capacité sur un aspect à la fois, plutôt que d'essayer de tout gérer en même temps. En guidant le modèle à travers une série d'analyses ciblées, vous pouvez obtenir une sortie finale plus complète et multidimensionnelle qui couvre tous les aspects importants.

### Exemple Détaillé

Prenons un exemple de l'utilisation de la décomposition des prompts pour analyser la santé financière d'une entreprise basée sur son rapport annuel. La tâche globale est d'évaluer les forces, faiblesses, opportunités et menaces (analyse SWOT) de l'entreprise.

```text
Extrait du Rapport Annuel :
"Au cours de l'exercice 2022, Acme Inc. a réalisé un chiffre d'affaires record de 500 millions de dollars, soit une augmentation de 20 % par rapport à l'année précédente. Cette croissance a été principalement due à la performance solide de notre division de logiciels cloud, qui a enregistré une augmentation de 35 % des ventes. Les dépenses d'exploitation ont augmenté de 15 % pour atteindre 350 millions de dollars, principalement en raison des investissements en recherche et développement pour de nouvelles gammes de produits. Le revenu net a augmenté à 100 millions de dollars, soit une augmentation de 25 %.

Cependant, l'entreprise a également rencontré des défis dans sa division matérielle, avec une baisse de 10 % des ventes en raison de perturbations de la chaîne d'approvisionnement et d'une concurrence accrue. Pour y remédier, nous avons mis en place un plan de réduction des coûts et explorons des partenariats stratégiques.

À l'avenir, nous voyons des opportunités significatives sur le marché croissant des solutions d'affaires alimentées par l'IA, où nos nouveaux produits sont bien positionnés. Cependant, nous faisons également face à des menaces liées à l'incertitude économique persistante et au risque de nouveaux entrants sur nos marchés principaux."
```

Sous-Prompt 1 - Forces :
```text
Identifiez les principales forces de l'entreprise basées sur l'extrait du rapport annuel :
<strengths>
- Chiffre d'affaires record de 500 millions de dollars, soit une augmentation de 20 % par rapport à l'année précédente
- Performance solide de la division de logiciels cloud, avec une augmentation de 35 % des ventes
- Revenu net augmenté à 100 millions de dollars, soit une augmentation de 25 %
- Bien positionné sur le marché croissant des solutions d'affaires alimentées par l'IA avec de nouveaux produits
</strengths>
```

Sous-Prompt 2 - Faiblesses :
```text
Identifiez les principales faiblesses de l'entreprise basées sur l'extrait du rapport annuel :
<weaknesses>
- Baisse de 10 % des ventes de la division matérielle en raison de perturbations de la chaîne d'approvisionnement et d'une concurrence accrue
- Augmentation des dépenses d'exploitation de 15 % à 350 millions de dollars, réduisant la rentabilité
</weaknesses>
```

Sous-Prompt 3 - Opportunités :
```text
Identifiez les principales opportunités pour l'entreprise basées sur l'extrait du rapport annuel :
<opportunities>
- Potentiel de croissance significatif sur le marché en expansion des solutions d'affaires alimentées par l'IA
- Exploitation de nouveaux produits dans ce domaine pour capturer des parts de marché et stimuler la croissance des revenus
- Exploration de partenariats stratégiques pour renforcer la division matérielle en difficulté
</opportunities>
```

Sous-Prompt 4 - Menaces :
```text
Identifiez les principales menaces auxquelles l'entreprise est confrontée basées sur l'extrait du rapport annuel :
<threats>
- Incertitude économique persistante pouvant freiner la demande et impacter la croissance des revenus
- Risque de nouveaux entrants sur les marchés principaux de l'entreprise, augmentant la concurrence et la pression sur les prix
- Défis continus dans la division matérielle, pouvant affecter la performance globale
</threats>
```

Prompt de Synthèse :
```text
Sur la base des <strengths>, <weaknesses>, <opportunities> et <threats> identifiés, fournissez une évaluation globale de la santé financière et de la position stratégique de l'entreprise. Mettez en évidence les facteurs les plus importants et fournissez des recommandations pour la priorisation et l'action.

<synthesis>
La santé financière d'Acme Inc. est solide, avec une croissance record du chiffre d'affaires et du revenu net, principalement grâce à la performance de sa division de logiciels cloud. Les nouveaux produits bien positionnés sur le marché des solutions d'affaires alimentées par l'IA présentent une opportunité significative pour une expansion future et des gains de parts de marché.

Cependant, Acme fait face à des défis dans sa division matérielle, qui affecte la performance globale et la rentabilité. Aborder cela par la réduction des coûts et des partenariats stratégiques devrait être une priorité clé. L'entreprise doit également naviguer dans un contexte économique incertain et la menace de nouveaux concurrents sur ses marchés principaux.

Globalement, Acme est bien positionnée pour la croissance si elle peut exploiter l'opportunité de l'IA tout en renforçant son activité matérielle. Les recommandations clés incluent :

1. Intensifier le développement et la commercialisation des produits d'IA pour capturer des parts de marché dans ce secteur en pleine croissance
2. Accélérer les efforts de réduction des coûts et d'amélioration de l'efficacité dans la division matérielle
3. Poursuivre des partenariats stratégiques pour gagner en échelle et en capacités dans le matériel
4. Surveiller de près les conditions économiques et ajuster les plans si nécessaire
5. Investir dans le marketing et la différenciation pour se défendre contre les nouveaux entrants sur le marché

En se concentrant sur ces priorités, Acme peut s'appuyer sur ses forces, atténuer ses risques et se positionner pour une croissance durable et un leadership sur le marché.
</synthesis>
```

Dans cet exemple, nous avons décomposé la tâche complexe d'une analyse SWOT en quatre sous-prompts ciblés, chacun se concentrant sur un aspect spécifique de la situation de l'entreprise. Cela a permis au modèle de faire une analyse approfondie de chaque domaine et de tirer les informations les plus pertinentes.

Le prompt de synthèse a ensuite demandé au modèle d'intégrer les points clés des sous-prompts en une évaluation globale et des recommandations. En guidant le modèle à travers cette analyse structurée, nous avons pu obtenir une sortie complète et nuancée qui couvre toutes les dimensions importantes.

### Quand Utiliser la Décomposition des Prompts

La décomposition des prompts est particulièrement utile pour les tâches qui impliquent l'analyse de sujets complexes sous plusieurs angles ou la génération de sorties longues avec des sections distinctes. Quelques cas d'utilisation spécifiques où la décomposition des prompts peut être bénéfique incluent :

- **Évaluations Complètes** : Décomposer l'évaluation d'un essai, d'une candidature, d'une critique de produit ou d'un autre document complexe en scores ou analyses pour des critères comme la structure, le contenu, le style, etc.
- **Stratégie Multidimensionnelle** : Décomposer un exercice de planification stratégique en prompts séparés pour les objectifs, les priorités, les ressources, les risques, le calendrier, etc. pour développer un plan plus complet et cohérent.
- **Feedback et Recommandations Détaillés** : Fournir des retours approfondis sur un écrit, un code, un design ou un autre travail créatif en utilisant des prompts ciblés pour différents aspects comme la clarté, l'originalité, le mérite technique et les domaines d'amélioration.
- **Q&R Approfondie** : Répondre à une question complexe et multipartite en la décomposant en sous-questions et en synthétisant les réponses partielles en une réponse complète et bien organisée.
- **Rapports ou Présentations Structurés** : Générer un rapport ou une présentation complète en utilisant des prompts séparés pour chaque section comme le résumé exécutif, la méthodologie, les résultats, les conclusions, etc. et en les intégrant ensuite.

Le fil conducteur est que la décomposition des prompts fonctionne bien lorsque vous avez besoin que le modèle fournisse une analyse approfondie et multidimensionnelle ou génère une sortie longue et structurée. En décomposant la tâche en parties plus petites et ciblées, vous pouvez obtenir un produit final plus complet et cohérent.

### Conseils pour une Décomposition des Prompts Efficace

Pour tirer le meilleur parti de la décomposition des prompts, gardez ces conseils à l'esprit :

1. **Couverture Complète** : Assurez-vous que vos sous-prompts couvrent tous les aspects clés de la tâche. Faites une analyse approfondie au départ pour identifier les composants et dimensions importants à inclure.
2. **Exclusivité Mutuelle** : Visez des sous-prompts aussi distincts et non redondants que possible. Vous voulez que chacun d'eux suscite des informations uniques, pas des informations redondantes.
3. **Granularité Appropriée** : Trouvez un équilibre dans la portée de vos sous-prompts. Trop étroits et vous vous retrouverez avec un nombre écrasant de sous-prompts. Trop larges et le modèle ne pourra pas fournir une analyse suffisamment détaillée.
4. **Formatage Cohérent** : Utilisez un format cohérent pour vos sous-prompts et leurs sorties. Cela facilitera la compréhension des attentes par le modèle et l'intégration des résultats par vous.
5. **Guidance de Synthèse** : Fournissez des instructions claires dans votre prompt de synthèse sur la manière de prioriser, d'intégrer et de formater la sortie finale. Plus vous donnez de guidance spécifique, mieux le modèle pourra tout rassembler.

En concevant soigneusement vos sous-prompts et le prompt de synthèse, vous pouvez tirer parti de la puissance de la décomposition des prompts pour obtenir des sorties de modèle plus complètes, nuancées et bien structurées. C'est une technique précieuse à avoir dans votre boîte à outils d'ingénierie des prompts pour aborder des tâches d'analyse et de génération complexes.

## Technique 17 : Fine-Tuning Basé sur les Prompts

### Exemple

Fine-tunez un modèle sur un ensemble de données formaté comme :

```text
Q : Résumez l'article suivant :
<article>
{Texte de l'article}
</article>

A : <summary>
{Résumé de l'article}
</summary>
```

Puis, à l'inférence, utilisez le prompt suivant :
```text
Résumez l'article suivant :
<article>
{Texte du nouvel article}
</article>

<summary>
```

### Explication

Plutôt que de simplement fournir des prompts au moment de l'inférence, vous pouvez les intégrer dans le processus de fine-tuning du modèle lui-même. En formatant les données d'entraînement dans le même format question-réponse que les prompts cibles, le modèle apprend à suivre ces instructions spécifiques et à reproduire le comportement souhaité de manière plus fiable.

### Comment Faire

1. Collectez un ensemble de données de paires entrée-sortie pour votre tâche
2. Formatez chaque exemple comme un prompt, avec l'entrée comme "question" et la sortie comme "réponse"
3. Fine-tunez le modèle sur cet ensemble de données formaté en prompts
4. Au moment de l'inférence, utilisez des prompts avec de nouvelles entrées dans le même format que les données d'entraînement
5. Le modèle sera prêt à suivre les instructions et à générer des sorties dans le format attendu

### Quand l'Utiliser

- Lorsque vous disposez d'un ensemble de données suffisamment grand pour le fine-tuning (le few-shot learning ne suffit pas)
- Pour des tâches où vous souhaitez que le modèle suive de manière fiable un schéma d'interaction spécifique
- Pour "intégrer" certains prompts ou instructions dans le comportement du modèle
- Lorsque vous avez besoin d'une inférence plus rapide que ce que permet le few-shot prompting

### Études de Cas Réelles

- Un fournisseur de télésanté a fine-tuné son modèle de diagnostic sur des prompts de médecin-patient couvrant différentes spécialités, démographies et conditions, améliorant considérablement sa précision et son étendue.
- Une startup d'écriture AI a fine-tuné son modèle sur des paires prompt-réponse auteur-éditeur réussies pour développer un assistant de co-écriture plus polyvalent et fiable pour ses utilisateurs.

## Conseils de Dépannage

Lorsque vous commencez à mettre en œuvre ces techniques d'ingénierie des prompts, vous pouvez rencontrer certains défis ou écueils courants. Voici quelques conseils pour vous aider à résoudre les problèmes et à obtenir les meilleurs résultats possibles :

### Sorties Trop Verboses ou Hors Sujet

Si les réponses du modèle sont trop verbeuses, hors sujet ou incluent des informations inutiles, essayez les solutions suivantes :
- Resserrez vos instructions pour qu'elles soient aussi spécifiques et concises que possible. Évitez toute ambiguïté.
- Fournissez des exemples plus ciblés qui démontrent comment rester sur le sujet et être succinct.
- Utilisez des techniques comme la sortie structurée pour contraindre le modèle à un format spécifique.
- Réduisez le paramètre de température pour rendre les sorties plus concentrées et moins "créatives".

### Inexactitudes Factuelles ou Hallucinations
Lorsque le modèle fait des déclarations incorrectes ou fabrique des informations non présentes dans l'entrée :
- Insistez dans votre prompt pour n'utiliser que les informations fournies dans le contexte.
- Instruisez le modèle à exprimer des incertitudes lorsque l'entrée est insuffisante pour répondre de manière confiante.
- Utilisez le Chain-of-Thought Prompting pour permettre au modèle de montrer son raisonnement et de vérifier son propre travail.
- Affinez le modèle sur des données de vérité terrain de haute qualité pour réduire sa propension à halluciner.

### Manque de Cohérence Entre les Sorties
Si vous obtenez une qualité ou une pertinence très variable des sorties entre différents prompts :
- Fournissez plus d'exemples de meilleure qualité dans vos prompts Few-Shot pour établir un schéma plus clair.
- Utilisez le Prompt Tuning sur un ensemble de données plus large pour optimiser les prompts pour la cohérence.
- Augmentez le déterminisme de votre méthode d'échantillonnage ou réduisez la température.
- Ensemblez plusieurs prompts et combinez leurs sorties pour lisser la variabilité.

### Temps de Génération Lente
Lorsque le modèle prend beaucoup de temps pour générer des sorties, en particulier avec des prompts complexes :
- Cherchez des moyens de simplifier ou de décomposer votre prompt en sous-tâches plus petites.
- Réduisez la longueur maximale de la sortie si vous n'avez pas besoin de génération longue.
- Utilisez un modèle plus petit avec moins de paramètres pour une inférence plus rapide.
- Affinez le modèle sur votre tâche spécifique pour qu'il nécessite moins d'apprentissage au moment du prompt.

### Difficulté à Affiner les Prompts
Si vous avez du mal à améliorer vos prompts de manière itérative pour obtenir les résultats souhaités :
- Inspirez-vous des galeries de prompts et des exemples qui ont bien fonctionné pour des tâches similaires.
- Isolez et testez systématiquement des parties spécifiques de votre prompt pour voir lesquelles ont le plus grand impact.
- Rassemblez un ensemble diversifié d'exemples d'entrée couvrant différents scénarios que votre prompt doit gérer.
- Collaborez avec d'autres et obtenez des retours sur vos prompts - un regard neuf peut repérer de nouvelles opportunités.

Rappelez-vous, l'ingénierie des prompts est un processus itératif. Ne vous découragez pas si vos premières tentatives ne fonctionnent pas parfaitement. Analysez ce qui ne fonctionne pas, formulez une hypothèse et testez-la méthodiquement. Avec persévérance et expérimentation, vous pourrez affiner vos prompts pour produire des sorties excellentes de manière constante. Adoptez l'itération et profitez du processus pour devenir un pro de l'ingénierie des prompts !


## Conclusion

L'ingénierie des prompts est un outil puissant pour obtenir des sorties de haute qualité des grands modèles de langage (LLMs). En appliquant de manière réfléchie des techniques comme l'attribution de rôles, la fourniture d'exemples, la structuration des entrées/sorties et l'optimisation des paramètres, vous pouvez améliorer considérablement les résultats.

Quelques principes clés à retenir :

- Soyez clair, spécifique et concis dans vos instructions
- Fournissez un contexte et des exemples pertinents
- Décomposez les tâches complexes en étapes
- Optimisez pour votre cas d'utilisation, ne vous contentez pas des valeurs par défaut
- Expérimentez, itérez et testez ce qui fonctionne le mieux

J'espère que ce tutoriel vous a équipé d'une solide base en ingénierie des prompts. Combinez ces techniques et adaptez-les à vos besoins. Avec de la pratique, vous serez capable d'obtenir des résultats excellents de manière constante avec les LLMs. Bon prompting !

