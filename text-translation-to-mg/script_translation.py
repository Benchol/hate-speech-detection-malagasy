# -*- coding: utf-8 -*-
"""translate_to_mg.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k_67S1GyHbaSfObRrw2e9Ns1wSq4ZHfC
"""

# -*- coding: utf-8 -*-
"""Hate Speech - TextTraslationToMg.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vzoa-oZphVH-qMU0D1LmP6OQreaP76f_

### Script for translating text (en) to Malagasy (mg) using the MADLAD-400-7B-MT-BT model.
"""

import subprocess
import sys
import os

def install_package(package_name):
    """Install or update a Python package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", package_name])
        print(f"Package '{package_name}' successfully installed/updated.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing package '{package_name}': {e}")
        return False

# Install required packages
# install_package('tqdm')
# install_package('pandas')
install_package("bitsandbytes")
# install_package('transformers')
# install_package('torch')
# install_package('wandb')
# install_package('gdown')

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
import torch
from tqdm.auto import tqdm
import wandb
import argparse
import gdown

# Define script arguments
parser = argparse.ArgumentParser(description='Translate a portion of a CSV file using MADLAD-400-7B-MT-BT.')
parser.add_argument('--start_index', type=int, default=0, help='Starting row index (inclusive).')
parser.add_argument('--end_index', type=int, default=10000, help='Ending row index (exclusive).')
parser.add_argument('--batch_size', type=int, default=16, help='Batch size for translation.')
parser.add_argument('--file_id', type=str, required=True, help='Public Drive file ID')
args = parser.parse_args()

start_index = args.start_index
end_index = args.end_index
batch_size = args.batch_size
file_id = args.file_id

# Check for GPU availability
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load MADLAD-400-7B-MT-BT model with 8-bit quantization
model_name = "google/madlad400-7b-mt-bt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, load_in_8bit=True, device_map='auto')

# Download CSV file from Google Drive
local_file_name = f"downloaded_data_{file_id}.csv"
try:
    print(f"Downloading file from {file_id}...")
    file_url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(file_url, local_file_name, quiet=False)
    file_path = local_file_name
    df = pd.read_csv(file_path)
    print("CSV file successfully downloaded and loaded.")
except Exception as e:
    print(f"Error downloading/loading CSV file from URL: {e}")
    exit()

# Verify 'text' column exists
if 'text' not in df.columns:
    print("Error: 'text' column not found in CSV file.")
    exit()

# Select portion of DataFrame to process
df_subset = df[start_index:end_index]
print(f"Processing rows {start_index} to {end_index - 1} in batches of {batch_size}.")

def translate_batch(texts):
    """Translate a batch of texts to Malagasy"""
    input_texts = [f"<2mg> {text}" for text in texts]
    inputs = tokenizer(input_texts, return_tensors="pt", padding=True, truncation=True).to(device)
    with torch.no_grad():
        generated_tokens = model.generate(
            **inputs,
            max_length=512
        )
    translated_texts = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return translated_texts

translations = [''] * len(df_subset)

# --- WandB Configuration ---
WANDB_API_KEY = "*******************************"
os.environ["WANDB_API_KEY"] = WANDB_API_KEY  # Set environment variable for WandB

# Initialize WandB
wandb.init(project="hate-speech-translated-malagasy", name=f"translation-run-{start_index}-{end_index}")
# --- End of WandB Configuration ---

total_batches = len(df_subset) // batch_size + (1 if len(df_subset) % batch_size != 0 else 0)

# Process translation in batches with progress bar and WandB tracking
for i in tqdm(range(0, len(df_subset), batch_size), desc=f"Translating ({start_index}-{end_index})"):
    batch = df_subset['text'][i:i + batch_size].tolist()
    translated_batch = translate_batch(batch)
    translations[i:i + batch_size] = translated_batch

    batch_number = i // batch_size + 1
    wandb.log({"progress": batch_number / total_batches * 100,
               "lines_processed": i + len(batch)})

# Add translations as new column
df_subset['translated'] = translations

# Create WandB table with original text, label and translation
wandb_table = wandb.Table(data=df_subset[['text', 'label', 'translated']], columns=["text", "label", "translated"])

# Log table to WandB
wandb.log({"translations_segment": wandb_table})

# Finish WandB run
wandb.finish()