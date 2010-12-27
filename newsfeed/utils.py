from oauth import oauth
from socialauth.models import TwitterUserProfile
from socialauth.utils import twitter

TWITTER_HOME_TIMELINE = 'https://api.twitter.com/1/statuses/home_timeline.json'


def tweets_to_posts(tweets):
    posts = []
    for tweet in tweets:
        posts.append({
            'id': tweet['id'],
            'avatar': tweet['user']['profile_image_url'],
            'content': tweet['text'],
            'datetime': tweet['created_at']})
            
    return posts

def get_token(user):
    try:
        return get_token._token
    except:
        twitter_profile = TwitterUserProfile.objects.get(user=user)
        get_token._token = twitter_profile.get_token()
        return get_token._token

def get_default_tweets(user):
    return twitter.api(TWITTER_HOME_TIMELINE,get_token(user))

def get_older_tweets(user, max_id):
    return twitter.api('%s?max_id=%s' % (TWITTER_HOME_TIMELINE, max_id),
                       get_token(user))
                       
def get_newest_tweets(user, since_id):
    return twitter.api('%s?since_id=%s' % (TWITTER_HOME_TIMELINE, since_id),
                       get_token(user))

#mix fb & tweets
def get_default_posts(user):
    return tweets_to_posts(get_default_tweets(user))

def get_older_posts(user, max_id):
    return tweets_to_posts(get_older_tweets(user, max_id))

def get_newest_posts(user, since_id):
    return tweets_to_posts(get_newest_tweets(user, since_id))



