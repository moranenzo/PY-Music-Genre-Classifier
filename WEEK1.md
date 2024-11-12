### **Semaine 1 : Recherche et préparation des données (uniquement pour les paroles)**

#### **1. Définir les objectifs précis et cadrer le projet**
   - **Choisir les émotions à détecter** : Optez pour trois ou quatre émotions distinctes (par exemple, joie, tristesse, colère, et surprise) pour simplifier l’analyse et rendre les résultats plus cohérents.
   - **Cadrage des objectifs** : Établir une liste de ce que vous souhaitez obtenir avec votre modèle (ex. la prédiction d’émotion pour chaque chanson, l’analyse de l’évolution émotionnelle dans une playlist, etc.).

#### **2. Collecte des données de paroles**
   - **Rechercher des datasets de chansons étiquetées par émotion** :
     - Par exemple, des plateformes comme *Genius Lyrics*, *Lyrics.com*, ou des bases de données open-source. Recherchez des datasets de paroles annotés pour une émotion spécifique.
     - Alternativement, téléchargez un dataset de paroles générales et envisagez de l’étiqueter vous-même avec des émotions si aucun dataset étiqueté n’est disponible.
   - **Sources de datasets annotés** : Explorez des corpus comme le *Dataset of Lyrics with Emotions* ou *GoEmotions* de Google (même si celui-ci ne concerne pas les chansons, il peut aider à enrichir votre vocabulaire émotionnel).

#### **3. Prétraitement des données textuelles**
   - **Nettoyage de texte** :
     - **Suppression des éléments non pertinents** : Enlever la ponctuation, les caractères spéciaux, les nombres, et les mots de remplissage ("oh", "ah", etc.) qui n'apportent pas d'information émotionnelle.
     - **Normalisation** : Convertir tous les mots en minuscules pour uniformiser le texte.
   
   - **Tokenisation et Lemmatisation** :
     - **Tokenisation** : Découper chaque chanson en mots ou en phrases.
     - **Lemmatisation** : Transformer chaque mot en sa racine pour uniformiser les termes (par exemple, "aimait", "aimer" deviennent "aime").
     - Utilisez des bibliothèques comme *NLTK* ou *spaCy* pour effectuer la tokenisation et la lemmatisation.

   - **Suppression des stop words** : Filtrer les mots les plus fréquents qui n’ajoutent pas de valeur émotionnelle (ex. "le", "de", "et"). Assurez-vous que la liste des stop words exclut les mots à potentiel émotionnel.

#### **4. Création d’un lexique d’émotions pour la base des émotions choisies**
   - **Construire un lexique émotionnel** :
     - Établir une liste de mots associés à chaque émotion (ex. "heureux", "sourire", "joie" pour la joie ; "triste", "perdu", "pleurer" pour la tristesse, etc.).
     - S’appuyer sur des lexiques préexistants comme le *NRC Emotion Lexicon* pour un vocabulaire large et étiqueté, que vous pourrez adapter à des paroles de chansons.
     - Tester les mots du lexique sur un petit échantillon de données pour vérifier leur pertinence dans un contexte de chanson.

   - **Raffinement du lexique pour chaque émotion** :
     - Ajouter des synonymes ou variantes de mots-clés pertinents au contexte musical.
     - Si certains mots-clés sont trop courants et ambigus dans les chansons, affinez le lexique en priorisant des mots spécifiques et représentatifs.

#### **5. Préparer la structure des données pour le modèle**
   - **Structurer les données** :
     - Créer un tableau avec les colonnes suivantes pour chaque chanson : *ID de la chanson*, *Paroles nettoyées*, *Emotion annotée* (si disponible), et *ID d'émotion (pour la classification)*.
     - Diviser les chansons en jeu d’entraînement et de test pour les phases ultérieures de modélisation.

   - **Équilibrage du dataset** :
     - Vérifiez si chaque émotion est représentée équitablement dans les données. Si une émotion est surreprésentée, vous pouvez effectuer un échantillonnage aléatoire ou utiliser une technique de sur-échantillonnage.

#### **6. Validation des données et vérifications finales**
   - **Vérifier la qualité des données** :
     - Analyser manuellement un échantillon pour s'assurer que les paroles et les annotations sont bien alignées avec les émotions prévues.
     - Nettoyer les incohérences restantes, comme les morceaux ayant peu de contenu émotionnel clair, pour éviter des prédictions erronées.
   - **Révisions finales** :
     - Faire un dernier contrôle de qualité sur le lexique émotionnel, le nettoyage de texte, et la structure des données avant de passer à la phase de modélisation.

Fin de semaine: disposer de données propres et structurées, prêtes à être utilisées pour la modélisation d’émotions dans les paroles.
