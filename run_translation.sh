#!/bin/bash

# Traduire les lignes 0 à 999 avec un batch size de 16
python hate_speech_texttraslationtomg.py --start_index 0 --end_index 1000 --batch_size 16 &

# Traduire les lignes 1000 à 1999 avec un batch size de 16
python hate_speech_texttraslationtomg.py --start_index 1000 --end_index 2000 --batch_size 16 &

# Traduire les lignes 2000 à 2999 avec un batch size de 16
python hate_speech_texttraslationtomg.py --start_index 2000 --end_index 3000 --batch_size 16 &

wait # Attend que tous les processus en arrière-plan se terminent
echo "Toutes les tâches de traduction sont terminées."