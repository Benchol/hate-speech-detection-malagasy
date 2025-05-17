%%bash
#!/bin/bash

echo "Début de l'exécution des traductions..."

# Exemple pour traiter les lignes 0 à 999 avec un batch size de 8
python script_translation.py --start_index 0 --end_index 1000 --batch_size 8 &

# Exemple pour traiter les lignes 1000 à 1999 avec un batch size de 8
python script_translation.py --start_index 1000 --end_index 2000 --batch_size 8 &

wait # Attend que tous les processus en arrière-plan se terminent
echo "Toutes les tâches de traduction sont terminées."