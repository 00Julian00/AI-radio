import groq
import os
import json

from ttsManager import generate_conversation as generate_conversation_tts, play_audio_from_queue as play_audio_from_queue_tts

script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'settings.config')

with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    api_key = config['groq_api_key']
    male_host_name = config['male_host_name']
    female_host_name = config['female_host_name']
    station_name = config['station_name']
    starting_topic = config['starting_topic']

client = groq.Groq(
    api_key=api_key
)

conversation_male = []
conversation_female = []

behavior_male = f""""
You are a radio host of the radio show {station_name}. You are talking to your co-host {female_host_name} (the user) and the listeners. You are entertaining and your language is very casual and natural.
You talk about diverse and interesting topics. Do NOT announce a song, if not explicitly told to do so. Do NOT pretend to take user calls. Your name is {male_host_name}.
Keep your answers short and concise. Do NOT add roleplaying elements to your answers, i.e. do not describe something by putting asterisks around it or putting it in brackets. Do not describe your actions.
Do NOT announce that the show has ended. If a topic becomes stale, switch the topic to something else. Start with the topic {starting_topic}. You can deviate from this topic during the conversation.

You are in a disucssion with your co-host, meaning you do not always agree with your co-host and you have your own interests and opinions.

Do not use academic language and complex sentences. Keep your language simple and natural. Use contractions.
Do not dwell on a topic for too long. Your main objective is to entertain the listeners.
"""

behavior_female = f""""
You are a radio host of the radio show {station_name}. You are talking to your co-host {male_host_name} (the user) and the listeners. You are entertaining and your language is very casual and natural. 
You talk about diverse and interesting topics. Do NOT announce a song, if not explicitly told to do so. Do NOT pretend to take user calls. Your name is {female_host_name}.
Keep your answers short and concise. Do NOT add roleplaying elements to your answers, i.e. do not describe something by putting asterisks around it or putting it in brackets. Do not describe your actions.
Do NOT announce that the show has ended. If a topic becomes stale, switch the topic to something else. Start with the topic {starting_topic}. You can deviate from this topic during the conversation.

You are in a disucssion with your co-host, meaning you do not always agree with your co-host and you have your own interests and opinions.

Do not use academic language and complex sentences. Keep your language simple and natural. Use contractions.
Do not dwell on a topic for too long. Your main objective is to entertain the listeners.
"""

conversation_male.append({"role": "system", "content": behavior_male})
conversation_female.append({"role": "system", "content": behavior_female})

def generate_conversation(length: int, next_genre: str):
    for _ in range(length):

        if _ == length - 1:
            prepare_for_song(next_genre)

        response = prompt_llm(conversation_male)
        conversation_male.append({"role": "assistant", "content": response})
        conversation_female.append({"role": "user", "content": response})

        response = prompt_llm(conversation_female)
        conversation_male.append({"role": "user", "content": response})
        conversation_female.append({"role": "assistant", "content": response})

def prompt_llm(conversation: list[str]):
    chat_completion = client.chat.completions.create(
        model="llama-3.2-90b-text-preview",
        messages=conversation
    )

    return chat_completion.choices[0].message.content

def generate_speech(length: int):
    result = []
    count = 0
    
    # Iterate through the reversed list
    for item in reversed(conversation_male):
        # Skip system messages
        if item["role"] == "system":
            continue
            
        result.append(item)
        count += 1
        
        if count >= length * 2:
            break

    # Reverse the result to maintain original order
    generate_conversation_tts(list(reversed(result)))


def play_speech():
    play_audio_from_queue_tts()

def prepare_for_song(song_genre: str):
    conversation_male.append({"role": "system", "content": f"You and your co-host will each get to say one more thing before the next song will be played. Song genre: {song_genre}. Your conversation will be continued after the song. Your co-host will announce the song. You will be informed when the song is over by the system."})
    conversation_female.append({"role": "system", "content": f"Interrupt your conversation and announce that a song will be played next. Song genre: {song_genre}. Your conversation will be continued after the song, but you need to interrupt the conversation and announce the song. Do NOT make up a name for the song. Do NOT mention the artist. You will be informed when the song is over by the system."})

def song_has_ended():
    conversation_male.append({"role": "system", "content": "The song is over. Switch the topic."})
    conversation_female.append({"role": "system", "content": "The song is over. Switch the topic."})

    #Force the model to acknowledge the song ending
    conversation_male.append({"role": "assistant", "content": "Welcome back!"})

def print_conversation():
    print(conversation_male)
