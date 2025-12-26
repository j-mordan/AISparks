# Import the official OpenAI library
from openai import OpenAI

# Make sure to replace "YOUR_API_KEY_HERE" with your actual API key
API_KEY = "key"
client = OpenAI(api_key=API_KEY)

# Get a prompt from the user
prompt = input("User: ")

while prompt.lower() != "quit":

    # Make the API call to the GPT model
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    # Print the AI's response
    print("AI:", response.choices[0].message.content)

    # Get a prompt from the user
    prompt = input("User: ")