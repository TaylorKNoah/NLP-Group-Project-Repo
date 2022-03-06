import sys, math

def get_tone_row(note_list):
	'''
	Generates a tone_row of the first 12 unique pitches
	found in the note_list	
	'''

	

	tone_row = []
	max_len = 12

	for note in note_list:
		# end case
		if len(tone_row) >= max_len:
			break

		# get pitch
		pitch = note[:-1]

		# check to see if pitch has been used
		#  if not, append note (pitch+oct)
		in_tone_row = False
		for i in range(len(tone_row)):
			idx = len(pitch)
			if pitch == tone_row[i][:idx]:
				in_tone_row = True
				break
				
		if not in_tone_row:
			tone_row.append(pitch)


	return tone_row

def jetsing_row(note_list):
	'''
	Determines the tone_row of the midifile
	Scores the midi on how well it adheres to the 
	tone row.	
	Higher score indicates the note_list breaks the rules
	 of tone rows more often.
	Octaves do not matter. Just pitches.
	ex:
	 - C4 C2
	 - tone row: C
	 - score: 0
	 - two possible tone rows with correct pictches: 0 error / 2 possible perfect rows = 0
	'''

	tone_row = get_tone_row(note_list)
	row_len = len(tone_row)
	print(f'Tone Row: {tone_row}')
	idx = 0
	score = 0

	for note in note_list:
		# if correct pitch found in tone row order
		pitch = note[:-1]

		if pitch == tone_row[idx]:
			idx += 1
			#ensure idx is 0<idx<len(tone_row)
			idx %= row_len
			continue
		# note in note list is incorrect according to tone_row
		else:
			score += 1

	# to get score representative of errors made to the most possible
	#   correct tone rows the piece could have achieved.
	# i.e. errors per possible tone_row.
	most_possible_tone_rows = math.ceil(len(note_list) / row_len)
	score /= most_possible_tone_rows	
	return score

def jetsing_oct(note_list):
	'''
	Scores the note_list on the use of pitches in far away octaves
	ex: 
	 - list: C2, C4
	 - score = 4-2 = 2
	higher score indicates larger octave differences in neighboring notes
	'''
	score = 0

	for i in range(len(note_list)-1):

		try:
			curr_oct = int(note_list[i][-1])
		except ValueError:
			print(f'Oct Value Error')
			print(f'Note: {note_list[i]}')
			print(f'Selected char for curr({i}) oct: {note_list[i][-1]}')
			print(f'Note List Dump:')
			for i in range(len(note_list)):
				print(f'Index({i}): {note_list[i]}')
			sys.exit(-1)

		try:
			next_oct = int(note_list[i+1][-1])
		except ValueError:
			print(f'Oct Value Error')
			print(f'Note: {note_list[i+1]}')
			print(f'Selected char for next oct: {note_list[i+1][-1]}')
			sys.exit(-1)



		s = curr_oct - next_oct
		if s < 0: s *= -1

		score += s

	# score represents average octave difference between all nerighboring notes
	score /= (len(note_list)-1)	
	return score