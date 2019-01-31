""" Interactive version that asks user to fill in the 
 three keys/chords in the 2-5-1.  
 Original was Circle_of_4ths.py, which asked user to input 
 a key and quality and then returned the Major 2-5-1.
 Written by Jim Baer to drive home Cicle of 4ths """

import re
import sys
import random

 # KeyCenter Fn --  Flow:
 # Locate key in C4 with C4.index("Key") and store as i
 # Determine quality of input and use if statement to adjust
 #    indices to return the key center and related minor as a list.    
 #  E.g., if Eb7 is input then i=3 and the answers are Ab and F-7
 #     

def KeyCenter(seq) :
 	if inKey[-2:] == "-7" :
 		idx = C4.index(inKey[:-2])  
 		if idx > 9 : idx = idx - 12 # To prevent index out of range error
 		seq0 = C4[idx+2]
 	elif inKey[-1] == "7" :
 		idx = C4.index(inKey[:-1])
 		if idx > 10 : idx = idx - 12 # To prevent index out of range error
 		seq0 = C4[idx+1]
 	else :
 		idx = C4.index(inKey)
 		seq0 = inKey
 	seq1 = RelMin[seq0]+'-7'
 	seq = [seq0,seq1]
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
#
	if len(seq[pos])>1 :
		if seq[pos][1] in ['b','#'] :
			altkey = enharmonic[seq[pos][:2]]+quality[pos]
#
	if ans in [seq[pos],altkey] :
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
#  Relative minor dict
RelMin = {'C':'A','F':'D','Bb':'G','Eb':'C','Ab':'F','Db':'Bb','Gb':'Eb',
           'B':'Ab','E':'Db','A':'Gb','D':'B','G':'E'}

# Quality - rearranged from Minor251 game (-7,7,) to
#    make it easier to use index in check_answer function
quality = ('','-7','7')
# Enharmonic dict
enharmonic = {'A#':'Bb', 'B#':'C', 'C#':'Db', 'D#':'Eb', 'E#':'F', 
    'F#':'Gb', 'G#':'Ab','Ab':'G#','Bb':'A#', 'Cb':'B','Db':'C#','Eb':'D#',
    'Fb':'E','Gb':'F#','F':'E#','C':'B#','B':'Cb'}
# prompt is labels for input requests
prompt = ('Enter the diatonic major key> ','Enter the related minor key> ')

# main loop - do until opt out
print "--> Type 'q' to quit at any time <--"
more = 'Y'
while more in ['Y','y'] :
#Randomly choose a key and quality as variable inKey
#  showkey variable used so enharmonic keys can be presented, not just ones in C4
  keypart = random.choice(C4e)
  qualpart = random.choice(quality)
  showKey = keypart+qualpart
  if keypart in C4 :
  	   inKey = keypart+qualpart
  else :
  	   inKey = enharmonic[keypart]+qualpart
  print "What is the key center for", showKey, " ?"
  #debug code - remove
  # end debug code
# Get answer for key center
  if inKey : 
  	seq = KeyCenter(inKey)

# Main loop uses call fn that gets & checks answer
#  - if fail call again
#  - if pass, then call fun to get & check answer2, then 3
  i = 0
  while i < 2 :
  	if check_answer(i,seq) :
  		i=i+1
  print "Congratulations!"

# want to introduct logic switch to continue playing or quit
# need to figure out quit option in check_anser fn also.
  more = raw_input("Try again(Y/N)? ")









