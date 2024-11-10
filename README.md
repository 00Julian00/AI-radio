# AI Radio Station (Proof of Concept)

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

### How it works
The project uses llama3.2-90b to generate the conversation between the hosts. The conversation will then be converted to speech via ElevenLabs. While the hosts are talking, the project uses Suno to generate a song in the background that will then be played. While the song is playing, the next part of the conversation is generated. This loop will continue until the program is terminated.

### Limitations
- Eventhough the system uses a lot of randomness, the structure is very stiff. Conversation, Song, Conversation, Song, etc.
- The conversation is pretty robotic. It is very obvious that it has been AI generated.
- The text to speech produces robotic and emotionless speech.
- The song generation is not always perfect. At times, a song is generated that is only a few seconds long. When that happens, there is a long silence, as the system is not yet finished generating the next part of the conversation.
- The Suno API is not official, which can sometimes cause problems.

### Costs
The project itself is fully open source and therefore free. The services it uses (Groq, Elevenlabs and Suno) offer free tiers with limited usage rates. This means you can run this project completly for free, but you will probably hit the limits of these services after a few hours of running the radio.

### A word from me
This project is a quick thrown together proof of concept. Eventhough the radio station I have described here may seem very boring and annoying to listen to, in my experience it is quite the opposite. During development I have found myself listening to the radio for hours. If you want to modify the codebase, just know that it crashes from time to time and produces weird bugs, mostly due to the Suno API beeing unofficial.

### Example
https://github.com/00Julian00/AI-radio/AIRadioExample.mp3
A few notes regarding the example:
- The male host acts like the song is about to play after it has already played. This is a glitch which I have not found a solution to, because it has nothing to do with the code logic, but is rather a hallucination of the model.
- The hosts act like the segment is about to end. This is a bug which should be fixable with better prompting.
