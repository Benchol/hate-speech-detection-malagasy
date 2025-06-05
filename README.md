# 🧠 Détection de discours haineux en malgache

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ce projet a pour objectif la détection automatique de discours haineux en langue malgache à partir de données textuelles. Il utilise à la fois des modèles multilingues pré-entraînés (mT5, mBERT) et des approches classiques basées sur TF-IDF.

---

## 🔍 Objectifs

- Étudier l’efficacité de **modèles multilingues pré-entraînés** (mT5, mBERT) pour la classification de textes haineux en malgache.
- Évaluer des **méthodes classiques** de machine learning (TF-IDF + XGBoost / Naive Bayes).
- Construire un **corpus annoté** de discours malgaches provenant de traductions et de données sociales réelles.
- Comparer différentes stratégies de fine-tuning et de gestion du déséquilibre des classes.

---

## 🧾 Données

Le corpus est composé de deux sources :
1. ✅ **Données traduites** : Traduction en malgache de datasets publics (HateXplain, DGHD, slur-corpus, HateCheck, OLID, SWAD, Labeled_data, twitter_sexism, twitter_racism) via MadLab-7B-MT-BT.
2. 🗣️ **Données Facebook Malagasy** : Scrappées manuellement sur des publications ciblées, nettoyées et annotées manuellement.

Les données combinées comportent :
- ~25,000 exemples
- ≈32.5% de discours haineux

---

## 🧠 Modèles fine-tunés

### 🔷 mT5-small

- Encoder de mT5 avec **Mean Pooling**
- Classifieur 512 → 256 → 2
- Utilise la **Focal Loss** pour gérer le déséquilibre
- Apprentissage supervisé sur données combinées

📂 Dossier : `mt5_finetuning/`

---

### 🔶 mBERT (bert-base-multilingual-cased)

- [CLS] token → Classifieur 768 → 256 → 2
- Utilise la **CrossEntropyLoss standard**
- Fine-tuning classique sur les mêmes données

📂 Dossier : `mbert_finetuning/`

---

### 🟡 TF-IDF + XGBoost / Naive Bayes

- Vectorisation avec **TF-IDF** (n-grammes 1 à 4)
- Deux modèles :
  - `XGBoostClassifier` avec `scale_pos_weight`
  - `MultinomialNB` avec suréchantillonnage SMOTE
- Augmentation des textes avec répétition pondérée des mots-clés haineux
- Courbes ROC, matrice de confusion, tests interactifs

📂 Dossier : `tfidf_models/`

---

## 🧪 Suivi des expériences

- 🔎 Suivi via **Weights & Biases (wandb)** pour les modèles fine-tunés
- 📊 Visualisations :
  - Matrices de confusion
  - Courbes ROC et Precision-Recall
  - Évolution des pertes et métriques
- 💾 Sauvegarde automatique des meilleurs checkpoints

---
