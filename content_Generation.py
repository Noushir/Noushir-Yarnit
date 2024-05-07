import requests

# Define the API endpoint
url = 'http://localhost:8000/generate_marketing_content'

# Define the JSON body of the request
data = {
    "format": "linkedin post",
    "topic": "Generative AI",
    "emotion": "excited",
    "length": 150
}

# Send the POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
