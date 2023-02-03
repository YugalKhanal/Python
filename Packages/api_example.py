import requests

# Use this key in your application by passing it with the key=API_KEY parameter.
api_key = "AIzaSyADfVCAWq8ia6n-o0w8rJOjuMlV-rDmius"
# api_key = "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"
url = "https://www.googleapis.com/youtube/v3/search"
headers = {
    "Authorization" : "Bearer" + api_key
}
response = requests.get(url, headers=headers)
print(response.text)