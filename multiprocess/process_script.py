import sys, os
from multiprocessing import Process
import bz2
import json
import gzip
import shutil

exitFlag = 0

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )
    
def print_f(filename):
    print filename
    

###***### if we eliminate the unrelevant sections the size of 5 files = <1.5 KB, time = 20 sec
def only_relevant(tweet):
    relevant = {}
    relevant['screen_name'] = tweet['user']['screen_name']
    relevant['text'] = tweet['text']
    relevant['timestamp'] = tweet['timestamp_ms']
    relevant['following'] = tweet['user']['friends_count']
    relevant['followers'] = tweet['user']['followers_count']
    relevant['description'] = tweet['user']['description']
    relevant['user_location'] = tweet['user']['location']
    relevant['in_reply_to_screen_name'] = tweet['in_reply_to_screen_name']
    relevant['user_mentions'] = tweet['entities']['user_mentions']
    relevant['hashtags'] = tweet['entities']['hashtags']
    
    return relevant

def analyse_file(filename,minute,hour,day,output):
    #output.write(minute + "/" + hour + "/" + day + "\n")
    print minute + "/" + hour + "/" + day
    
    bz_file = bz2.BZ2File(filename)
    line_list = bz_file.readlines()
    j = [json_loads_byteified(elm) for elm in line_list]
    for tweet in j:
        if tweet.get('text') != None:
            if tweet['lang'] == "en":
                if "beyonc" in tweet['text'].lower():
                    json.dump(only_relevant(tweet),output)
                    output.write("\n")
                elif " bey " in tweet['text'].lower():
                    json.dump(only_relevant(tweet),output)
                    output.write("\n")
                elif "sasha fierce" in tweet['text'].lower():
                    json.dump(only_relevant(tweet),output)
                    output.write("\n")
                elif "knowles carter" in tweet['text'].lower():
                    json.dump(only_relevant(tweet),output)
                    output.write("\n")
                elif "mrs. carter" in tweet['text'].lower():
                    json.dump(only_relevant(tweet),output)
                    output.write("\n")
         
def process_reponse(head, suffix, output_dir, output):

    old_day = "00"
    old_hour = "aa"
    directory = ""
    
    root = head+suffix
    for path, subdirs, files in os.walk(root):
        for name in files:
            minute = name[:2]
            hour = path[-2:]
            day = path[-5:-3]
            
            if old_day != day:
                directory = output_dir + "/" + day
                if not os.path.exists(directory):
                    os.makedirs(directory)
                    old_day = day
                    print "New day folder! - " + day
            
            ##**!!!**##Creating files for each minute
            #output_name =  hour + "_" + minute + ".json"
            #output_file_path = os.path.join(directory, output_name).replace("\\","/")
            #output = open(output_file_path, 'w') 
            
            ##**!!!**##Creating files for each hour
            if old_hour != hour:
                output.close()
                print "New hour file* - " + hour
                output_name =  hour + ".json"
                output_file_path = os.path.join(directory, output_name).replace("\\","/")
                output = open(output_file_path, 'w') 
                old_hour = hour
            
            input =  path + "/" + name
            
            analyse_file(input.replace("\\","/"),minute,hour,day,output)
            
            ###***### if we end the script here the size of 5 files = 14 KB, time = 17 sec
            #with open(output_file_path, 'rb') as f_in, gzip.open(output_file_path + '.gz', 'wb') as f_out:
            #    shutil.copyfileobj(f_in, f_out)
            ###***### if we end the script here the size of 5 files = 23 KB, time = 28 sec
            #os.remove(output_file_path)
            ###***### if we end the script here the size of 5 files = 3 KB, time = 28 sec

    
def main():
    #D:\Misra\archiveteam-twitter-stream-2017-01\archiveteam-twitter-stream-2017-01\01\01\00\*.json.bz2
    #input_folder = "D:/Misra/archiveteam-twitter-stream-2017-01/archiveteam-twitter-stream-2017-01/01/01/00/"
    
    head = "D:/Misra/archiveteam-twitter-stream-2017-01/"

    output_dir = "D:\Misra\output"
    
    output = open("successfull_start.txt", 'w')
    output.write("Your program was started successfully, good luck! - Nonsensical Giraffes")
    
    try:
        process1 = Process(target = process_reponse, args = (head, "part1", output_dir, output))
        process2 = Process(target = process_reponse, args = (head, "part2", output_dir, output))
        #process3 = Process(target = process_reponse, args = (head, "part3", output_dir, output))
        
        process1.start()
        process2.start()
        #process3.start()
        
        process1.join()
        process2.join()
        #process3.join()
    except:
        print "Error: unable to start thread"

        
    output.close()



if __name__ == '__main__':
    main()