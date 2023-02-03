import requests
import apiKey

# Use this key in your application by passing it with the key=API_KEY parameter.
url = "https://www.googleapis.com/youtube/v3/search"
headers = {
    "Authorization" : "Bearer" + apiKey.api_key
}
response = requests.get(url, headers=headers)
print(response.text)
