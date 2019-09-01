from datetime import date
from dateutil.rrule import rrule, DAILY

today = date.timetuple(date.today())[0:3]

a = date(today[0], today[1], today[2])
b = date((today[0] + 1), today[1], today[2])

for dt in rrule(DAILY, dtstart=a, until=b):
    title = dt.strftime("%Y-%m-%d")
    title = 'todo-' + title + '.txt'
    with open(title, 'w') as f:
        line = dt.strftime("(%B %d, %Y)")
        line = '\tTo Do ' + line + ':\t\n\n\n1.)\n\n2.)\n\n3.)\n\n4.)\n\n5.)\n\n6.)'
        f.write(line)
