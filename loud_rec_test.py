#!/usr/bin/env python

import pyaudio
import wave
import numpy as np
from datetime import datetime
from time import sleep

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 8

threshold = 1

p = pyaudio.PyAudio()

imput_device_index = 0
stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    frames_per_buffer = chunk
)

cnt = 0

while True:
    data = stream.read(chunk)
    x = np.frombuffer(data, dtype="int16") / 32767
    print np.max(x)
    if x.max() == threshold:
        filename = datetime.today().strftime("%Y%m%d%H%M%S") + ".wav"
        print(x.max(), cnt, filename)

        all = []
        all.append(data)
        for i in range(0, int(RATE / chunk * int(RECORD_SECONDS))):
            data = stream.read(chunk)
            all.append(data)
        data = b''.join(all)

        out = wave.open(filename,'w')
        out.setnchannels(CHANNELS)
        out.setsampwidth(2)
        out.setframerate(RATE)
        out.writeframes(data)
        out.close()

        print("Saved.")

        cnt += 1
    if cnt > 5:
        break

stream.close()
p.terminate()
