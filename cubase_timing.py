import sys

TICKS_16TH_NOTE = 120
TICKS_4TH_NOTE = 4 * TICKS_16TH_NOTE
FIELD_WIDTH = 8

# each split_spec is: [#subintervals, #notes, #4thnotes]
SPLIT_SPECS = ((3, 1, 0), (3, 2, 0), (3, 4, 0),
			   (4, 1, 0), (4, 3, 0), (4, 5, 0))

def cubase_time(ticks):
	notes_4th = ticks // TICKS_4TH_NOTE
	ticks = ticks % TICKS_4TH_NOTE
	notes_16th = ticks // TICKS_16TH_NOTE
	ticks = ticks % TICKS_16TH_NOTE
	return (notes_4th, notes_16th, ticks)

def print_split_spec(subs, notes_4th, notes_16th):
	print(f'{notes_4th} quarter notes, {notes_16th} sixteenth notes, {subs} subintervals')

def print_header():
	print(f"{'1/4th':^{FIELD_WIDTH}s}{'1/16th':^{FIELD_WIDTH}s}{'ticks':^{FIELD_WIDTH}s}")

def print_interval_boundaries(splits, notes_4th, notes_16th):
	split_ticks = (notes_4th * TICKS_4TH_NOTE + notes_16th * TICKS_16TH_NOTE) // splits
	for split in range(1, splits):
		ct = cubase_time(split_ticks * split)
		print(f'{ct[0]:^{FIELD_WIDTH}d}{ct[1]:^{FIELD_WIDTH}d}{ct[2]:^{FIELD_WIDTH}d}')
	print()

def run(args):
	if len(args) == 1:
		for spec in SPLIT_SPECS:
			print_split_spec(spec[0], spec[1], spec[2])
			print()
			print_header()
			print_interval_boundaries(spec[0], spec[1], spec[2])
	elif len(args) == 2 and args[1] == 'jupyter':
		try:
			notes_4th =  int(input('enter # of 1/4th notes in interval:  '))
			notes_16th = int(input('enter # of 1/16th notes in interval: '))
			splits =     int(input('enter # of subintervals:             '))
			print()
			print_header()
			print_interval_boundaries(splits, notes_4th, notes_16th)
		except ValueError as e:
			print(f'{e} is not an integer')
	elif len(args) == 4:
		try:
			print_header()
			print_interval_boundaries(int(args[1]), int(args[2]), int(args[3]))
		except ValueError as e:
			print(f'{e} is not an integer')
	else:
		print('need 3 integer args')

if __name__ == '__main__':
	run(sys.argv)
