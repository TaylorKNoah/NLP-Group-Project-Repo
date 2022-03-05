from music21 import *

import music21

note_list = []

def get_note_list(midifile):

    parsed = music21.converter.parse(midifile)

    for elem in parsed.flat.notes:
    
        if(hasattr(elem,"name")):
            #print(elem.name + str(elem.octave))
            note = f'{elem.name}{str(elem.octave)}'

        else:

            highest_note= 'C0'
            for i in range(len(elem)):

                if len(highest_note) == 2: idx = 1
                elif len(highest_note) == 3: idx = 2

                if elem[i].octave > int(highest_note[idx]):
                    highest_note = f'{elem[i].name}{str(elem[i].octave)}'
                    note = highest_note
            
        note_list.append(note)
    return note_list