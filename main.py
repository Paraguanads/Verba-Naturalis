from flask import Flask, request, render_template
import nltk
from gensim.summarization import summarize

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["input"]

        if request.form["submit"] == "tokenize":
            tokens = nltk.word_tokenize(text)
            return render_template("index.html", tokens=tokens)
        elif request.form["submit"] == "summarize":
            summary = summarize(text, ratio=0.2)
            return render_template("index.html", summary=summary)

    # Manejar solicitudes GET
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
