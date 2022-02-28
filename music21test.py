from music21 import *

import music21
parsed = music21.converter.parse('test123.mid')
for elem in parsed.flat.notes:

    print(elem.name)
    #print(elem.quarterLength)