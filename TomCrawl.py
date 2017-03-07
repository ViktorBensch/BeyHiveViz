from twython import Twython
import re
import collections
import csv
import datetime 

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
 
	MAX_ATTEMPTS                    =   100
	COUNT_OF_TWEETS_TO_BE_FETCHED   =   1100
	search_query                    =   "Koala"
	
	for i in range(0,MAX_ATTEMPTS):
	    print i
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
	        results = t.search(q=search_query, result_type='recent', count='100')
	    else:
	        # After the first call we should have max_id from result of previous call. Pass it in query.
	        results = t.search(q=search_query,result_type='recent',include_entities='true',max_id=next_max_id)
	
	    # STEP 2: Save the returned tweets
	    for result in results['statuses']:
	        #tweet_text = result['text']
	        tweets.append(result)
	        #tweet_ids.append(result['id_str'])

	        #print count_tweets(tweets)
		#print 'tweet example: ' +tweets[-1]
	
	    # STEP 3: Get the next max_id
	    try:
	        # Parse the data returned to get max_id to be passed in consequent call.
	        next_results_url_params    = results['search_metadata']['next_results']
	        next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
	    except:
	        # No more next pages
	        print 'No more next pages'
	        break
	return tweets, search_query
	
	

def main():
     
	tweets, query = search()
	print 'Search complete'
	
	title = 'TomCSV' +'_'+ query + '_'+ str(datetime.datetime.now()) +'.csv'
	#Output JSON instead
	with open(title, 'w') as csvfile:
		fieldnames = ['text', 'language','created_at']#,'timestamp']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for tweet in tweets:
			tweet_text = tweet['text'].encode('utf-8')
			tweet_lang = tweet['lang']#.encode('utf-8')
			tweet_created = tweet['created_at']
			#tweet_timestamp = tweet['timestamp_ms']
			writer.writerow({'text': tweet_text ,'language':tweet_lang, 'created_at': tweet_created  })#, 'timestamp':tweet_timestamp})
			#Hashtags
			#Retweets num
			#Username/ userID
	#for ID in tweet_ids:
         #print ID

	
	
	
if __name__ == "__main__":
    main()
    #print extract_hashtags(tweets)
