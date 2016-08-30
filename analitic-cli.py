import main
import datetime
mydob = datetime.datetime(input("what year were you born in?"),input("and what month?"),input("and the day?"),input("hour?"),input("minuite?"),input("seccond?"))
reading1=main.Reading(mydob,raw_input("which town were you born in?"),raw_input("in which country?"))
for i in sorted(reading1.attributes,key=reading1.attributes.__getitem__):
    print i + " %s"% reading1.attributes[i]
