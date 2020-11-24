import os
import subprocess
import sox
import warnings
warnings.simplefilter("ignore")

#get path to wav files
DATA_DIR = os.getcwd()+ "/wav/"
#number of files in directory
print(DATA_DIR)
val=len([name for name in os.listdir(DATA_DIR)])
print(val)
os.chdir("/home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/wav")

for i in range(1,val):
    if (i>=1 and i<=9):
       filename="arctic_a000{}.wav".format(i)
       subprocess.check_output("sox "+filename+" -r 16000 "+filename,shell=True)
       #print(sox.file_info.sample_rate(filename))
    elif (i >= 10 and i <= 99):
        filename = "arctic_a00{}.wav".format(i)
        subprocess.check_output("sox " + filename + " -r 16000 " + filename, shell=True)
    elif (i >= 100 and i <= 999):
        filename = "arctic_a0{}.wav".format(i)
        subprocess.check_output("sox " + filename + " -r 16000 " + filename, shell=True)
