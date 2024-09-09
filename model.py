import tensorflow as tf
from tensorflow import keras
import boto3
from botocore.exceptions import NoCredentialsError
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os

def predict(user_input_tweet):
    # AWS credentials and S3 bucket details
    ACCESS_KEY = 'your-access-key'
    SECRET_KEY = 'your-secret-key'
    BUCKET_NAME = 'twitter-sentiment-analysis'
    FILE_NAME = 'twitter_sentiment_analysis.h5'

    def download_file_from_s3():
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)

        try:
            # Download file to the root directory
            s3.download_file(BUCKET_NAME, FILE_NAME, FILE_NAME)
            print(f"{FILE_NAME} has been downloaded.")
        except NoCredentialsError:
            print("Credentials not available")

    download_file_from_s3()
    
    # Load the model
    model_path = os.path.join(os.getcwd(), FILE_NAME)
    model = tf.keras.models.load_model(model_path)

    # Initialize the tokenizer (ensure this matches the one used for training)
    tk = Tokenizer(num_words=1000, filters='!"#$%&()*+,./:;<=>?@[]^_`{|}~')

    # Convert user input to sequences and pad them
    tk.fit_on_texts(user_input_tweet)
    X = tk.texts_to_sequences(user_input_tweet)
    X = pad_sequences(X, maxlen=30)
    
    # Predict using the model
    predicted_result = model.predict(X, batch_size=1)

    # Get predicted result
    status = ['positive', 'negative']
    if predicted_result[0, 0] > predicted_result[0, 1]:
        status_result = status[0]
        predicted_probability = predicted_result[0, 0]
    else:
        status_result = status[1]
        predicted_probability = predicted_result[0, 1]

    return status_result, predicted_probability