""" Interactive version that asks user to fill in the 
 three keys/chords in the 2-5-1.  
 Original was Circle_of_4ths.py, which asked user to input 
 a key and quality and then returned the Major 2-5-1 """

import re
import sys
import random


# create indexing function that returns index for any key
# take input of any key and quality and return the corresponding 
# major 2-5-1
#
# e.g., > Eb7 yields [Bb-7,Eb7,Ab]
# 
# Build with this functionality:
# Input a key & quality.  Program parses input, matches quality, 
#    and returns the corresponding 2-5-1

# get_key fn to get key input from user and QC input to see that it is
#    a letgit key
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

# Check key fn taken from get_key -- to be used for user input in game
def check_key(ans):
	if ans[0] in ['A','B','C','D','E','F','G'] :
	   if len(ans) == 1 : 
	   		return 1
	   elif ans[1:] in ['b','#','7','-7','b7','b-7','#7','#-7'] :
	   		return 1
	   else : 
	   	print "That's not a key/quality I know"
	   	return None


#major_parser fn (not used) -- removes quality from key
def major_parser(inKey) :
   if inKey[-2:] == "-7" :
     j = 2
   elif inKey[-1] == "7" :
     j = 5
   else :
     j = 1   
   return j 

 # Major251 fn --  Flow:
 # Locate key in C4 with C4.index("Key") and store as i
 # Determine quality of input and use if statement to adjust
 #    indices to return the 2-5-1 sequence for Cycle of 4ths in list seq.
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
 
# flatter does enharmonic switch for #s preserving quality
def flatter(inKey) :
 	if re.search(r'#',inKey) :
 		sloc=inKey.index('#')+1
 		inKey = enharmonic[inKey[0:sloc]] + inKey[sloc:]
 	return inKey

# Function to check answer against seq (output of Major251() fn) and
#    validate correct answer or ask again
def check_answer(pos,seq) :
	ans = raw_input(prompt[pos])
	UC = ans[0].upper()
	if len(ans) == 1 :
		ans = UC 
	else :
		ans = UC + ans[1:]
	altkey = 'ZZZ' #Initializing to out of range value
	if not ans :
		quitter = raw_input("Quit (Y/N)?: ")
		if quitter in ['Y','y'] : 
			return 
	if len(ans)>1 :
		if ans[1] in ['b','#'] :
			altkey = enharmonic[ans[:2]]+quality[pos]
			#print "altkey= ", altkey
	if seq[pos] in [ans,altkey] :
	#if ans == seq[pos] :
		result=1 
	else :
		print "epic fail"
		result=0
	return result


# Main
# set up basic sequence of chromatic scale
C4 = ('C','F','Bb','Eb','Ab','Db','Gb','B','E','A','D','G')
# Enharmonic translation 
C4s = ('C','F','A#','D#','G#','C#','F#','B','E','A','D','G')
# Quality
quality = ('-7','7','')
# Enharmonic dict
enharmonic = {'A#':'Bb', 'B#':'C', 'C#':'Db', 'D#':'Eb', 'E#':'F', 
    'F#':'Gb', 'G#':'Ab','Ab':'G#','Bb':'A#', 'Cb':'B','Db':'C#','Eb':'D#',
    'Fb':'E','Gb':'F#','F':'E#','C':'B#','B':'Cb'}
# prompt is labels for input requests
prompt = ('Enter the 2/-7 key> ','Enter the 5/7 key> ','Enter the 1/Major key> ')

# main loop - do until opt out
more = 'Y'
while more in ['Y','y'] :
#Randomly choose a key and quality as variable inKey
  inKey = random.choice(C4)+random.choice(quality)
  print "What is the Major 2-5-1 for", inKey, " ?"

# Get 2-5-1 sequence for inKey
  if inKey : 
  	seq = Major251(inKey)

# Main look uses call fn that gets & checks answer
#  - if fail call again
#  - if pass, then call fun to get & check answer2, then 3
  i = 0
  while i < 3 :
  	if check_answer(i,seq) :
  		i=i+1
  print "Congratulations!"

# want to introduct logic switch to continue playing or quit
# need to figure out quit option in check_anser fn also.
  more = raw_input("Try again(Y/N)? ")









