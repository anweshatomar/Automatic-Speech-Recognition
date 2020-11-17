import os
import pandas as pd
import subprocess
import pandas as pd
from jiwer import wer
import sox
#downloading wav files
if "wav" not in os.listdir():
    os.system("wget https://storage.googleapis.com/speechrecogdata/wav.zip")
    os.system("unzip wav.zip")
#downloading transcript files
if "transcript" not in os.listdir():
    os.system("wget https://storage.googleapis.com/speechrecogdata/transcript.zip")
    os.system("unzip transcript.zip")
#get path to wav files
DATA_DIR = os.getcwd()+ "/wav/"
#number of files in directory
val=len([name for name in os.listdir(DATA_DIR)])
#dataframe of files transcribed by deepspeech
df=pd.DataFrame()
df_error=pd.DataFrame()
g_trans=[]
g_name=[]
error=[]
error_trans=[]
#change the directory to acccess the deeepspeech mdoel
os.chdir("/home/anwesha/Automatic-Speech-Recognition/speechrecog/")
for i in range(1,val):
    if (i>=1 and i<=9):
       temp=subprocess.check_output("deepspeech --model deepspeech-0.8.1-models.pbmm "
                                               "--scorer deepspeech-0.8.1-models.scorer "
                                           "--audio /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/wav/arctic_a000{}.wav".format(i),shell=True)
       temp=str(temp)
       n_line='\n'
       n_line=str(n_line)
       temp=temp.lstrip("b").strip("'").strip(n_line)
       g_trans.append(temp)
       g_name.append("arctic_a000{}.wav".format(i))
    elif (i>=10 and i<=99):
        temp = subprocess.check_output("deepspeech --model deepspeech-0.8.1-models.pbmm "
                                      "--scorer deepspeech-0.8.1-models.scorer "
                                      "--audio /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/wav/arctic_a00{}.wav".format(i),
                                      shell=True)
        temp = str(temp)
        n_line = '\n'
        n_line = str(n_line)
        temp = temp.lstrip("b").strip("'").strip(n_line)
        g_trans.append(temp)
        g_name.append("arctic_a00{}.wav".format(i))
    elif (i>=100 and i<=999):
        temp = subprocess.check_output("deepspeech --model deepspeech-0.8.1-models.pbmm "
                                      "--scorer deepspeech-0.8.1-models.scorer "
                                      "--audio /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/wav/arctic_a0{}.wav".format(i),
                                      shell=True)
        temp = str(temp)
        n_line = '\n'
        n_line = str(n_line)
        temp = temp.lstrip("b").strip("'").strip(n_line)
        g_trans.append(temp)
        g_name.append("arctic_a0{}.wav".format(i))
#assigning values to the data frame 
df['wav']=g_name
df['transcript']=g_trans
df.to_pickle("/home/anwesha/speechrecog/deepspeech/dpspeech.pkl")
print(df)
#access the transcripts 
os.chdir("/home/anwesha/speechrecog/deepspeech/")
DATA_DIR = os.getcwd()+ "/transcript/"
#Word error rate
for f in os.listdir(DATA_DIR):
    for i in range (len(df)):
        temp = df['wav'][i]
        if (f[:-4]== temp[:-4]):
            error_trans.append(temp)
            error.append(wer(DATA_DIR + f, df['transcript'][i]))
df_error['Wav']=error_trans
df_error['WER']=error
df_error.to_pickle("/home/anwesha/speechrecog/deepspeech/dpspeech_WER.pkl")
print(df_error)