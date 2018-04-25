import sys
from collections import defaultdict
import urllib2

#quit if not python@2
if sys.version_info >= (3, 0):
    sys.stdout.write("Sorry, requires Python 2.x, not Python 3.x\n")
    sys.exit(1)


# primes are assigned to letters by frequency of occurence in English
primes = {'e': 2, 't': 3, 'a': 5, 'o': 7, 'i': 11, 'n': 13, 's': 17, 'h': 19, 'r': 23, 'd': 29, 'l': 31, 'c': 37, 'u': 41,
          'm': 43, 'w': 47, 'f': 53, 'g': 59, 'y': 61, 'p': 67, 'b': 71, 'v': 73, 'k': 79, 'j': 83, 'x': 89, 'q': 97, 'z': 101}


def getprime(value): return primes.get(value)

def main():
    # a multidict containing a set of words withe same product
    wordDict = defaultdict(set)

    #get the data
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    wordlist = urllib2.urlopen(url).read().split("\r\n")

    for word in wordlist:

        #use list comprehension to make a list of primes for each letter
        #in the word
        primes = [getprime(letter) for letter in word]

        #use the reduce function to multiply together
        #the list of primes
        product = reduce(lambda x,y: x*y, primes)

        #create a multidict of anagrams, the key is the product
        #and the value is a growing set of words with this product
        wordDict[product].add(word)

    #make a new dictionary, which is a subset of the entire dict,
    #filtered to only contain words which are anagrams
    anagrams = {key: value for (
        key, value) in wordDict.items() if len(value) > 1}

    #Output the anagrams
    print(anagrams)


if __name__ == "__main__":
    main()
