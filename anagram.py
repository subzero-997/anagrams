import sys
from collections import defaultdict
import urllib2


#2      3      5      7     11     13     17     19     23     29 
#31     37     41     43     47     53     59     61     67     71 
#73     79     83     89     97    101    103    107    109    113 

#Frequency
#etaoinshrdlcumwfgypbvkjxqz

def main():
	#primes are assigned to letters by frequency of occurence in English
	primes = {'e':2, 't':3, 'a':5, 'o':7, 'i':11, 'n':13, 's':17, 'h':19, 'r':23, 'd':29, 'l':31, 'c':37, 'u':41, 'm':43, 'w':47, 'f':53, 'g':59, 'y':61, 'p':67, 'b':71, 'v':73, 'k':79, 'j':83, 'x':89, 'q':97, 'z':101}

	#a multidict containing a set of words withe same key
	factorizedWords = defaultdict(set)

	url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
	data = urllib2.urlopen(url).read()
	data = data.split("\n")

	for line in data:
		curval = 1
		aline = line.rstrip()

		#calculte the word's factor, by multiplying the letters together
		#the first letter's 
		for letter in aline:
			try:
				curprime = primes.get(letter)
				if type(curprime) == int:
					curval = curval * curprime
			except:
				pass

		#add the factor to the dict as the key. The word is added to the set with the same key
		factorizedWords[curval].add(aline)

	#find all the keys with more than one element in the set - anagrams
	for key in factorizedWords:
		if len(factorizedWords[key])>1:
			print key, factorizedWords[key]

if __name__ == "__main__":
	main()