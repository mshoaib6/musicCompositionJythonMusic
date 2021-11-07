# PierreCage.StructuresPourDeuxChances.py
 
from music import *
from random import randint, random, seed

seed(9079990)
numberOfNotes = 100    # notes in each parallel phrase

melody1 = Phrase(0.0)  # create phrase ; beginning of piece
melody2 = Phrase(0.0)  # create phrase ; beginning of piece
 
# generate random notes for first melody
for i in range(numberOfNotes):
   pitch = randint(C1, G9)
   duration = random() * 4.0
   dynamic = randint(0, 127)
   pan = random() * 1.0
   note = Note(pitch, duration, dynamic, pan) 
   melody1.addNote(note)
# melody 1 created
 
# generate random notes for second melody
for i in range(numberOfNotes):
   pitch = randint(C1, G9)
   duration = random() * 4.0
   dynamic = randint(0, 127)
   pan = random() * 1.0
   note = Note(pitch, duration, dynamic, pan) 
   melody2.addNote(note)
# melody 1 created
 
# combine
part = Part() # create empty part
part.addPhrase(melody1)
part.addPhrase(melody2)

instrument = randint(0,127)
print("instrument is: " + str(instrument))

tempo = randint(24,220)
print("tempo is: " + str(tempo))

part.setInstrument(instrument)
part.setTempo(tempo)

Play.midi(part)
