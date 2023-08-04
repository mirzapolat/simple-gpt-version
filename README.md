# Usage of OpenAI API for GPT Models

This is only using the OpenAI API with `import openai`. 

To use, add a file called `openai_key.txt` with your personal OpenAI API Key inside. You can customize the personality of the GPT responder by editing the character description in `model_description.txt`.

To get your own API key, visit [this page](https://platform.openai.com/account/api-keys).

## Development
Init python virtual environment
```bash
python3 -m venv venv
```

Activate virtual environment
```bash
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run the program
```bash
python3 simple_chatgpt.py
```