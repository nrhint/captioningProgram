#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import subprocess
import srt
import json
import datetime

SetLogLevel(-1)

if not os.path.exists("./VTT/model"):
    print("Trying to download voice model, this is a one time thing and may take a while...")
    try:
        if not os.path.exists("./VTT/model.zip"):
            import urllib.request
            print("Downloading...")
            urllib.request.urlretrieve("https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip", "./VTT/model.zip")
        import zipfile
        import platform
        print("Extracting...")
        with zipfile.ZipFile("./VTT/model.zip", 'r') as zip_ref:
            zip_ref.extractall("./VTT/")
        ##Rename the folder:
        files = os.listdir('./VTT')
        for file in files:
            if 'model' in file and '.zip' not in file:
                if platform.system() == "Windows":
                    status = subprocess.call('copy %s model /e'%('./VTT/'+file), shell=True)
                else:
                    status = subprocess.call('cp -r %s %s'%(os.getcwd()+'/VTT/'+file+"", os.getcwd()+'/VTT/model'), shell=True)

        print("Finished")
    except Exception:
        print(Exception)
        print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit (1)

sample_rate=16000
model = Model("./VTT/model")
rec = KaldiRecognizer(model, sample_rate)
rec.SetWords(True)


process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            sys.argv[0],
                            '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                            stdout=subprocess.PIPE)


WORDS_PER_LINE = 7

def transcribe():
    results = []
    subs = []
    while True:
       data = process.stdout.read(4000)
       if len(data) == 0:
           break
       if rec.AcceptWaveform(data):
           results.append(rec.Result())
    results.append(rec.FinalResult())

    for i, res in enumerate(results):
       jres = json.loads(res)
       if not 'result' in jres:
           continue
       words = jres['result']
       for j in range(0, len(words), WORDS_PER_LINE):
           line = words[j : j + WORDS_PER_LINE] 
           s = srt.Subtitle(index=len(subs), 
                   content=" ".join([l['word'] for l in line]),
                   start=datetime.timedelta(seconds=line[0]['start']), 
                   end=datetime.timedelta(seconds=line[-1]['end']))
           subs.append(s)
    return subs

print (srt.compose(transcribe()))
