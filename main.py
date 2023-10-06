import tempfile
import speech_recognition as sr
import openai
import streamlit as st
import requests
from pydub import AudioSegment
from pydub.playback import play

# Define API keys for Eleven Labs and OpenAI
ELEVENLABS_API_KEY = "{Your_ElevenLabs_Key}"
VOICE_ID = "{Your_Voice_ID}"
openai.api_key = "{Your_OpenAI_Key}"

# Text-to-Speech Function
def text_to_speech_eleven_labs(text, voice_id, api_key):
    """
    Convert text to speech using Eleven Labs API.

    Parameters:
    text (str): Text to convert to speech.
    voice_id (str): ID of the Eleven Labs voice to use.
    api_key (str): Eleven Labs API key.

    Returns:
    str: Filepath of the generated audio file, or None if request fails.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "accept": "audio/mpeg",
        "content-type": "application/json",
        "xi-api-key": api_key,
    }
    data = {"text": text}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        return "output.mp3"
    else:
        print(f"Error in generating TTS: {response.status_code}, {response.text}")
        return None

def record_audio():
    """
    Record audio from the user's microphone.

    Returns:
    audio: Recorded audio data.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)  # Listen to the user's input
    return audio

def transcribe_audio(audio):
    """
    Transcribe recorded audio to text using OpenAI's Whisper API.

    Parameters:
    audio: Recorded audio data.

    Returns:
    str: Transcribed text from the audio.
    """
    with tempfile.NamedTemporaryFile(mode="wb", delete=False, suffix=".wav") as f:
        f.write(audio.get_wav_data())  # Save audio data as a temporary file
        audio_file_path = f.name  # Get the name of the temporary file
    with open(audio_file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)  # Transcribe the audio
    return transcript["text"]

def send_message_to_gpt(user_message, messages_history):
    """
    Send user's message to GPT-3.5 Turbo and return GPT's response.

    Parameters:
    user_message (str): User's message to send to GPT.
    messages_history (list): Conversation history.

    Returns:
    str: GPT's response.
    """
    # Append user's message to the conversation history
    messages_history.append({"role": "user", "content": user_message})
    data = {
        "model": "gpt-3.5-turbo",  # Specify the model to use
        "messages": messages_history,  # Provide the conversation history
    }
    response = openai.ChatCompletion.create(**data)  # Get response from GPT
    chatgpt_response = response["choices"][0]["message"]["content"]  # Extract message content from response
    messages_history.append({"role": "assistant", "content": chatgpt_response})  # Append GPT's response to conversation history
    return chatgpt_response

# Streamlit App Interface
st.title("🗣️ TalkGPT")
st.write("Talk to GPT using your voice and listen to its responses.")

# Initialize session state for conversation history if it doesn't exist
if not hasattr(st.session_state, "messages_history"):
    st.session_state.messages_history = []

# Start recording audio when button is pressed
if st.button("Start Recording"):
    st.write("Recording...")
    audio = record_audio()  # Record user's voice
    speech_to_text = transcribe_audio(audio)  # Convert recorded audio to text
    st.write(f"You said: {speech_to_text}")  # Display transcribed text

    # Send transcribed text to GPT and get response
    chatgpt_response = send_message_to_gpt(speech_to_text, st.session_state.messages_history)
    st.write(f"GPT said: {chatgpt_response}")  # Display GPT's response

    # Convert GPT's response to speech
    output_file = text_to_speech_eleven_labs(chatgpt_response, VOICE_ID, ELEVENLABS_API_KEY)
    if output_file:
        # Play the generated audio file
        output_audio = AudioSegment.from_file(output_file, format="mp3")
        play(output_audio)
    else:
        st.write("TTS generation failed. Please try again.")  # Handle TTS generation failure

# Insert a line separator for visual clarity
st.markdown("---")

# Display entire conversation history
for message in st.session_state.messages_history:
    # Display user's and GPT's messages differently
    st.write(f'🗨️ You: {message["content"]}' if message["role"] == "user" else f'🤖 GPT: {message["content"]}')
