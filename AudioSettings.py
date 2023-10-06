import requests

# Define the URL to request the settings of a specific voice from ElevenLabs API.
# Replace {Your_Voice_ID} with the actual ID of the voice whose settings you want to retrieve.
url = "https://api.elevenlabs.io/v1/voices/{Your_Voice_ID}/settings"

# Replace {Your_ElevenLabs_Key} with your actual ElevenLabs API key to authenticate the request.
headers = {
    "Accept": "application/json",
    "xi-api-key": "{Your_ElevenLabs_Key}"
}

# Make a GET request to the specified URL with the given headers.
# This request retrieves the settings of the specified voice from the ElevenLabs API.
response = requests.get(url, headers=headers)

# Print the response from the server.
# If the request is successful, this will be a JSON string containing the settings of the specified voice.
# You can parse this string to manipulate or display the voice settings in your application.
print(response.text)
