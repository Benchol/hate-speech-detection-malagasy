# 🔍 Détection de discours haineux en malgache avec TF-IDF + XGBoost / Naive Bayes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Classification automatique des discours haineux en malgache en utilisant des méthodes classiques de machine learning basées sur la vectorisation TF-IDF.

---

## Fonctionnalités principales

- 🧠 **Deux modèles testés** :
  - `XGBoostClassifier` (avec gestion du déséquilibre via `scale_pos_weight`)
  - `Multinomial Naive Bayes` (avec SMOTE)
- 🔤 **Vectorisation TF-IDF** avec n-grammes (1 à 4)
- 💬 **Augmentation ciblée des textes** avec des mots-clés haineux malgaches
- 📊 **Évaluations complètes** : Accuracy, Rapport de classification, Matrice de confusion, Courbe ROC
- 🧪 **Fonction de test interactif** de phrases

---

## Prétraitement et pipeline

1. 🔧 Nettoyage des textes (URLs, chiffres, mots inutiles)
2. 📈 Répétition pondérée des mots-clés haineux (`list.json`)
3. ✂️ Séparation train/test (80/20)
4. 📐 Vectorisation avec `TfidfVectorizer` (ngram_range=(1,4))
5. 🔁 Entraînement :
   - `XGBoost` avec `scale_pos_weight`
   - `Naive Bayes` avec `SMOTE` pour équilibrer les classes
6. 📊 Évaluation complète

---

## Architecture technique

```python
                Texte brut
                    ↓
            Nettoyage + Augmentation
                    ↓
    TF-IDF (n-grammes 1-4, max_features=10000)
                    ↓
     ┌─────────────┐           ┌─────────────┐
     │  XGBoost    │   ou      │ Naive Bayes │
     └─────────────┘           └─────────────┘
                    ↓
 Prédiction binaire (0 = Non-haineux, 1 = Haineux)
