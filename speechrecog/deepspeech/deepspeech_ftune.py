import subprocess
subprocess.check_output("python3  /home/anwesha/DeepSpeech/DeepSpeech.py "
                        "--audio_sample_rate 16000 "
                        "--alphabet_config_path /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/alphabet.txt "
                        "--save_checkpoint_dir /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/checkpoint "
                        "--dropout_rate 0.05 "
                        "--train_files /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/train.csv "
                        "--export_dir /home/anwesha/Automatic-Speech-Recognition/speechrecog/deepspeech/models",shell=True)