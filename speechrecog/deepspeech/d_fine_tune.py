import subprocess
import os
import pandas as pd
import csv
#import tensorflow as tf
#tf.compat.v1.disable_eager_execution()
#creating dtaa frame with target transcripts
DATA_TEXT=os.getcwd()+"/transcript/"
trans=[]
txt_name=[]
for path in os.listdir(DATA_TEXT):
    with open(DATA_TEXT + path[:-4] + ".txt", "r") as s:
        trans.append(s.read())
        txt_name.append(path)

df_target=pd.DataFrame()
df_target['file name']=txt_name
df_target['transcript']=trans
df_target.to_pickle("/home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/target_transcripts.pk")

data=pd.read_pickle("dpspeech.pkl")
rows=len(data)
file_stats=[]
DATA_DIR = os.getcwd()+ "/wav/"
for f in os.listdir(DATA_DIR):
    file_stats.append(os.stat(DATA_DIR+f).st_size)
data['file_size']=file_stats[:99]
FIELDNAMES = ["wav_filename", "wav_filesize", "transcript"]
target_csv="train.csv"
with open(target_csv, "w", encoding="utf-8", newline="") as target_csv_file:
    writer = csv.DictWriter(target_csv_file, fieldnames=FIELDNAMES)
    writer.writeheader()
    #bar = progressbar.ProgressBar(max_value=len(rows), widgets=SIMPLE_BAR)
    for w1,v,w2,t in zip(data['wav'],data['file_size'],df_target['file name'], df_target['transcript']):
        if (w1[:-4]==w2[:-4]):
            writer.writerow(
                {
                    "wav_filename": DATA_DIR+w1,
                    "wav_filesize":v,
                    "transcript": t
                }
            )
subprocess.check_output("python3 /home/anwesha/DeepSpeech/DeepSpeech.py "
                        "--alphabet_config_path /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/alphabet.txt "
                        "--save_checkpoint_dir /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/checkpoint "
                        "--dropout_rate 0.5 "
                        "--train_files /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/train.csv",shell=True)
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