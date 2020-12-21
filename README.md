# Automatic-Speech-Recognition:

The repository consists of two folders, one for transcribing wav files using Google API and the second to transcribe wav files using Mozilla DeepSpeech 2.0.

Installing necessary files:
```
mv install.sh ~
```
```
cd ~
```
```
chmod +x install.sh
```
```
sudo ./install.sh
```
#### Description of project:

In this project, automatic speech recognition is implemented using Google Speech to Text API
and Mozilla Deepspeech 2.0 in order to transcribe text from speech. The LM arctic data set
non-native English speech is used for training and testing the model. This dataset consists
of speakers who have Arabic, Madrid, Vietnamese, Hindi, Spanish and Korean as their first
language. The dataset is preprocessed and then input into the pre-trained model of
Deepspeech and Google Speech to Text API.


#### Results:

WER of Google Speech to text API: 9.06

WER of Mozilla DeepSpeech 2.0 Pre-Trained Model: 8.73

The Deepspeech model performs better, therefore we continue with improving and fine tuning
this model.
