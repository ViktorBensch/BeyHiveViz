import sys, os
import bz2
import json

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

def analyse_file(filename,minute,hour,day,output):
    output.write(minute + "/" + hour + "/" + day)
    print minute + "/" + hour + "/" + day
    
    bz_file = bz2.BZ2File(filename)
    line_list = bz_file.readlines()
    j = [json_loads_byteified(elm) for elm in line_list]
    for tweet in j:
        if tweet.get('text') != None:
            if tweet['lang'] == "en":
                if "beyonc" in tweet['text'].lower():
                    json.dump(tweet,output)
                    output.write("\n")
                elif " bey " in tweet['text'].lower():
                    json.dump(tweet,output)
                    output.write("\n")
                elif "sasha fierce" in tweet['text'].lower():
                    json.dump(tweet,output)
                    output.write("\n")
                elif "knowles carter" in tweet['text'].lower():
                    json.dump(tweet,output)
                    output.write("\n")
                elif "mrs. carter" in tweet['text'].lower():
                    json.dump(tweet,output)
                    output.write("\n")
         

    
def main():
    #D:\Misra\archiveteam-twitter-stream-2017-01\archiveteam-twitter-stream-2017-01\01\01\00\*.json.bz2
    input_folder = "D:/Misra/archiveteam-twitter-stream-2017-01/archiveteam-twitter-stream-2017-01/01/01/00/"
    
    root = "D:/Misra/archiveteam-twitter-stream-2017-01/archiveteam-twitter-stream-2017-01/01/"
    #args = sys.argv[1:]
    
    output = open("output.json", 'w') 
    
    for path, subdirs, files in os.walk(root):
        for name in files:
            minute = name[:2]
            hour = path[-2:]
            day = path[-5:-3]
            
            input =  path + "/" + name
            
            analyse_file(input.replace("\\","/"),minute,hour,day,output)
            
    
    output.close()



if __name__ == '__main__':
    main()