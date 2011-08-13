# lang-detect: a tool to detect language

Detecting the language for a small piece of unicode text

Currently we support detecting de, en, es, fr, it, ja, nl, pl, ru, zh-hans,
zh-hant, and zh-yue.

After some simple testing, we found that the result for long sentence is better.

## Method

We focus on the Basic Multilingual Plane in unicode encoding, and current
language support set could be extended.

For each language, we use a uniformed ngram vector to represent the language
itself. This vector can be seen at the data folder.

When we detect a text, we generate the uniformed ngram vector for this text, and
just comparing the cosine value of the angle between the text vector and the
language vector.

To get the language vector, we use feature articles on Wikipedia as corpus.

## Usage

cd python
python detect.py YOUR_SENTENCE_HERE




