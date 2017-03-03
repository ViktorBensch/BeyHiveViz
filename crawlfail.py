from twython import Twython
import re
import collections

def search():
	
	#connect to Twitter API
	TWITTER_APP_KEY = 'yDR8sFgX68WaI255xxJ5gGPpC' #supply the appropriate value
	TWITTER_APP_KEY_SECRET = 'D1tSnlt5Q63K5IwHOXnkRURhufvEqOBsG1Qo8ut7GYkSGNZ83X' 
	TWITTER_ACCESS_TOKEN = '830037838162956288-0cn7W6p8wxODLa8xx50on7J45Oou3Yq'
	TWITTER_ACCESS_TOKEN_SECRET = 'G1d9bI8btngCdBoNI3PlMrxrkcriZROnIMkFNSqDn3cXq'
	
	t = Twython(app_key=TWITTER_APP_KEY, 
	            app_secret=TWITTER_APP_KEY_SECRET, 
	            oauth_token=TWITTER_ACCESS_TOKEN, 
	            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
	
	#search phrase
	tweets                          =   []
	MAX_ATTEMPTS                    =   10
	COUNT_OF_TWEETS_TO_BE_FETCHED   =   1000
	search_query                    =   "android"
	
	for i in range(0,MAX_ATTEMPTS):
	    if(COUNT_OF_TWEETS_TO_BE_FETCHED < len(tweets)):
	        break # we got 500 tweets... !!
	    #----------------------------------------------------------------#
	    # STEP 1: Query Twitter
	    # STEP 2: Save the returned tweets
	    # STEP 3: Get the next max_id
	    #----------------------------------------------------------------#
	
	    # STEP 1: Query Twitter
	    if(0 == i):
	        # Query twitter for data. 
	        results = t.search(q=search_query,count='100')
	    else:
	        # After the first call we should have max_id from result of previous call. Pass it in query.
	        results = t.search(q=search_query,include_entities='true',max_id=next_max_id)
	
	    # STEP 2: Save the returned tweets
	    for result in results['statuses']:
	        tweet_text = result['text']
	        tweets.append(tweet_text)
	        #print count_tweets(tweets)
	
	
	    # STEP 3: Get the next max_id
	    try:
	        # Parse the data returned to get max_id to be passed in consequent call.
	        next_results_url_params    = results['search_metadata']['next_results']
	        next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
	    except:
	        # No more next pages
	        print 'No more next pages'
	        break
	
	return tweets
	
def extract_hashtags(tweets):
	
	allhashtags = []
	
	#lookup hashtags (and print tweets)
	for tweet in tweets:
	  print tweet['id_str'], " - ", tweet['lang'], " - ", tweet['created_at']
	  print tweet['text']
	  print '\n'
	  
	  hashtags = re.findall(u'#(.*?)[ ,:)(!]', tweet['text'])
	  
	  for m in hashtags:
	  	tag = m.lower()
	  	allhashtags.append(tag)

	
	return allhashtags
	
def count_hashtags(allhashtags):
	
	counter = collections.Counter(allhashtags)
	print counter
	
	for item in counter:
		print item, counter[item]
		
	return 0
	
def count_tweets(tweets):
	
	counter = 0
	for tweet in tweets:
		counter = counter + 1
		
	return counter

def main():

	tweets = search()
	
	
    #allhashtags = extract_hashtags(tweets)
    #count_hashtags(allhashtags)
	
	
	
if __name__ == "__main__":
    main()
    print extract_hashtags(tweets)