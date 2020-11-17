#google-api
sudo -H pip3 install --upgrade google-cloud-speech
# deepespeecg-pretrain
sudo -H pip3 install deepspeech
sudo -H pip3 install deepspeech-gpu

wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.pbmm
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.scorer
#WER
sudo -H pip3 install jiwer
#sox
sudo apt-get install sox
# deepspeech fine-tune
cd ~
git clone --branch v0.9.1 https://github.com/mozilla/DeepSpeech
cd DeepSpeech
pip3 install --upgrade pip==20.2.2 wheel==0.34.2 setuptools==49.6.0
pip3 install --upgrade -e .