%%bash
#!/bin/bash

echo "Début de l'exécution du fine-tuning mBERT..."

python finetuning_mbert.py \
    --train_file_id "1DL04tjtLOByQQCAPrr0lysa5aiwlhuGB" \
    --test_file_id "1DUVUq7JRAzuKowSyj8A31nnltDhq6cQS" \
    --batch_size "8" \
    --epochs "5" \
    --learning_rate "0.001" \
    --wandb_project "hate_speech_detection_mBERT" \
    --wandb_name "finetuning_v1" \
    --wandb_key "00623049297b4d6a9b3febd02306cf1294021a68"

echo "Fine-tuning mBERT terminé."