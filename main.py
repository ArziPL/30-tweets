import tweepy
import time
import sys
import smtplib
from config import *
from email.message import EmailMessage
from string import Template
from pathlib import Path

# App made with Twitter API, take last 30 tweets from Eminem and print them


# Authentication to use Twitter API
auth = tweepy.OAuthHandler(OAuthHandler1,
                           OAuthHandler2)
auth.set_access_token(access_token1,
                      access_token2)

api = tweepy.API(auth)

list_of_tweets = []
tweet_counter = 0


# Taking every tweet, apending it to list
for marshall_tweet in tweepy.Cursor(api.user_timeline, id='Eminem').items():
    tweet_counter += 1
    tweet_id = marshall_tweet.id
    final_tweet = (
        f'TWEET {tweet_counter} / LINK TO TWEET : https://twitter.com/twitter/statuses/{tweet_id} \n  Tweet : {marshall_tweet.text}')
    list_of_tweets.append(final_tweet)
    if tweet_counter == 30:
        break

# Changing list to nice look string
tweets_string = ''
for item in list_of_tweets:
    tweets_string += '\n'
    tweets_string += item
    tweets_string += '\n'


print(tweets_string)


# Normal - py main.py
# For my own knowledge i did those things under just to try new things, you can save tweets to txt or send as a email.
# py main.py [txt] [email]  

# # Taking from user info if it is supposed to be txt or send email
# sending_method = sys.argv[1]


# # Writing new txt file
# if sending_method == 'txt':
#     with open('30EminemTweets.txt', 'wt', encoding='utf-8') as tweet_to_txt:
#         tweet_to_txt.write(tweets_string)
#         print('It worked !')
#         tweet_to_txt.close()


# # Sending email 
# elif sending_method == 'email':
#     email = EmailMessage()
#     email['from'] = 'example@example.pl'
#     email['to'] = 'ogryzek.arkadiusz@gmail.com'
#     email['subject'] = 'Your all new Eminem tweets ! :)'
#     email.set_content(tweets_string)
    
#     
#     with smtplib.SMTP_SSL(host='smtp.wp.pl', port=465) as smtp:
#         smtp.ehlo()
#         smtp.login('example@example.pl', 'password !') # !!!
#         smtp.send_message(email)
#         print('It worked !')

# else :
#     print('Bad arguments, it should be txt or email')
