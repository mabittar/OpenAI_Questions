# OpenAI_API

FastAPI Form to consume OpenAI

## Requirements

- python 3.8+ installed
- terminal to run commands
- IDE if you need to edit any code
- know how to clone this repo

Create virtual environment and install requirements

**On Linux**

```Shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**On Windows**

```Shell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Your OpenAI API Key

To make successful calls to the Open AI API, you will need to register to Open API and create a new API Key by clicking on the dropdown menu on your profile and selecting [View API key](https://beta.openai.com/account/api-keys). It will be need to input your questions and answers to validate.

After everything installed and set it's possible to start using it.

## How It Works

At the terminal, type: `python main.py` and the output should be something like this:

```Shell
INFO:     Will watch for changes in these directories: []
INFO:     Uvicorn running on http://localhost:8001 (Press CTRL+C to quit)
INFO:     Started reloader process [52945] using StatReload
INFO:     Started server process [52976]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

At your browser navigate to: `http://localhost:8001` and input the form values and submit to validation.

Access the link at the foot, to generate an API key, it can be reusable after. Then fill all form to validate your answer.
