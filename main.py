import requests
import nltk
class Reading:
    def __init__(self,dob,town,country):
        self.signs = []
        text = self.getText(self.buildURL(dob,town,country))
        eachSign = self.splitText(text)
        for i in eachSign:
            try:
                self.signs.append(self.Sign(i))
            except IndexError:
                pass
        self.attributes = self.mergeSignAttributes()
    def mergeSignAttributes(self):
        allAttributes = {}
        for sign in self.signs:
            for attribute in sign.attributes:
                try:
                    allAttributes[attribute[0]] +=1
                except KeyError:
                    allAttributes[attribute[0]] = 1
        return allAttributes
    class Sign:
        def __init__(self,signString):
            self.position    = signString.split("\r\r")[0].split("is in")[1]
            self.planet      = signString.split("\r\r")[0].split("is in")[0]
            self.description = signString.split("\r\r")[1]
            self.tokens = nltk.word_tokenize(self.description)
            self.tags = nltk.pos_tag(self.tokens)
            self.attributes = self.filterTags("JJ")
        def filterTags(self,tagString):
            returnList = []
            for tag in self.tags:
                if tag[1] == tagString:
                    returnList.append(tag)
            return returnList
    def buildURL(self,dob,town,country,urlpattern = "https://alabe.com/cgi-bin/chart/astrobot.cgi?INPUT1=&INPUT2=&MONTH={month}&DAY={day}&YEAR={year}&HOUR={hour}&MINUTE={minuite}&AMPM=PM&TOWN={town}&COUNTRY={country}&STATE=&INPUT9=&Submit=Submit"):
        return (urlpattern.format(month=dob.month, day=dob.day, year=dob.year,hour=dob.hour,minuite=dob.minute,town=town,country=country))
    def getText(self,url):
        return requests.get(url).text
    def splitText(self,rawText):
        mainText = rawText.split("\rwith your Report!")[1].split("If you would like a detailed")[0].replace("\t"," ")
        SignList = mainText.replace("<br>","").split("\r\r\r")[2:]
        return SignList
