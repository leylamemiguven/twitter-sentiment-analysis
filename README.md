# digiturk-sentiment-analysis
A flask application that uses Tensorflow Keras Sequential model to classify Turkish text tweets as positive or negative.
You can try out the project at https://digiturk-sentiment-analysis.herokuapp.com/ 

Here is what the app preview looks like: 

![](images/image1.png)

As it can be seen in the picture above, the machine learning model has classifies the word "iğrenç" (which translates to "disgusting")as negative with 63% probablitiy . Here are some other examples:

![Example 1 --> Positive](images/image2.png)
Here the phrase "çok güzel olmus ellerinize sağlık" translates to "This is wonderful good job". As this is a positive sentiment, it is classified as positive. 

![Example 3 --> Negative ](images/image4.png)
Here the phrase "bok gibi olmuş bir daha olmasın" translates to "This is so bad like shit, please don't let it happen again".  As this is a negative sentiment, it is classified as negative. 




