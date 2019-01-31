# Major 251 program:
# Input a Key and Quality and it returns the relative Major 2-5-1
# from the  circle of 4ths

import re
import sys


# create indexing function that returns index for any key
# take input of any key and quality and return the corresponding 
# major 2-5-1
#
# e.g., > Eb7 yields [Bb-7,Eb7,Ab]
# 
# Build with this functionality:
# Input a key & quality.  Program parses input, matches quality, 
#    and returns the corresponding 2-5-1

def major_parser(inKey) :
   if inKey[-2:] == "-7" :
     j = 2
   elif inKey[-1] == "7" :
     j = 5
   else :
     j = 1   
   return j 

 # Flow:
 # Locate key in C4 with C4.index("Key") and store as i
 # Determine quality of input and use if statement to adjust
 #    indices to print the 2-5-1 sequence for Cycle of 4ths.
 #  E.g., if Eb7 is input then i=3 and the relative 2-5-1 
 #     would be Bb-7, Eb7, Ab

def Major251(inKey) :
 	if inKey[-2:] == "-7" :
 		idx = C4.index(inKey[:-2])  
 		if idx > 9 : idx = idx - 12 # To prevent index out of range error
 		seq =(inKey,C4[idx+1]+quality[1],C4[idx+2]+quality[2])
 	elif inKey[-1] == "7" :
 		idx = C4.index(inKey[:-1])
 		if idx > 10 : idx = idx - 12 # To prevent index out of range error
 		seq = (C4[idx-1]+quality[0],inKey,C4[idx+1]+quality[2])
 	else :
 		idx = C4.index(inKey)
 		seq = (C4[idx-2]+quality[0],C4[idx-1]+quality[1],inKey)
 	return seq

 # Works but ...
 # 1. Can't handle C# or G# - solved with flatter fn 
 # 2. Only recognized -7, 7, and M.  Other quality or chord causes barf.
 
def get_key():
	"""Get Key and Quality as input"""
	print "Enter Key & Quality"
	print "Example: Bb-7"
	inKey = raw_input("> ")
	if inKey[0] in ['A','B','C','D','E','F','G'] :
	   if len(inKey) == 1 : 
	   		return inKey
	   elif inKey[1:] in ['b','#','7','-7','b7','b-7','#7','#-7'] :
	   		return inKey
	   else : 
	   	print "That's not a key/quality I know"
	   	return None

# flatter does enharmonic switch for #s preserving quality
def flatter(inKey) :
 	if re.search(r'#',inKey) :
 		sloc=inKey.index('#')+1
 		inKey = enharmonic[inKey[0:sloc]] + inKey[sloc:]
 	return inKey

# Main
# set up basic sequence of chromatic scale
C4 = ('C','F','Bb','Eb','Ab','Db','Gb','B','E','A','D','G')
# Enharmonic translation 
C4s = ('C','F','A#','D#','G#','C#','F#','B','E','A','D','G')
# Quality
quality = ('-7','7','','-7b5','7b9b13','-7')
# Enharmonic dict
enharmonic = {'A#': 'Bb', 'B#': 'C', 'C#': 'Db', 'D#': 'Eb', 'E#': 'F', 
    'F#': 'Gb', 'G#': 'Ab'}


inKey = get_key()
# print "inKey=", inKey

inKey = flatter(inKey) 

# print "inKey2 =", inKey

if inKey : 
	seq = Major251(inKey)
	print seq
else :
	print "Try again with a legit key & quality"

# Need to save quality and add again -- dropping on the enharmonic function.

# Next: randomize the selection of inKey, print it, and query user for 
#   the Major 2-5-1, evaluating the answer at each position.






