# Key Center
""" Game to hone ability to recognize key centers --
for any key/quality combination from a major or minor 2-5-1 
the player is asked to provide the key center -- i.e., the "1"
with quality.  E.g., for E7b9b13 the correct response would
be A-7.

Edited from original circle of 4ths game."""

import re
import sys
import random

 # Major251 fn --  Flow:
 # Locate key in C4 with C4.index("Key") and store as i
 # Determine quality of input and use if statement to adjust
 #    indices to return the 2-5-1 sequence for Cycle of 4ths in list seq.
 #  E.g., if Eb7 is input then i=3 and the relative 2-5-1 
 #     would be Bb-7, Eb7, Ab


def KeyCenter(root,qual) :
  idx = C4.index(root)
  if qual[:2] == '-7' :
    if idx > 9 : idx = idx - 12 # To prevent index out of range error
    true_root = C4[idx+2]
  elif qual[:1] == '7' :
    if idx > 10 : idx = idx - 12 # To prevent index out of range error
    true_root = C4[idx+1]
  if qual in ['-7b5','7b9b13'] :
    true_key = true_root + '-7'
  else :
    true_key = true_root 
  return true_key 

def check_answer(true_key) :
  ans = raw_input("Key Center? >")
  UC = ans[0].upper()
  if len(ans) == 1 :
    ans = UC 
  else :
    ans = UC + ans[1:]
  if true_key[-2:] == '-7': 
    enharmonic_key = enharmonic[true_key[:-2]] + '-7'
  else : 
    enharmonic_key = enharmonic[true_key]
  if ans in [true_key,enharmonic_key] :
    result = 1 
  else : 
    print "Nope - Guess Again"
    result = 0
  return result

# Main
# set up basic sequence of chromatic scale
C4 = ('C','F','Bb','Eb','Ab','Db','Gb','B','E','A','D','G')
# Quality
quality = ('-7','7','-7b5','7b9b13')
# Enharmonic dict
enharmonic = {'A#':'Bb', 'B#':'C', 'C#':'Db', 'D#':'Eb', 'E#':'F', 
    'F#':'Gb', 'G#':'Ab','Ab':'G#','Bb':'A#', 'Cb':'B','Db':'C#','Eb':'D#',
    'Fb':'E','Gb':'F#','A':'A','B':'Cb','C':'B#','D':'D','E':'Fb','F':'E#',
    'G':'G'}

# main loop - do until opt out
more = 'y'
while more in ['Yes','y'] :
#Randomly choose a key and quality as variable inKey
  rand_root = random.choice(C4)
  rand_qual = random.choice(quality)
  inKey = rand_root + rand_qual
  
  print "What is the key center for", inKey, " ?"
  

# Call keycenter function to get the answer
  if inKey :
  	true_key = KeyCenter(rand_root,rand_qual)
  else :
  	if raw_input("Quit?") not in ['No','n'] :
  		sys.exit(0)

# Main look uses call fn that gets & checks answer
#  - if fail call again
#  - if pass, then call fun to get & check answer2, then 3
  i = 0
  while i < 1 :
  	if check_answer(true_key) :
  		i=i+1
  print "Congratulations!"
  
# want to introduct logic switch to continue playing or quit
# need to figure out quit option in check_anser fn also.
  more = raw_input("Try again(Yes/y)? ")









