import os
from google.cloud import speech
import io
import pandas as pd
from jiwer import wer
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="envspeech.json"
def transcribe_file(speech_file):
    """Transcribe the given audio file."""

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        #print(u"Transcript: {}".format(result.alternatives[0].transcript))
        return result.alternatives[0].transcript
if __name__=="__main__":
    #data frame
    df=pd.DataFrame()
    g_trans=[]
    g_name=[]
    # extract data
    if "wav" not in os.listdir():
        os.system("wget https://storage.googleapis.com/speechrecogdata/wav.zip")
        os.system("unzip wav.zip")
    if "trancript" not in os.listdir():
        os.system("wget https://storage.googleapis.com/speechrecogdata/trancript.zip")
        os.system("unzip trancript.zip")
    DATA_DIR = os.getcwd()+ "/wav/"
    for f in os.listdir(DATA_DIR):
        if f[-4:] == ".wav":
            g_name.append(f)
            g_trans.append(transcribe_file(DATA_DIR+f))
    

    df['transcript'] = g_trans
    df['wav'] = g_name
    print(df)

    os.chdir("/home/anwesha/speechrecog/google_api/")
    DATA_DIR = os.getcwd() + "/trancript/"
    error=[]
    for f in os.listdir(DATA_DIR):
        for i in range(len(df)):
            temp=df['wav'][i]
            if (f[:-4]== temp[:-4]):
                error.append(wer(DATA_DIR + f, df['transcript'][i]))
    print(error)