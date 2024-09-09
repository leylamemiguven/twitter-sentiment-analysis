import tensorflow as tf
from tensorflow import keras
# from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import h5py


def predict(user_input_tweet):

    #load the models
    model = tf.keras.models.load_model('/app/twitter_sentiment_analysis.h5')

    # load tokenizer for prediction
    tk = Tokenizer(num_words=1000, filters='!"#$%&()*+,./:;<=>?@[]^_`{|}~')

    tk.fit_on_texts(user_input_tweet)
    X = tk.texts_to_sequences(user_input_tweet)
    X = pad_sequences(X, maxlen=30)
    predicted_result = model.predict(X, batch_size=1)
    # print(predicted_result)

    #get predicted result
    status = ['positive','negative']
    if predicted_result.item(0)> predicted_result.item(1):
        status = status[1]
        predicted_probability = predicted_result.item(0)
    else:
        status = status[0]
        predicted_probability = predicted_result.item(1)

    return(status, predicted_probability)
