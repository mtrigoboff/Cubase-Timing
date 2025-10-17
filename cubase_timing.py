TICKS_PER_16TH_NOTE = 120
TICKS_PER_4TH_NOTE = 4 * TICKS_PER_16TH_NOTE
TICKS_PER_BAR = 4 * TICKS_PER_4TH_NOTE

# each aublist is: [#intervals, #notes, #4thnotes]
SPLITS = [[3, 0, 2]]

class CubaseTime:
    
	def __init__(self, ticks):
		self._notes_4th = ticks // TICKS_PER_4TH_NOTE
		ticks -= self._notes_4th * TICKS_PER_4TH_NOTE
		self._notes_16th = ticks // TICKS_PER_16TH_NOTE
		self._ticks = ticks % TICKS_PER_16TH_NOTE

	@property
	def notes_4th(self):			# getter
		return self._notes_4th

	@property
	def notes_16th(self):			# getter
		return self._notes_16th

	@property
	def ticks(self):				# getter
		return self._ticks
	
	def __str__(self):
		return f'{self.notes_4th} 4th notes, {self.notes_16th} 16th notes, {self.ticks} ticks'

def main():
	print()
	for split in SPLITS:
		splits = split[0]
		notes_4th = split[1]
		notes_16th = split[2]

		print(f'{splits} splits, {notes_4th} 4th notes, {notes_16th} 16th notes')

		ct = CubaseTime(notes_4th * TICKS_PER_4TH_NOTE + notes_16th * TICKS_PER_16TH_NOTE)
		print(ct)

if __name__ == '__main__':
	main()