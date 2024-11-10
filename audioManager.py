import sounddevice as sd
import soundfile as sf
import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'settings.config')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    output_device = config['output_device']

def play_audio(file_path, volume=1.0, device_id=output_device):
    data, samplerate = sf.read(file_path)

    data = data * volume

    sd.play(data, samplerate, device=device_id)
    sd.wait()

def play_audio_data(audio_data, sample_rate=44100):  # ElevenLabs uses 44100 Hz
    sd.play(audio_data, sample_rate)
    sd.wait()