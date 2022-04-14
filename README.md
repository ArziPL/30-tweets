# <div align="center">30-tweets</div>
### DESCRIPTION

I love Eminem, but I don't use Twitter so i did script that prints all of his tweets. Make call to API, get response, print response. On the bottom of script there are lines commented out, if you want you can save tweets to .txt, or send them as email (some work needed to do that). If you want you can change id at line 26 to get anyone tweets and change tweet_counter at 32 to change number of tweets.

### USED TECHNOLOGIES
<span>
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen"/>  
<img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/>  
</span>  

### HOW TO
Get your API keys at https://developer.twitter.com/en/docs/twitter-api and past them here at lines 14-18 :
````
13 Authentication to use Twitter API
14 auth = tweepy.OAuthHandler(OAuthHandler1,      <-- here
15                            OAuthHandler2)      <-- here
16 auth.set_access_token(access_token1,           <-- here
17                       access_token2)           <-- here
18 
19 api = tweepy.API(auth)
````
Just do that, you should see tweets in console
````
python main.py
````
If you want to save them as txt, comment out 50-78 and run this command 
````
python main.py txt
````
If you want to send as email comment out 50-78 and fill in the data on the lines 65-66/71/73 then run
````
python main.py email
````
***

<div align="center">Hope you had a good time here. If you liked the project, leave a ⭐ and visit <a href="https://github.com/ArziPL">my profile</a> to send feedback, check other projects, or make something cool together</p></div> 

