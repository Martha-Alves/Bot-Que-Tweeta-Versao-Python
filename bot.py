import tweepy
import time 

client = tweepy.Client(
    consumer_key='--------',
    consumer_secret='--------',
    access_token='--------',
    access_token_secret='--------'
)

try:

    tweet = client.create_tweet(text="encerrando o terceiro dia... #SaveWarriorNun")
    print(tweet)

    time.sleep(60) 

    client.create_tweet(in_reply_to_tweet_id= --------, text="você pode ver mais sobre o trabalho de quem transcreveu o roteiro aqui: https://tvshowtranscripts.ourboard.org/viewforum.php?f=1595 #SaveWarriorNun")

except:

    print("Alguma coisa deu errado!")    



