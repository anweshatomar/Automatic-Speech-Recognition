import re
import os
import pandas as pd
import csv
import unicodedata
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
    for i in range(0,len(data['wav'])):
        for j in range(0,len(df_target['file name'])):
            t1=data['wav'][i]
            t2=df_target['file name'][j]
            if (t1[:-4] == t2[:-4]):
                data['transcript'][i]=(df_target['transcript'][j].lower())
    #bar = progressbar.ProgressBar(max_value=len(rows), widgets=SIMPLE_BAR)
    for w1,v,t in zip(data['wav'],data['file_size'],data['transcript']):
        writer.writerow(
                {
                    "wav_filename": DATA_DIR+w1,
                    "wav_filesize":v,
                    "transcript": t,
                }
            )