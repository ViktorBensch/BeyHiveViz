import sys, os
import bz2
import json
import gzip
import shutil

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
    #output.write(minute + "/" + hour + "/" + day + "\n")
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
    
    old_day = "00"
    output_dir = "D:\Misra\output"
    directory = ""
    
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
            
            output_name =  hour + "_" + minute + ".json"
            output_file_path = os.path.join(directory, output_name).replace("\\","/")
            output = open(output_file_path, 'w') 
            
            input =  path + "/" + name
            
            analyse_file(input.replace("\\","/"),minute,hour,day,output)
            
            output.close()
            ###***### if we end the script here the size of 5 files = 14 KB, time = 17 sec
            #with open(output_file_path, 'rb') as f_in, gzip.open(output_file_path + '.gz', 'wb') as f_out:
            #    shutil.copyfileobj(f_in, f_out)
            ###***### if we end the script here the size of 5 files = 23 KB, time = 28 sec
            #os.remove(output_file_path)
            ###***### if we end the script here the size of 5 files = 3 KB, time = 28 sec
            
    
    output.close()



if __name__ == '__main__':
    main()