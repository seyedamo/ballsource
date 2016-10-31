
# coding: utf-8

# In[51]:

import urllib2
from bs4 import BeautifulSoup
from lxml import html, etree
import datetime

response = urllib2.urlopen("http://www.rotoworld.com/teams/injuries/nba/all/")
injury = BeautifulSoup(response, 'lxml')
cp1_pnlInjuries = injury.find("div", {"id":"cp1_pnlInjuries"})
pb_list = cp1_pnlInjuries.findAll("div", {"class":"pb"})

todayS = datetime.date.today().strftime("%Y%m%d")

newFile = "./Rotoworld_injury_news_" + todayS + ".csv"
header = "team, player_name, player_position, player_status, player_injury_date, player_injury, player_return, update_report, update_impact, update_date, source"

outFile = open(newFile, 'w')
outFile.write(header + "\n")

for pb in pb_list:
    team = pb.find("div", {"class":"headline"}).find("div").text
    #print(team)
    tr_list = pb.find("table").findAll("tr")
    for tr in tr_list:
        #print(player)
        cols = tr.findAll("td")
        if cols[0].find("b"):
            #print("header")
            continue
        player_name = cols[0].find("a").text
        #print(player_name)
        update = cols[1].find("div")
        update_report = update.find("div", {"class":"report"}).text
        #print(update_report)
        update_impact = update.find("div", {"class":"impact"}).text
        #print(update_impact)
        update_date = update.find("div", {"class":"date"}).text
        #print(update_date)
        player_position = cols[2].text
        #print(player_position)
        player_status = cols[3].text
        player_injury_date = cols[4].text
        player_injury = cols[5].text
        player_return = cols[6].text
        newLine = ",".join([team, player_name, player_position, player_status, player_injury_date,
                           player_injury, player_return, update_report, update_impact, update_date, "Rotoworld"]).encode('utf-8').strip()
        outFile.write(newLine + "\n")


