
import urllib2
from BeautifulSoup import BeautifulSoup

stations = ["CYSN", "CYHM", "KIAG", "KBUF", "CYYZ"]

metar_adds = """https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString={}&hoursBeforeNow={}&fields=raw_text"""

taf_adds = """https://www.aviationweather.gov/adds/dataserver_current/httpparam?datasource=tafs&requestType=retrieve&format=xml&mostRecentForEachStation=true&hoursBeforeNow=1&stationString={}"""

with open('reports.txt','w') as f:

    for i in stations:
        
        response = urllib2.urlopen(metar_adds.format(i,str(2)),timeout = 5)
        content = response.read()
        soup = BeautifulSoup(content)
        items = soup.findAll('raw_text')
        for t in items:
            f.write(t.string + '\n\n')
        

        response = urllib2.urlopen(taf_adds.format(i,),timeout = 5)
        content = response.read()
        soup = BeautifulSoup(content)
        f.write(soup.find('raw_text').string)
        f.write('\n\n')

        



    
