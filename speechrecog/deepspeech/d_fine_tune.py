import subprocess
import os
import pandas as pd
import csv
#import tensorflow as tf
#tf.compat.v1.disable_eager_execution()
data=pd.read_pickle("dpspeech.pkl")
rows=len(data)
file_stats=[]
DATA_DIR = os.getcwd()+ "/wav/"
for f in os.listdir(DATA_DIR):
    file_stats.append(os.stat(DATA_DIR+f).st_size)
data['file_size']=file_stats[:9]
FIELDNAMES = ["wav_filename", "wav_filesize", "transcript"]
target_csv="train.csv"
with open(target_csv, "w", encoding="utf-8", newline="") as target_csv_file:
    writer = csv.DictWriter(target_csv_file, fieldnames=FIELDNAMES)
    writer.writeheader()
    #bar = progressbar.ProgressBar(max_value=len(rows), widgets=SIMPLE_BAR)
    for w,v,t in zip(data['wav'],data['file_size'],data['transcript']):
        writer.writerow(
            {
                "wav_filename": DATA_DIR+w,
                "wav_filesize":v,
                "transcript": t,
            }
        )
subprocess.check_output("python3 /home/anwesha/DeepSpeech/DeepSpeech.py "
                             "--alphabet_config_path /home/anwesha/speechrecog/deepspeech/alphabet.txt "
                             "--n_hidden 2 "
                             "--save_checkpoint_dir /home/anwesha/speechrecog/deepspeech/checkpoint "
                             "--dropout_rate 0.5 "
                             "--train_files train.csv "
                             "--drop_source_layers 2 "
                             "--train_cudnn",shell=True)
#python3 DeepSpeech.py --train_files ../data/CV/en/clips/train.csv --dev_files ../data/CV/en/clips/dev.csv --test_files ../data/CV/en/clips/test.csv
#"--n_hidden 2048 "
#"--learning_rate 0.0001 "
#"--epochs 1 "
#"--test_files test "
#--alphabet_config_path /home/anwesha/speechrecog/deepspeech/alphabet.txt "
#"--dropout_rate 0.1 "
#"--dropout_rate2 0.2 "
#"--dropout_rate3 0.3 "
#"--dropout_rate4 0.4 "
#"dropout_rate5 0.5 "
#"dropout_rate6  0.6 "