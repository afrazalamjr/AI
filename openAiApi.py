import openai

# Set your OpenAI API key
openai.api_key = 'your api key'

def sentiment_analysis(text):
    # Define the prompt for sentiment analysis
    prompt = f"Analyse the sentiment of the following text: '{text}'"

    # Use OpenAI API to perform sentiment analysis
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0,
        max_tokens=50,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract sentiment from the API response
    sentiment = response.choices[0].text.strip().lower()

    # Print the sentiment result
    if "positive" in sentiment:
        print("The text has a positive sentiment.")
    elif "negative" in sentiment:
        print("The text has a negative sentiment.")
    else:
        print("The sentiment of the text is neutral or unclear.")

# Ask the user for input
user_input = input("Enter a text for sentiment analysis: ")
# Call the sentiment_analysis function
sentiment_analysis(user_input)

