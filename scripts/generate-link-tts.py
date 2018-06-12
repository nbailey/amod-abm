import csv

sourcefile = '../lib/ModeData/trips_attributes_nate.csv'
outfile = '../lib/LinkTravelTimesPrec5.py'

precision = 5
method = 'min'

link_tt_dict = dict()

print('link_travel_times = {', file=open(outfile, 'a+'))
with open(sourcefile) as f:
	reader = csv.reader(f)
	next(reader)
	for row in reader:
		olat = round(float(row[0]), precision)
		olng = round(float(row[1]), precision)
		dlat = round(float(row[2]), precision)
		dlng = round(float(row[3]), precision)
		duration = row[-1]
		link = (olng, olat, dlng, dlat)
		if link not in link_tt_dict.keys():
			link_tt_dict[link] = duration
		elif method == 'min' and duration < link_tt_dict[link]:
			link_tt_dict[link] = duration
		elif method == 'max' and duration > link_tt_dict[link]:
			link_tt_dict[link] = duration

for link in link_tt_dict.keys():
	print('{}: {}, '.format(link, duration), file=open(outfile, 'a'))

print('}', file=open(outfile, 'a', newline=''))