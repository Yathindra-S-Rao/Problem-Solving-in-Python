#       Filename :   Tweets_list.py
#       Author :    Yathindra S.
#       Program to find the number of tweets.

num_of_testcases = int(input())
tweets = list()

for test in range(num_of_testcases):
    num_of_tweets = int(input())
    for tweet in range(num_of_tweets):
        input_tweet = input()
        input_tweet = input_tweet.split(" ")
        tweets.append(input_tweet[0])


    

