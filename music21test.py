from music21 import *

import music21
parsed = music21.converter.parse('twinkleweird.mid')
for elem in parsed.flat.notes:


    if(hasattr(elem,"name")):
        print(elem.name + str(elem.octave))
    else:

        for i in range(len(elem)):
            print(elem[i].name + str(elem[i].octave),end=' ')
        print("")



    #print(elem.quarterLength)