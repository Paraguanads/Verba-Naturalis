# Extra logs for debugging
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# Main imports
from flask import Flask, request, render_template
import nltk
import torch
from transformers import BartTokenizer, BartForConditionalGeneration

# Flask init
app = Flask(__name__)

# Load BART tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BartForConditionalGeneration.from_pretrained('bart-large-cnn')
model.to(device)
tokenizer = BartTokenizer.from_pretrained('bart-large-cnn')

# Function to predict sentiment on text
def predict_sentiment(text, model, tokenizer, device):
    input_ids = tokenizer.encode(text, return_tensors='pt').to(device)
    # Add a batch dimension to the input tensor
    input_ids = input_ids.unsqueeze(0)
    logits = model(input_ids)[0]
    # Remove the batch dimension from the logits tensor
    logits = logits.squeeze(0)
    # Convert logits to a Python scalar
    logits = logits.tolist()[0]
    if logits > 0:
        return "positive"
    else:
        return "negative"

# Sentiment analysis
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Summarize a text
def generate_summary(text, model, tokenizer, device, max_length=1024):
    input_ids = tokenizer.encode(text, return_tensors='pt').to(device)
    summary_ids = model.generate(input_ids, max_length=max_length)
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text

# main function, processing the input with the selected option, also print errors for debugging purposes
@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["input"]

        if request.form["submit"] == "tokenize":
            try:
                tokens = nltk.word_tokenize(text)
                tagged_tokens = nltk.pos_tag(tokens)
            except Exception as e:
                print(e)  # Print error if exists
                return render_template("index.html", error=str(e))

            return render_template("index.html", tokens=tokens, tagged_tokens=tagged_tokens)
        elif request.form["submit"] == "summarize":
            try:
                summary = generate_summary(text, model, tokenizer, device)
            except Exception as e:
                print(e)  # Print error if exists
                return render_template("index.html", error=str(e))

            return render_template("index.html", summary=summary)
        elif request.form["submit"] == "sentiment":
            try:
                sentiment = predict_sentiment(model, tokenizer, device, text)
            except Exception as e:
                print(e)  # Print error if exists
                return render_template("index.html", error=str(e))

            return render_template("index.html", sentiment=sentiment)

    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run()

