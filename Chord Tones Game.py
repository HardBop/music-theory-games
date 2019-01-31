#Chord Tones Game
# Game selects a random key & quality then asks for:
#  chord tones (triad + 7)
#  9, tritone, 13
#
# built borrowing functions from the C4game_e.py
#
# import packages
#
import re
import sys
import random
#
# define common lists and dicts
#
# basic sequence of chromatic scale
C4 = ('C','F','Bb','Eb','Ab','Db','Gb','B','E','A','D','G')
# extended chromatic scale to allow enharmonic representations
C4e = ('C','F','Bb','A#','Eb','D#','Ab','G#','Db','C#','Gb',
	    'F#','B','E','A','D','G')
# Quality
quality = ('-7','7','')
# Enharmonic dict
enharmonic = {'A#':'Bb', 'B#':'C', 'C#':'Db', 'D#':'Eb', 'E#':'F', 
    'F#':'Gb', 'G#':'Ab','Ab':'G#','Bb':'A#', 'Cb':'B','Db':'C#','Eb':'D#',
    'Fb':'E','Gb':'F#','F':'E#','C':'B#','B':'Cb'}
#
# prompt is labels for input requests
prompt = ('Enter the tonic, 3rd , 5th, & 7th')
#
# main loop
#
print "--> Type 'q' to quit at any time <--"
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
  print "What are the chord tones for", showKey, " ?"
  #
  # This is incomplete - have not formed the main loop yet
  
