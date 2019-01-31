""" Interactive version that asks user to fill in the 
 three keys/chords in the 2-5-1.  
 Original was Circle_of_4ths.py, which asked user to input 
 a key and quality and then returned the Major 2-5-1.
 Written by Jim Baer to drive home Cicle of 4ths """

import re
import sys
import random

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

 # Limited chord qualites to Major251 - can add minor251 later

# Function to check answer against seq (output of Major251() fn) and
#    validate correct answer or ask again
def check_answer(pos,seq) :
	ans = raw_input(prompt[pos])
	# if blank return check if user wants to continue
	if not ans :
		quitter = raw_input("Quit (Y/N)?: ")
		if quitter in ['Y','y'] :
			sys.exit()
		else : ans = raw_input(prompt[pos])	
	# if user types 'q' as input then terminate	
	if ans == 'q' :
		sys.exit()
	UC = ans[0].upper()
	if len(ans) == 1 :
		ans = UC 
	else :
		ans = UC + ans[1:]
	altkey = 'ZZZ' #Initializing to out of range value
#	if not ans :
#		quitter = raw_input("Quit (Y/N)?: ")
#		if quitter in ['Y','y'] : 
#			return 
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
C4e = ('C','F','Bb','A#','Eb','D#','Ab','G#','Db','C#','Gb','F#','B','E','A','D','G')
# Quality
quality = ('-7','7','')
# Enharmonic dict
enharmonic = {'A#':'Bb', 'B#':'C', 'C#':'Db', 'D#':'Eb', 'E#':'F', 
    'F#':'Gb', 'G#':'Ab','Ab':'G#','Bb':'A#', 'Cb':'B','Db':'C#','Eb':'D#',
    'Fb':'E','Gb':'F#','F':'E#','C':'B#','B':'Cb'}
# prompt is labels for input requests
prompt = ('Enter the 2/-7 key> ','Enter the 5/7 key> ','Enter the 1/Major key> ')

# main loop - do until opt out
print "Type 'q' to quit at any time"
more = 'Y'
while more in ['Y','y'] :
#Randomly choose a key and quality as variable inKey
#  inKey = random.choice(C4)+random.choice(quality)
  keypart = random.choice(C4e)
  qualpart = random.choice(quality)
  showKey = keypart+qualpart
  if keypart in C4 :
  	   inKey = keypart+qualpart
  else :
  	   inKey = enharmonic[keypart]+qualpart
  print "What is the Major 2-5-1 for", showKey, " ?"

# Get 2-5-1 sequence for inKey
  if inKey : 
  	seq = Major251(inKey)

# Main loop uses call fn that gets & checks answer
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









