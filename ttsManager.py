from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import queue
import io
import soundfile as sf
from audioManager import play_audio_data
import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'settings.config')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    elevenlabs_api_key = config['elevenlabs_api_key']
    male_host_voice = config['male_host_voice']
    female_host_voice = config['female_host_voice']

client = ElevenLabs(
  api_key=elevenlabs_api_key
)

queue = queue.Queue()

voice_settings = VoiceSettings(
    stability=0.5,
    similarity_boost=1,
    style=1,
    use_speaker_boost=True,
)

def process_audio_stream(audio_stream):
    # Collect all bytes
    audio_data = bytes()
    for chunk in audio_stream:
        if chunk is not None and len(chunk) > 0:
            audio_data += chunk
    
    audio_buffer = io.BytesIO(audio_data)
    
    data, samplerate = sf.read(audio_buffer)
    return data

def generate_conversation(conversation: list[dict]):
    for message in conversation:
        voice = male_host_voice if message["role"] == "assistant" else female_host_voice
        audio = client.generate(
            text=message["content"],
            voice=voice,
            model="eleven_multilingual_v2",
            voice_settings=voice_settings
        )
        processed_audio = process_audio_stream(audio)
        if len(processed_audio) > 0:
            queue.put(processed_audio)

def play_audio_from_queue():
    while not queue.empty():
        audio = queue.get()
        play_audio_data(audio)