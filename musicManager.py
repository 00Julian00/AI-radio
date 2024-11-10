import time
import requests
import queue
from pathlib import Path

from audioManager import play_audio

base_url = 'http://localhost:3000'

def get_audio_information(audio_ids):
    url = f"{base_url}/api/get?ids={audio_ids}"
    response = requests.get(url)
    return response.json()

queue = queue.Queue()

def generate_audio_by_prompt(payload):
    url = f"{base_url}/api/generate"
    response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
    return response.json()

def download_audio(url, save_path):
    response = requests.get(url)
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.write_bytes(response.content)
    return str(save_path)

def generate_song(genre: str, has_vocals: bool):
    dataRaw = generate_audio_by_prompt({
        "prompt": f"A {genre} song",
        "make_instrumental": not has_vocals,
        "wait_audio": False
    })

    data = get_audio_information(dataRaw[0]['id'])

    while True:
        data = get_audio_information(dataRaw[0]['id'])
        if data[0]["status"] == 'complete':
            break

        time.sleep(1)

    timestamp = int(time.time())
    songs_dir = Path(__file__).parent / 'Songs'
    songs_dir.mkdir(exist_ok=True)
    file_path = songs_dir / f'{genre}_{timestamp}.mp3'

    download_audio(data[0]['audio_url'], file_path)

    queue.put(file_path)

def play_song():
    if not queue.empty():
        file_path = queue.get()
        play_audio(file_path)
    else:
        print("No song to play")