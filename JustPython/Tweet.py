#       Filename :   Tweet.py
#       Author :    Yathindra S.
#       Program to find the number of tweets.

num_of_testcases = int(input())
tweets = dict()

for test in range(num_of_testcases):
    num_of_tweets = int(input())
    for tweet in range(num_of_tweets):
        input_tweet = input()
        input_tweet = input_tweet.split(" ")
        if input_tweet[0] in tweets:
            tweets[input_tweet[0]] += 1
        else:
            tweets[input_tweet[0]] = 1

tweet_values_list = list(tweets.values())
for value in tweet_values_list:
    if tweet_values_list.count(value) > 1: 
        tweets = sorted (tweets.items(), key = lambda t : t[0])
        for key in tweets:
            print ("{} {}".format(key[0], key[1]))
        break
    else:
        for key, value in tweets.items():
            if value == max(tweet_values_list):
                print("{} {}".format(key, value))
                break
        break
