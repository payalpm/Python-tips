import openai

# Set the API key for OpenAI
openai.api_key = "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"

while True:
    # Prompt the user for a question
    question = input("Enter a question: ")

    # Use the OpenAI API to generate a response to the question
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Answering: " + question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Print the response
    print("Response: " + response.choices[0].text)
