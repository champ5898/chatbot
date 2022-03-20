# Chatbot using Python.

Simple chatbot implementation with Python.

## Installation

### Create a virtual environment

Whatever you prefer (e.g. `conda` or `venv`)

```console
mkdir myproject
$ cd myproject
$ python3 -m venv Chatbot
```

### Activate it

Mac / Linux:

```console
. Chatbot/bin/activate
```

Windows:

```console
Chatbot\Scripts\activate
```

### Install dependencies

```console
pip install -r requirements.txt
```

if `nltk` not installed:

```console
pip install nltk
```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:

```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage

Run

```console
python chat.py
```

## Customize

Have a look at [intents.json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chat bot. You have to re-run the training whenever this file is modified.

```console
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    ...
  ]
}
```
