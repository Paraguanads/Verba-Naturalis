# Verba-Naturalis
Natural language processing with Python and NLTK.

This is a beta product, so you may find bugs and unoptimized code. Feel free to fork & edit as much you want.

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
