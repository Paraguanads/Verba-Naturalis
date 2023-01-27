# Verba Naturalis (Beta)
Natural language processing with Python and NLTK.

You may find bugs and unoptimized code. Help me to get this thing better ☺

## What is this?
I have noticed that many on the internet find it difficult to finish reading an article of no more than 1000 words, which is alarming for us as a society and which in turn makes us think of plausible ideas to help people in this task of analysis.

This application processes text using Transformers, Torch and NLTK in Python (under a simple Flask web environment) and returns two types of output to the user.

## Summary 
Take the most relevant content from a long text and show it to the user in a summarized way. It is ideal for creating microblog entries based on medium-long texts, as well as for a more "laser eyes" understanding.

## Sentiment
Extract the sentiment contained in the text taking into account three variables:

### Negative
A text with tendencies to use negative language. It can contain sad or alarming sentences.

### Positive
A text with positive tendencies, which surely uses digestible language for all ages and which in turn can have hopeful, optimistic content, etc.

### Neutral
it is the most common of the variables that I have come across in Internet texts and it is basically the "commercial" way of writing.

## What do I need to get this thing running?
Will be way easier for you if you're using an integrated development environment (IDE) for Python, download the code and install all the libraries from there, but
here all those you need to install to run this model.

Let's assume you have Python installed (3.8), then:

1. Flask [Official site](https://palletsprojects.com/p/flask/) `pip install -U Flask`
2. NLTK [Official site](https://www.nltk.org/) `pip install nltk`
3. Torch [Official site](https://pytorch.org/) `pip install torch`
4. Transformers with BART [Official site](https://huggingface.co/docs/transformers/model_doc/bart) `pip install transformers==2.1.0`

Did you finished downloadind libraries? Now you will need to create a profile here on HuggingFace (if you don't have it) and navigate to [this link](https://huggingface.co/settings/tokens)

Create a new token for your application and copy it. We will use it to authenticate with `huggingface-cli login` in our app.
After you ran that command above, the console will ask you for the token. Paste it, press enter and wait until the models are available for you to use.
