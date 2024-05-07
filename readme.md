
---

## README.md

```markdown
This repository contains Solutions to the two Problem Statements given in the Assessment by Yarnit.

```markdown
# Webpage Question Answering API using Flask-Problem Statement 1

A simple implementation of a question-answering API using Flask. The API takes a webpage URL and a question as input and responds with the answer based on the content of the webpage.

## Prerequisites

Before running the API, ensure you have the following installed:

- Python 3.6+
- Flask (`pip install flask`)
- Transformers (`pip install transformers`)
- BeautifulSoup (`pip install beautifulsoup4`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/webpage-qa-flask.git
   cd webpage-qa-flask
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. Start the Flask server:
   ```bash
   python wqa_Api.py
   ```

2. The server will start on `http://127.0.0.1:5000/`.

## Usage

Send a POST request to `http://127.0.0.1:5000/qa` with a JSON payload containing the `url` and `question`. You will receive a JSON response with the answer.

Example JSON payload:
```json
{
    "url": "https://en.wikipedia.org/wiki/Generative_artificial_intelligence",
    "question": "What are the concerns around Generative AI?"
}
```

## Frontend

The application also provides a simple HTML form to interact with the API. Navigate to `http://127.0.0.1:5000/` in your web browser to access the form.

## Customization

You can customize the NLP model used for question answering by changing the model name in `wqa_Api.py`.

## Deployment

For production deployment, consider using a production WSGI server like Gunicorn.




# Marketing Content Generation API-Problem Statement 2

This project provides an API for generating marketing content using the Mistral 7B model from Hugging Face. The API accepts a topic and format as input and responds with generated text in the desired format.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Transformers library
- Requests library (for testing the API)

## Installation

First, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/marketing-content-api.git
cd marketing-content-api
```

Then, install the required Python libraries:

```bash
pip install fastapi uvicorn transformers requests
```
## Huggingface key
Make sure to put huggingface access token in key.py
## Running the API

Start the FastAPI server by running:

```bash
uvicorn content_generation:app --reload
```

The API will be available at `http://localhost:8000`.

## Using the API

To generate marketing content, send a POST request to `/generate_marketing_content` with a JSON body containing the `format`, `topic`, `emotion`, and `length` parameters.

Example request body:

```json
{
    "format": "linkedin post",
    "topic": "Generative AI",
    "emotion": "excited",
    "length": 150
}
```

## content_Generation.py

The `content_Generation.py` script can be used to interact with the API using the `requests` library. It sends a POST request to the API and prints the response.
