# 🎉 Random Joke Generator
import requests  # this library lets us call APIs easily

# Step 1: API endpoint (the URL that gives us a random joke)
url = "https://official-joke-api.appspot.com/random_joke"

# Step 2: Make a request to the API
response = requests.get(url)

# Step 3: Convert the response into JSON format
joke_data = response.json()

# Step 4: Extract the joke setup and punchline
setup = joke_data["setup"]
punchline = joke_data["punchline"]

# Step 5: Display the joke
print("😂 Here's a random joke for you:")
print(setup)
print("👉", punchline)
