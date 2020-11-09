import os
from flask import Flask, render_template, request
from model import predict


app = Flask('Twitter Sentiment Analysis')

@app.route('/')
@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        user_input = request.form["user_tweet"]
        status, predicted_probability = predict(user_input)
        return render_template('predictform.html', prediction_text = '"{}", \n is {} with %{} probability'. format(user_input, status, str(round(predicted_probability*100))))
    return render_template('predictform.html')


if __name__ == '__main__':
    #call the functions here
    app.run()