import sys

TICKS_16TH_NOTE = 120
TICKS_4TH_NOTE = 4 * TICKS_16TH_NOTE
TICKS_BAR = 4 * TICKS_4TH_NOTE

# each split_spec is: [#intervals, #notes, #4thnotes]
SPLIT_SPECS = ((3, 1, 0), (3, 2, 0), (3, 4, 0),
			   (4, 1, 0), (4, 3, 0), (4, 5, 0))

class CubaseTime:
    
	def __init__(self, ticks):
		self._notes_4th = ticks // TICKS_4TH_NOTE
		ticks = ticks % TICKS_4TH_NOTE
		self._notes_16th = ticks // TICKS_16TH_NOTE
		self._ticks = ticks % TICKS_16TH_NOTE

	def __str__(self):
		return f'{self._notes_4th} {self._notes_16th} {self._ticks}'

def print_split(splits, notes_4th, notes_16th):

	print(f'{splits} splits, {notes_4th} 4th notes, {notes_16th} 16th notes')

	split_ticks = (notes_4th * TICKS_4TH_NOTE + notes_16th * TICKS_16TH_NOTE) // splits
	for split in range(1, splits):
		ct = CubaseTime(split_ticks * split)
		print(ct)

	print()

def main(args):

	if len(args) == 1:
		for spec in SPLIT_SPECS:
			print_split(spec[0], spec[1], spec[2])
	elif len(args) == 4:
		try:
			print_split(int(args[1]), int(args[2]), int(args[3]))
		except ValueError as e:
			print(f'{e} is not an integer')
	else:
		print('need 3 integer args')

if __name__ == '__main__':
	main(sys.argv)