import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from flask import Flask, request, jsonify, render_template_string

# Web scraping and text extraction
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    webpage_text = soup.get_text()
    return webpage_text

# Load pre-trained NLP model
nlp_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Answer extraction function
def get_answer(webpage_text, question):
    answer = nlp_model(question=question, context=webpage_text)["answer"]
    return answer

# Flask app setup
app = Flask(__name__)

# Route for the question-answering API
@app.route("/qa", methods=["POST"])
def question_answering():
    data = request.get_json()
    url = data.get("url")
    question = data.get("question")

    if not url or not question:
        return jsonify({"error": "Please provide both 'url' and 'question'."}), 400

    try:
        webpage_text = extract_text_from_url(url)
        answer = get_answer(webpage_text, question)
        if answer:
            return jsonify({"answer": answer})
        else:
            return jsonify({"answer": "I don't know the answer"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for serving the HTML form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        question = request.form["question"]
        webpage_text = extract_text_from_url(url)
        answer = get_answer(webpage_text, question)
        return render_template_string(HTML_FORM, answer=answer)
    return render_template_string(HTML_FORM, answer="")

# HTML form template
HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Question Answering System</title>
</head>
<body>
    <h1>Ask a Question</h1>
    <form method="post">
        <label for="url">URL:</label>
        <input type="text" id="url" name="url" required>
        <label for="question">Question:</label>
        <input type="text" id="question" name="question" required>
        <button type="submit">Submit</button>
    </form>
    {% if answer %}
    <h2>Answer:</h2>
    <p>{{ answer }}</p>
    {% endif %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
