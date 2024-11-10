import threading
import random
import os
import json

from musicManager import generate_song, play_song
from speechManager import generate_conversation, generate_speech, play_speech, prepare_for_song, song_has_ended, print_conversation


script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'settings.config')

def get_random_genre():
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
        genres = config['genres']
        return random.choice(genres)


def run():
    next_genre = get_random_genre()
    has_lyrics = random.random() < 0.9

    #First itteration is a bit different from the loop.
    thread_music_generation = threading.Thread(target=generate_song, args=(next_genre, has_lyrics))
    thread_music_generation.start()

    conversation_length = random.randint(3, 6)

    generate_conversation(conversation_length, next_genre)
    generate_speech(conversation_length)
    play_speech()

    while True:
        thread_music_generation.join()
        thread_music_playback = threading.Thread(target=play_song)
        thread_music_playback.start()

        song_has_ended()

        next_genre = get_random_genre()
        conversation_length = random.randint(3, 6)
        generate_conversation(conversation_length, next_genre)
        generate_speech(conversation_length)

        thread_music_playback.join()

        has_lyrics = random.random() < 0.9
        thread_music_generation = threading.Thread(target=generate_song, args=(next_genre, has_lyrics))
        thread_music_generation.start()
        play_speech()