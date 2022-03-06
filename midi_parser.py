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

def get_left_right_seperation(midifile):

    note_value = 0
    note_value_octave = 0
    note_total = 0

    parsed = music21.converter.parse(midifile)
    for elem in parsed.flat.notes:
        if (hasattr(elem, "name")):
            if(elem.name == "A" or elem.name == "A#" or elem.name == "A-"):
                note_value += 8
            elif(elem.name == "B" or elem.name == "B#" or elem.name == "B-"):
                note_value += 9 * elem.octave
            elif("#" in elem.name or "-" in elem.name):
                note_value += int(elem.name[0],base=17) - 9
            else:
                note_value += int(elem.name,base=17) - 9

            note_value_octave += elem.octave
            note_total += 1

        else:
            for i in range(len(elem)):
                if (elem[i].name == "A" or elem[i].name == "A#" or elem[i].name == "A-"):
                    note_value += 8
                elif (elem[i].name == "B" or elem[i].name == "B#" or elem[i].name == "B-"):
                    note_value += 9
                elif ("#" in elem[i].name or "-" in elem[i].name):
                    note_value += int(elem[i].name[0],base=17) - 9
                else:
                    note_value += int(elem[i].name, base=17)  - 9

                note_value_octave += elem[i].octave
                note_total += 1


    the_note = round(note_value/note_total)
    the_octave = round(note_value_octave/note_total)

    if(the_note == 3):
        return "C"+str(the_octave)
    elif(the_note == 4):
        return "D" + str(the_octave)
    elif (the_note == 5):
        return "E" + str(the_octave)
    elif (the_note == 6):
        return "F" + str(the_octave)
    elif (the_note == 7):
        return "G" + str(the_octave)
    elif (the_note == 8):
        return "A" + str(the_octave)
    elif (the_note == 9):
        return "B" + str(the_octave)
