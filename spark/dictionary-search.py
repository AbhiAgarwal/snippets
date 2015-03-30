# Silly

import sys
from operator import add
from pyspark import SparkContext

def CreateKeyValueMap(lines):
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print "%s: %i" % (word, count)

def SearchWord(words, extension):
    print words.filter(lambda w: w.startswith(extension)).take(5)

if __name__ == "__main__":
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile("/usr/share/dict/words", 1)
    SearchWord(lines, "a")
    sc.stop()
