%%bash
#!/bin/bash

echo "Début de l'exécution des traductions parallèles..."

# --- Traduction 1: Dataset HateSpeechDataset(nbre_rows = 440.906) (Attention: j'ai déjà fini la traduction jusqu'à l'index 130.000)
python script_translation.py \
    --start_index 130000 \
    --end_index 440905 \
    --batch_size 32 \
    --file_id "1phccMgk_1KxNsCkcigjhkHM44w7Qy_Aa" &

# --- Traduction 2: DataSet HateXplainDataset(nbre_rows = 19.229)
python script_translation.py \
    --start_index 0 \
    --end_index 19228 \
    --batch_size 32 \
    --file_id "1NIavkN5INEV68cOpgfH6iUXrc7aAvzTa" &

# --- Traduction 3: DataSet Kurrek Slur Corpus(nbre_rows = 40.003)
python script_translation.py \
    --start_index 0 \
    --end_index 40002 \
    --batch_size 32 \
    --file_id "1171e_GbrxhU8k9kDUpTp-8LolqjioDCo" &

# --- Traduction 4: DataSet Tweet racism(nbre_rows = 13.471)
python script_translation.py \
    --start_index 0 \
    --end_index 13470 \
    --batch_size 32 \
    --file_id "1--V-kyXYA88hwW5dqwbgK8CbyUxBVrkX" &

# --- Traduction 5: DataSet OLID(nbre_rows = 13.240)
python script_translation.py \
    --start_index 0 \
    --end_index 13239 \
    --batch_size 32 \
    --file_id "1-7rs2hYnzSZ76AxTFOKnend97QHh9qUS" &

# --- Traduction 6: DataSet DynamicallyGeneratedHateDataset (nbre_rows = 40.622)
python script_translation.py \
    --start_index 0 \
    --end_index 40621 \
    --batch_size 32 \
    --file_id "1-7ziVqFY-4zUwHoZ_NIkxFGYmDEevr-p" &

# --- Traduction 7: DataSet HateCheck (nbre_rows = 3.729)
python script_translation.py \
    --start_index 0 \
    --end_index 3728 \
    --batch_size 32 \
    --file_id "1gQdh4M_2cU_3S0Jbee23pL5Rb73boLcR" &

# --- Attente de la fin de toutes les tâches ---
wait
echo "Toutes les tâches de traduction sont terminées."