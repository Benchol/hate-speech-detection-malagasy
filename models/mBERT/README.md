# Détection de discours haineux en malgache avec mBERT

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Modèle de classification fine-tuné à partir de BERT multilingue (mBERT) pour détecter automatiquement les discours haineux en langue malgache à partir de publications Facebook.

---

## Fonctionnalités principales

- 🤖 **Modèle basé sur mBERT (bert-base-multilingual-cased)** fine-tuné
- ⚖️ **Gestion du déséquilibre des classes** (32.5% de haineux) via **pondération de la loss**
- 📊 **Métriques complètes** : Accuracy, Précision, Recall, F1, ROC-AUC
- 📈 **Visualisations** : Matrices de confusion, courbes ROC/Precision-Recall
- 🧪 **Évaluation rigoureuse** sur jeux de test en malgache
- 💾 **Sauvegarde & Restauration** automatique du meilleur modèle

---

## Architecture technique

```python
BertModel → [CLS] token → Classifieur (768 → 256 → 2) → CrossEntropyLoss (pondérée)
```

## Exemples d'utilisation

```bash
#!/bin/bash
python finetuning_mbert.py \
    --train_file_id FILE_TRAIN_ID \
    --test_file_id FILE_TEST_ID \
    --batch_size BATCH_SIZE \
    --epochs EPOCH \
    --learning_rate LEARNING_RATE \
    --wandb_project WANDB_PROJECT \
    --wandb_name WANDB_NAME \
    --wandb_key WANDB_KEY
```
