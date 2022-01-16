import pickle
import re

import nltk
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

MAX_SEQUENCE_LENGTH = 30
nltk.download('stopwords')


def preprocess(text, text_cleaning_re, stop_words, stemmer, stem=False):
    text = re.sub(text_cleaning_re, ' ', str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in stop_words:
            if stem:
                tokens.append(stemmer.stem(token))
            else:
                tokens.append(token)
    return " ".join(tokens)


def preprocess_twit(input_twit: str):
    stop_words = stopwords.words('english')
    stemmer = SnowballStemmer('english')
    text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

    twit = preprocess(input_twit, text_cleaning_re, stop_words, stemmer)

    with open('NLP_module/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    twit = pad_sequences(tokenizer.texts_to_sequences([twit]), maxlen=MAX_SEQUENCE_LENGTH)

    return twit


def decode_sentiment(score):
    return "Positive" if score > 0.5 else "Negative"


def predict_sentiment(twit: str):
    model_path = 'NLP_module/model.h5'
    model_loaded = tf.keras.models.load_model(model_path)

    preprocessed_twit = preprocess_twit(twit)

    output = model_loaded.predict(preprocessed_twit)
    sentiment = decode_sentiment(output)
    return sentiment
