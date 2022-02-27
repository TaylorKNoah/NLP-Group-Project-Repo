from MIDI import MIDIFile
import copy

def get_note(line):
    '''
    generates note,oct pairs for each note in a track in 
    time order. returns [[note, oct], [note, oct], ...]
    '''

    line = str(line)

    time_idx_s = line.find('@')+1
    time_idx_e = line.find(' ')
    note_time = int(line[time_idx_s: time_idx_e])

    note_idx = line.find('NOTE_ON') + 11
    note = line[note_idx]
    octave = int(line[note_idx+1])
    
    note = [note_time, note, octave]
    
    return note

def organize_by_time(notes):
    '''
    Takes note collection [[time, note, oct], [t,n,o], ...] 
     and returns collection organized by time: [ [t, [n,o], [n,o]], ... , [t_n, [n,o], [n,o]] ]   
    '''
    time = -1
    notes_by_time = []
    notes_of_same_time = []

    for note in notes:
        # if time changes
        if note[0] > time:
            # if the first update don't append
            if time > -1:
                notes_by_time.append(copy.deepcopy(notes_of_same_time))
                notes_of_same_time.clear()
            
            # update current time, append time to current note collection
            time = note[0]
            notes_of_same_time.append(time)

        # append note and octave to current note collection at time
        notes_of_same_time.append([note[1], note[2]])

    return notes_by_time



def parse(file):
    '''
    Takes a Midi file and parses the tracks.
    Sends tracks to helper func to get array of lists 
    containing note, oct pairs.
    '''
    midi=MIDIFile(file)
    midi.parse()
    print(str(midi))
    notes = []

    for idx, track in enumerate(midi):
        track.parse()

        for line in track:
            line = str(line)
            if 'NOTE_ON' in line:
                notes.append(get_note(line))
    
    print(f'Notes gathered:\n {notes}')

    nbt = organize_by_time(notes)

    print(f'\n\nNotes organized by time: \n{nbt}')

parse('C2_C4.mid')