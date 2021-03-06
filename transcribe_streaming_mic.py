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

# [START import_libraries]
from __future__ import division

import re
import sys
import serial
from datetime import datetime

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue
# [END import_libraries]

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

# [START def_sheetdasu]
def sheetdasu(ohgoe):
    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x06)) # 0x00 - 0x2F
    ser.write("新しいものづくりがわかるメディア\r\r")
    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write(chr(0x1C)) # 0x1C
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x0C)) # 0x00 - 0x2F
    ser.write("fabcross\r")
    ser.write(chr(0x1C)) # 0x1C
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write("\r");  # Line Feed
    date = datetime.today().strftime("%Y年%m月%d日 %H:%M")
    ser.write(date)
    ser.write("\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x26)) # 0x00 - 0x2F
    ser.write("担:01\r\r\r\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x28)) # 0x00 - 0x2F
    ser.write("様\r")

    ser.write("-----------------------------\r")
    ser.write("大きい声　　　　　　　　数量 1\r\r\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write("内容\r\r")
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write(chr(0x1C)) # 0x1C
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write(ohgoe)
    ser.write(chr(0x1C)) # 0x1C
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write("\r（内うるさい度　　　　100）\r\r\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x68)) # 0x68
    ser.write(chr(0x00)) # 0x00 or 01 or 02 or 03
    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x1D)) # 0x00 - 0x2F
    ser.write("レシート No.012\r")
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x68)) # 0x68
    ser.write(chr(0x01)) # 0x00 or 01 or 02 or 03
    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write("-----------------------------\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x04)) # 0x00 - 0x2F
    ser.write("》》》 記事見てね！《《《\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x4A)) # 0x4A
    ser.write(chr(0x10)) # 0xXX
    ser.write("記事はこちら！！\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x68)) # 0x68
    ser.write(chr(0x00)) # 0x00 or 01 or 02 or 03
    ser.write("\rhttps://fabcross.jp/list/series/sorepi/\r\r")
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x68)) # 0x68
    ser.write(chr(0x01)) # 0x00 or 01 or 02 or 03

    ser.write("[それ、ラズパイでつくれるよ]\rで検索！\r")
    ser.write("\r\r");  # Line Feed

    # QRcode Print
    ser.write(chr(0x1D))
    ser.write(chr(0x79))
    ser.write(chr(0x01))
    ser.write(chr(0x1D))
    ser.write(chr(0x78))
    ser.write(chr(0x4C))
    ser.write(chr(0x27))
    ser.write("https://fabcross.jp/list/series/sorepi/")   # DATA
    ser.write("\r\r\r\r\r\r");  # Line Feed
# [END def_sheetdasu]

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)
# [END audio_stream]


def listen_print_loop(responses):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = ' ' * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + '\r')
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)
            encoded = transcript.encode('utf-8')
            sheetdasu(encoded)

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('Exiting..')
                break

            num_chars_printed = 0


def main():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = 'ja-JP'  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses)


if __name__ == '__main__':
    main()
