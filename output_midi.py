from MIDI import MIDIFile

def get_note(track):
    print(track)
    notes = []
    new_note_line = 'NOTE_ON'
    for line in track:
        if new_note_line in str(line):
            print(f'{len(str(line))}: {str(line)}')
            notes.append([str(line)[20], str(line)[21]])
    
    return notes

def parse(file):
    c=MIDIFile(file)
    c.parse()
    print(str(c))
    for idx, track in enumerate(c):
        track.parse()
        #print(f'Track {idx}:')
        #print(str(track))

        print(f'{len(track)}')
        new_note_line = 'NOTE_ON'
        if new_note_line in str(track):
            notes = get_note(track)
    
    print(notes)





parse('./test.mid')