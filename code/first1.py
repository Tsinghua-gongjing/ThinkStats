import survey 
table = survey.Pregnancies() 
table.ReadRecords() 
print 'Number of pregnancies', len(table.records)

live_birth_num = 0
live_birth_ord1 = 0
live_birth_ord1_weeks_total = 0
live_birth_ordOther = 0
live_birth_ordOther_weeks_total = 0

for r in table.records:
	if r.outcome == 1:
		live_birth_num += 1
		if r.birthord == 1:
			live_birth_ord1 += 1
			live_birth_ord1_weeks_total += r.prglength
		else:
			live_birth_ordOther += 1
			live_birth_ordOther_weeks_total += r.prglength
live_birth_ord1_weeks_mean = live_birth_ord1_weeks_total / float(live_birth_ord1)
live_birth_ordOther_weeks_mean = live_birth_ordOther_weeks_total / float(live_birth_ordOther)
print "live_birth_num: %s, 1st: %s (mean week: %s), other: %s (mean week: %s)"%(live_birth_num, live_birth_ord1, live_birth_ord1_weeks_mean, live_birth_ordOther, live_birth_ordOther_weeks_mean)
# live_birth_num: 9148, 1st: 4413 (mean week: 38.6009517335), other: 4735 (mean week: 38.5229144667)


