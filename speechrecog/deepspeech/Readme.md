# Order of running files:
Dowloading the data:
```
chmod +x data.sh
```
```
sudo ./data.sh
```

Next we run the preprocessing file in order to convert the sample rate from 44100 to 16000:

```
python3 preprocess_data.py
```

Then we run the transcribe file this generates two .pkl files one for WER and one to store transcribed files to a dataframe:

```
python3 trascribe_d.py
```

In order to fine tune to the DeepSpeech model, we have to run two files:
- create_csv.py: generate CSV file needed for fine tuning, generates train.csv
- check_char.py: generate alphabet for fune tuning, generates alphabet.txt

```
python3 create_csv.py
```
```
python3 check_char.py
```

Running DeepSpeech fine tuning file(currently not working):
```
python3 deepspeech_ftune.py
```
