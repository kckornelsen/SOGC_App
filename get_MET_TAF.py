
import urllib2
from BeautifulSoup import BeautifulSoup
import datetime

stations = ["CYSN", "CYHM", "KIAG", "KBUF", "CYYZ","CYOO","CYTR"]

metar_adds = """https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString={}&hoursBeforeNow={}&fields=raw_text"""

taf_adds = """https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=1&stationString={}"""

with open('index.html','w') as f:
    f.write("RETRIEVED AT : " + datetime.datetime.now().strftime('%b %d %Y %H:%M') + " Local <br>\n  ")
    f.write("RETRIEVED AT: " + datetime.datetime.utcnow().strftime('%b %d %Y %H:%M') + " UTC<br><br>\n")

    for i in stations:
        
        response = urllib2.urlopen(metar_adds.format(i,str(2)),timeout = 5)
        content = response.read()
        soup = BeautifulSoup(content)
        items = soup.findAll('raw_text')
        if items is None:
            f.write('{} has no METAR! <br><br>\n'.format(i))
        else:
            
            for t in items:
                f.write(t.string + '<br><br>\n')
            

        response = urllib2.urlopen(taf_adds.format(i),timeout = 5)
        content = response.read()
        soup = BeautifulSoup(content)
        items = soup.find('raw_text')
        if items is None:
            f.write('{} has no TAF <br><br>\n'.format(i))
        else:
            for t in items:
                f.write(t.string + '<br><br>\n')

        
        f.write('<br><br>\n')

        



    
