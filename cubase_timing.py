TICKS_PER_16TH_NOTE = 120
TICKS_PER_4TH_NOTE = 4 * TICKS_PER_16TH_NOTE
TICKS_PER_BAR = 4 * TICKS_PER_4TH_NOTE

# each aublist is: [#intervals, #notes, #4thnotes]
INTERVALS= [[3, 0, 2]]

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


class Interval:

	def __init__(self, intervals, notes, notes_4th):
		self._intervals = intervals
		self._notes = notes
		self._notes_4th = notes_4th

	@property
	def intervals(self):			# getter
		return self.intervals

	@property
	def notes(self):				# getter
		return self._notes

	@property
	def notes_4th(self):			# getter
		return self._notes_4th

def main():
	for interval in INTERVALS:
		pass