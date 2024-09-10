# digiturk-sentiment-analysis
A flask application that uses Tensorflow Keras Sequential model to classify Turkish text tweets as positive or negative.
You can try out the project at https://digiturk-sentiment-analysis.herokuapp.com/ 

Here is what the app preview looks like: 

![image1](https://github.com/user-attachments/assets/96bd1b97-2bd0-4ca4-964e-b0487467fe9d)


As it can be seen in the picture above, the machine learning model has classified the word "iğrenç" (which translates to "disgusting")as negative with 63% probablitiy . Here are some other examples:

![Example 1 --> Positive]![image2](https://github.com/user-attachments/assets/75503198-019a-47b4-8052-d5a3e4091220)

Here the phrase "çok güzel olmuş ellerinize sağlık" translates to "This is wonderful good job". As this is a positive sentiment, it is classified as positive. 

![Example 3 --> Negative ]![image4](https://github.com/user-attachments/assets/216032ea-7580-4eae-a85d-34a3f2156b1c)

Here the phrase "bok gibi olmuş bir daha olmasın" translates to "This is so bad like shit, please don't let it happen again".  As this is a negative sentiment, it is classified as negative. 




