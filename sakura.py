#sakura.py

# four means (four beats per bar)
# four means each beat = QUARTER_NOTE = 1/4 WHOLE_NOTE
# four QUARTER/bar = one WHOLE_NOTE per bar

from music import *

pit1_2 = [A4, A4, B4] * 2
pit3_4 = [A4, B4, C5, B4, A4, B4, A4, F4]
pit5_6 = [E4, C4, E4, F4, E4, E4, C4]
pit13_14 = [D4, E4, B4, A4, F4, E4]

dur1_2 = [QN, QN, HN] * 2
dur3_4 = [QN, QN, QN, QN, QN, EN, EN, HN]
dur5_6 = [QN, QN, QN, QN, QN, EN, EN]
dur13_14 = [QN, QN, EN, EN, QN, WN]

# create empty phrase; construct the theme from the motifs given above

theme = Phrase()
theme.addNoteList(pit1_2, dur1_2)

for i in range(2):
   theme.addNoteList(pit3_4, dur3_4)
   theme.addNoteList(pit5_6, dur5_6)
   if i == 0:
      theme.addNote(E4,HN)
   else:
      theme.addNote(B3,HN)
      
theme.addNoteList(pit1_2, dur1_2)
theme.addNoteList(pit13_14, dur13_14)

# set instrument and tempo 
theme.setInstrument(PIANO) # default is PIANO as well
theme.setTempo(100) # default is 60 beats per minute, we can change it to 100 to make it play faster.

# play the theme sakura
Play.midi(theme)