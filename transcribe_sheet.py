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

"""Google Cloud Speech API sample application using the REST API for batch
processing.

Example usage:
    python transcribe.py resources/audio.raw
    python transcribe.py gs://cloud-samples-tests/speech/brooklyn.flac
"""

# [START import_libraries]
import argparse
import io
import serial
from datetime import datetime
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

# [START def_transcribe_file]
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_sync_request]
    # [START migration_audio_config_file]
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ja-JP')
    # [END migration_audio_config_file]

    # [START migration_sync_response]
    response = client.recognize(config, audio)
    # [END migration_sync_request]
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        encoded = (result.alternatives[0].transcript).encode('utf-8')
        sheetdasu(encoded)
    # [END migration_sync_response]
# [END def_transcribe_file]



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    args = parser.parse_args()
    # if args.path.startswith('gs://'):
        # transcribe_gcs(args.path)
    # else:
    transcribe_file(args.path)
