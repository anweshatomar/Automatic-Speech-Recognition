import subprocess
import os

if "wav" not in os.listdir():
    os.system("wget https://storage.googleapis.com/speechrecogdata/wav.zip")
    os.system("unzip wav.zip")
DATA_DIR=os.getcwd()+"/wav/"
train,test=[],[]
#train=['/home/anwesha/speechrecog/deepspeech/wav/arctic_a0001.wav']
#test=['/home/anwesha/speechrecog/deepspeech/wav/arctic_a0008.wav']
for f in os.listdir(DATA_DIR):
    train.append(DATA_DIR+f)
    test.append(DATA_DIR+f)
print(len(train), len(test))
print(os.getcwd())
subprocess.check_output("python3 /home/anwesha/DeepSpeech/DeepSpeech.py "
                             "--alphabet_config_path /home/anwesha/speechrecog/deepspeech/alphabet.txt "
                             "--n_hidden 2048 "
                             "--save_checkpoint_dir /home/anwesha/speechrecog/deepspeech/checkpoint "
                             "--train_files train.csv "
                             "--dropout_rate 0.1 ",shell=True)

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