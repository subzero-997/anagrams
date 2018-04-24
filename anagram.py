import sys
from collections import defaultdict
import urllib2



def main():
	#primes are assigned to letters by frequency of occurence in English
	primes = {'e':2, 't':3, 'a':5, 'o':7, 'i':11, 'n':13, 's':17, 'h':19, 'r':23, 'd':29, 'l':31, 'c':37, 'u':41, 'm':43, 'w':47, 'f':53, 'g':59, 'y':61, 'p':67, 'b':71, 'v':73, 'k':79, 'j':83, 'x':89, 'q':97, 'z':101}

	#a multidict containing a set of words withe same product
	wordDict = defaultdict(set)

	url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
	data = urllib2.urlopen(url).read()
	wordlist = data.split("\n")

	for line in wordlist:
		word = line.rstrip()

		#calculte the word's product, by multiplying the prime numbers per letter together
		#the first letter's prime value is multiplied by 1
		product = 1

		for letter in word:
			curprime = primes.get(letter)
			#if there is a non a-z letter in the list we skip it
			if type(curprime) == int:
				product = product * curprime

		#add the product to the dict as the key. 
		#The word is added to the set with the same key
		wordDict[product].add(word)

	#find all the keys with more than one element in the set - anagrams
	#use dictionary comprehension
	anagrams = {key:value for (key,value) in wordDict.items() if len(value)>1 }
	print anagrams

if __name__ == "__main__":
	main()