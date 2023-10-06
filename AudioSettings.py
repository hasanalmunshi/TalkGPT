import requests

url = "https://api.elevenlabs.io/v1/voices/{Your_Voice_ID}/settings"

headers = {
    "Accept": "application/json",
    "xi-api-key": "{Your_ElevenLabs_Key}"
}

response = requests.get(url, headers=headers)

print(response.text)
