# 🧠 Détection de discours haineux en malgache

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ce projet a pour objectif la détection automatique de discours haineux en langue malgache à partir de données textuelles. Il utilise des modèles de traitement du langage naturel multilingues et pré-entraînés, adaptés pour la classification binaire (haineux vs non-haineux).

---

## 🔍 Objectifs

- Étudier l’efficacité de **modèles multilingues pré-entraînés** (mT5, mBERT) pour la classification de textes haineux en malgache.
- Construire un **corpus annoté** de discours malgaches provenant de traductions et de données sociales réelles.
- Évaluer différentes stratégies de fine-tuning et de gestion du déséquilibre des classes.

---

## 🧾 Données

Le corpus est composé de deux sources :
1. ✅ **Données traduites** : Traduction en malgache de datasets publics (HateXplain, DGHD, slur-corpus, HateCheck, OLID, SWAD, Labeled_data, twitter_sexism, twitter_racism) via MadLab-7B-MT-BT.
2. 🗣️ **Données Facebook Malagasy** : Scrappées manuellement sur des publications ciblés, nettoyées et annotées manuellement.

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

### 🔶 mBERT (bert-base-multilingual-cased)

- [CLS] token → Classifieur 768 → 256 → 2
- Utilise la **CrossEntropyLoss standard**
- Fine-tuning classique sur les mêmes données

📂 Dossier : `mbert_finetuning/`

## 🧪 Suivi des expériences

- Suivi complet avec **Weights & Biases (wandb)**
- Visualisations : matrices de confusion, courbes ROC et Precision-Recall
- Sauvegarde automatique des meilleurs modèles

---

