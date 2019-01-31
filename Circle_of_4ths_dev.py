Circle_of_4ths_dev.py
# Python playfile to drive home circle of 4ths
# -- make a practice game for Circle of 4ths to 
#    get the 2-5-1 sequence automatic

import re

C4 = ('C','F','Bb','Eb','Ab','Db','Gb','B','E','A','D','G')

C4s = ('B#','E#','A#','D#','G#','C#','F#','B','E','A','D','G')

# create indexing function that returns index for any key
# take input of any key and degree and return the corresponding 
# major 2-5-1
#
# e.g., > Eb7 yields [Bb-7,Eb7,Ab]
# 
# Build with this functionality:
# Input a key & degree.  Program parses input, matches degree, 
#    and returns the corresponding 2-5-1

degree = ('-7','7','','-7b5','7b9b13','-7')

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
 # Determine degree of input and use if statement to adjust
 #    indices to print the 2-5-1 sequence for Cycle of 4ths.
 #  E.g., if Eb7 is input then i=3 and the relative 2-5-1 
 #     would be Bb-7, Eb7, Ab

def Major251(inKey) :
 	if inKey[-2:] == "-7" :
 		idx = C4.index(inKey[:-2])  
 		if idx > 9 : idx = idx - 12
 		seq =(inKey,C4[idx+1]+degree[1],C4[idx+2]+degree[2])
 	elif inKey[-1] == "7" :
 		idx = C4.index(inKey[:-1])
 		if idx > 10 : idx = idx - 12
 		seq = (C4[idx-1]+degree[0],inKey,C4[idx+1]+degree[2])
 	else :
 		idx = C4.index(inKey)
 		seq = (C4[idx-2]+degree[0],C4[idx-1]+degree[1],inKey)
 	return seq

 # Works but ...
 # 0. Had issue with end of sequence needing to cycle.  Fixed by putting
 #    in the switched on idx but should be more elegant way.
 # 1. Can't handle C# or G# - solved with flatter fn 
 # 2. Only recognized -7, 7, and M.  Other degree or chord causes barf.
 
 isophonic = {'A#': 'Bb', 'B#': 'C', 'C#': 'Db', 'D#': 'Eb', 'E#': 'F', 
    'F#': 'Gb', 'G#': 'Ab'}

 def flatter(inKey) :
 	if re.search(r'#',inKey) :
 		inKey = isophonic[inKey]
 	return inKey

# Error in the indexing on degree 
#  Problem is for 7 and -7 the +i increments in the 
#    seq = statement puts the index out of range for 
#    the last two keys in the sequence.
#
__________________________________________________________

Workspace


