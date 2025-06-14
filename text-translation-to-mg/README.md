# Script de Traduction Anglais-Malgache (en-mg)

## Description
Script Python pour traduire du texte anglais vers le malgache en utilisant le modèle MADLAD-400-7B-MT-BT de Google. Le traitement se fait par lots avec suivi via WandB.

## 📦 Dépendances
```bash
pip install transformers torch bitsandbytes pandas tqdm wandb gdown
```

## 📌 Paramètres du script

| Argument          | Description                                            |
|-------------------|--------------------------------------------------------|
| `--file_id`       | ID du fichier sur Google Drive                         |
| `--start_index`   | Index de la première ligne à traiter (incluse)         |
| `--end_index`     | Index de la dernière ligne à traiter (exclue)          |
| `--batch_size`    | Nombre de textes à traduire simultanément              |

## Exemples d'utilisation

```bash
#!/bin/bash
python script_translation.py \
  --file_id ID_GOOGLE_DRIVE \
  [--start_index 0] \
  [--end_index 10000] \
  [--batch_size 16]
```

## ⚡ Exécution Parallèle

Le projet inclut un script bash pour lancer les traductions en parallèle :

**Fichier** : `run_translation.sh`

### Exemple d'utilisation
```bash
chmod +x run_translation.sh  # Rendre le script exécutable
./run_translation.sh         # Lancer toutes les traductions
```