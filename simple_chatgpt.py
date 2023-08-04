import openai

# OpenAI API key
# Read the API key from a file
openai.api_key = open("openai_key.txt", "r").read().strip()
# The model to use
mod = "gpt-3.5-turbo"


def loop():
    print(">> Starting chat...\n")

    try:

        while True:
            prompt = input(">> Input: ")

            response = openai.ChatCompletion.create(
                model=mod,
                messages=[
                    {"role": "system", "content": open("model_description.txt", "r").read().strip()},
                    {"role": "user", "content": f"{prompt}"},
                ],
                temperature=0.5,
                presence_penalty=1,
                frequency_penalty=1
            )
            print("\n<< ", end=" ")
            print(response["choices"][0]["message"]["content"].strip() + "\n")

    except KeyboardInterrupt:
        print("\n>> Exiting chat...\n")
