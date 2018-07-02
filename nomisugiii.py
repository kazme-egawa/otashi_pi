#!/usr/bin/env python
# coding: utf-8

# Copyright 2018 Kazme Egawa. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pyaudio
import wave
import numpy as np
from datetime import datetime
import transcribe_sheet as reciept

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5

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
    # print np.max(x)
    if x.max() == threshold:
        print("Recording.")
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

        reciept.transcribe_file(filename)


stream.close()
p.terminate()
