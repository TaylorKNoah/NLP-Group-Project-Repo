from midi_parser import get_note_list
from jetsing_utils import jetsing_row, jetsing_oct
import sys

if len(sys.argv) > 2: 
	print(f'Error: Got {len(sys.argv)} args. Expected 2.')
	print(f'To Use: jetsing.py <midifile.midi>')
	sys.exit(-1)

midifile = sys.argv[1]

print('='*128)
print(f'Analyzing {midifile}...')
print('='*128)

note_list = get_note_list(midifile)
print('-'*128)
print(f'Note List: {note_list}')
print('-'*128)

row_score = jetsing_row(note_list)
oct_score = jetsing_oct(note_list)


print('-'*128)
print(f'Scores for {midifile}:')
print(f'JETSING-ROW: {row_score}')
print(f'JETSING-OCT: {oct_score}')
print('-'*128)
