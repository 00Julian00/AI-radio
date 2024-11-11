# AI Radio Station (Proof of Concept)
## Version 1.0.1

This project is an AI generated radio station. It consists of 2 hosts having an AI generated conversation who are interruped by AI generated songs from time to time. This project is a proof of concept.

### How to use
1. Install [this](https://github.com/gcui-art/suno-api?tab=readme-ov-file) local server for interacting with [Suno](https://Suno.com). Follow the instructions listed on the github page how to install and start it.
2. Get a [Groq](https://groq.com/) and [ElevenLabs](https://elevenlabs.io/) API key and add it to the `settings.config` file.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Select the correct output device in the `settings.config` file.
5. Make sure the suno-api server is running.
6. Run `StartRadio.py` to start the radio. It usually takes around 15-20 seconds before the radio starts playing. As long as there is no error in the console, just be patient.
7. Liked a song you heard? They are all stored in the `Songs` folder as well as on your Suno account.
8. To add or remove genres, you can edit the list in the `settings.config` file.
9. To change the starting topic, you can edit the `starting_topic` in the `settings.config` file. It is set to "History" by default.

### What's new in version 1.0.1
- Improved prompting for a more natural conversation.
- Fixed a bug where the hosts would act like the segment is about to end.
- Fixed a bug where the hosts would act like the song is about to play after it has already played.
- Improved stability.
- Added a "starting topic" setting.
- Tweaked the values of the TTS to reduce failed generations.

### How it works
The project uses llama3.2-90b to generate the conversation between the hosts. The conversation will then be converted to speech via ElevenLabs. While the hosts are talking, the project uses Suno to generate a song in the background that will then be played. While the song is playing, the next part of the conversation is generated. This loop will continue until the program is terminated.

### Limitations
- Eventhough the system uses a lot of randomness, the structure is very stiff. Conversation, Song, Conversation, Song, etc.
- The conversation is pretty robotic. It is very obvious that it has been AI generated.
- The text to speech produces robotic and emotionless speech.
- The song generation is not always perfect. At times, a song is generated that is only a few seconds long. When that happens, there is a long silence, as the system is not yet finished generating the next part of the conversation.
- The Suno API is not official, which can sometimes cause problems.

### Costs
The project itself is fully open source and therefore free. The services it uses (Groq, Elevenlabs and Suno) offer free tiers with limited usage rates. This means you can run this project completly for free, but you will probably hit the limits of these services very quickly.

### Tips
- Sometimes, there will just be silence with no indication why in the console. If that's the case, visit [the Groq logs](https://console.groq.com/settings/logs). If you see a code 429 on one of the recent generations, this means you have hit the rate limit. Just wait for a few minutes and restart the radio. Alternativly, you can change the model in `speechManager.py` to reset the rate limits. [Here](https://console.groq.com/settings/limits) is a list of all availabe models. Note that smaller models tend to produce worse results and adhere less to the internal instructions, resulting in a worse overall experience.

### A word from me
This project is a quick thrown together proof of concept. Eventhough the radio station I have described here may seem very boring and annoying to listen to, in my experience it is quite the opposite. During development I have found myself listening to the radio for hours. If you want to modify the codebase, just know that it crashes from time to time and produces weird bugs, mostly due to the Suno API beeing unofficial.

### Example
Version 1.0.1 sample recording:
[![Listen Now](https://img.shields.io/badge/Listen-Now-orange)](https://soundcloud.com/julian-679307453/ai-radio-sample-recording-for-version-101)

Version 1.0 sample recording:
[![Listen Now](https://img.shields.io/badge/Listen-Now-orange)](https://soundcloud.com/julian-679307453/ai-radio-example-recording)
