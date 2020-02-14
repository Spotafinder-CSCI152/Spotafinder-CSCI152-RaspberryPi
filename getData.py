import csv
i = 0
flag = False

def countDevices():
	with open('output.csv',newline='') as csvfile:
		cr = csv.DictReader(csvfile)
		for row in cr:
			for j in row.items():
				if flag:
					i = i + 1
				if j[1][0] == 'Station MAC':
					flag = True
		return i