from pyspark import SparkContext, SparkConf
import json

def unicode_to_string(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ unicode_to_string(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            unicode_to_string(key, ignore_dicts=True): unicode_to_string(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def main() :
    conf = SparkConf().setAppName("infoviz")

    sc = SparkContext(conf=conf)
        
    path = "00.json.bz2"
    my_RDD_strings = sc.textFile(path)
    #text = sc.wholeTextFiles(path).values.flatMap(lambda x: x.split("\n"))
    my_RDD_dictionaries = my_RDD_strings.map(json.loads).map(lambda x:unicode_to_string(x))
    print my_RDD_dictionaries.take(1)


if __name__ == '__main__':
    main()