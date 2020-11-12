import os
import pandas as pd
import subprocess
import pandas as pd
from jiwer import wer


if "wav" not in os.listdir():
    os.system("wget https://storage.googleapis.com/speechrecogdata/wav.zip")
    os.system("unzip wav.zip")

if "trancript" not in os.listdir():
    os.system("wget https://storage.googleapis.com/speechrecogdata/trancript.zip")
    os.system("unzip trancript.zip")

DATA_DIR = os.getcwd()+ "/wav/"
val=len([name for name in os.listdir(DATA_DIR)])
df=pd.DataFrame()
g_trans=[]
g_name=[]
error=[]
os.chdir("/home/anwesha/")
for i in range(1,val):
   temp=subprocess.check_output("deepspeech --model deepspeech-0.8.1-models.pbmm "
                                           "--scorer deepspeech-0.8.1-models.scorer "
                                       "--audio /home/anwesha/speechrecog/deepspeech/wav/arctic_a000{}.wav".format(i),shell=True)
   temp=str(temp)
   n_line='\n'
   n_line=str(n_line)
   temp=temp.lstrip("b").strip("'").strip(n_line)
   g_trans.append(temp)
   g_name.append("arctic_a000{}.wav".format(i))


df['wav']=g_name[:9]
df['transcript']=g_trans
print(df)

os.chdir("/home/anwesha/speechrecog/deepspeech/")
DATA_DIR = os.getcwd()+ "/trancript/"


for f in os.listdir(DATA_DIR):
    for i in range (len(df)):
        temp = df['wav'][i]
        if (f[:-4]== temp[:-4]):
           error.append(wer(DATA_DIR + f, df['transcript'][i]))
print(error)