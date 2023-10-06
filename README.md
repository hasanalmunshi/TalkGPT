# TalkGPT

TalkGPT is a voice interaction application that allows users to communicate with OpenAI's powerful GPT-3.5 Turbo model using voice commands. It provides a unique experience where users speak to the application, and it responds vocally using generated text from GPT and a text-to-speech service from ElevenLabs, allowing users to hear responses in their own voice.

## Features

- Voice-to-text conversion using OpenAI's Whisper ASR API.
- Text generation using OpenAI's GPT-3.5 Turbo.
- Text-to-speech conversion using ElevenLabs API with the option of using your own voice.

## Installation

Ensure you have Python 3.7.1 or newer installed on your system.

1. Clone the repository to your local machine:
    ```shell
    git clone {Your_Repository_Link}
    ```
2. Navigate to the project directory and install the required packages:
    ```shell
    pip install -r requirements.txt
    ```
3. Run the Streamlit application:
    ```shell
    streamlit run app.py
    ```
## Usage

1. After installing the project, you need to add your API keys and choose a voice. Inside the `main.py` file, replace `{Your_ElevenLabs_Key}` and `{Your_OpenAI_Key}` with your ElevenLabs API key and OpenAI API key, respectively. Additionally, replace `{Your_Voice_ID}` with the ID of the voice you want to use.

    - **Obtaining ElevenLabs API Key and Voice ID:**
      - Visit [ElevenLabs](https://www.elevenlabs.io/) and sign up for an account if you don’t have one.
      - Navigate to the API section to find your API key.
      - For the Voice ID, you can either use the ID of one of the available voices or clone your own voice. To clone your own voice, follow the instructions provided on the ElevenLabs platform. Cloning your voice allows the application to respond with a voice that sounds like yours, enhancing the personalization of the experience.

    **Note:** While the project is designed to offer a unique experience with your cloned voice, you're not limited to using a cloned voice. You can use any Voice ID available on the ElevenLabs platform that you'd like to hear in the application. Simply replace the `{Your_Voice_ID}` placeholder with your preferred Voice ID.

3. Start the application following the installation steps.
4. Click the "Start Recording" button to begin voice interaction.
5. Speak into your microphone; the application will transcribe, process, and respond to your commands vocally using your selected voice.

    Ensure your system's microphone and audio output are properly configured and working as expected to fully experience the voice interaction capabilities of TalkGPT.




## Disclaimer

TalkGPT is developed solely by [Hasan](https://github.com/hasanalmunshi) and is not officially affiliated with OpenAI or ElevenLabs. Users are encouraged to use this application responsibly and ethically, adhering to the terms of service and usage policies of all incorporated services and APIs.
