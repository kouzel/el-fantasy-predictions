import requests
import json

from scripts.processData import processData

week = 33
isAllData= False
def getData():

    url ='https://www.dunkest.com/api/stats/table?season_id=17&mode=dunkest&stats_type=tot&weeks%5B%5D={0}&rounds%5B%5D=1&rounds%5B%5D=2&rounds%5B%5D=3&teams%5B%5D=31&teams%5B%5D=32&teams%5B%5D=33&teams%5B%5D=34&teams%5B%5D=35&teams%5B%5D=36&teams%5B%5D=37&teams%5B%5D=38&teams%5B%5D=39&teams%5B%5D=40&teams%5B%5D=41&teams%5B%5D=42&teams%5B%5D=43&teams%5B%5D=44&teams%5B%5D=45&teams%5B%5D=47&teams%5B%5D=48&teams%5B%5D=60&positions%5B%5D=1&positions%5B%5D=2&positions%5B%5D=3&player_search=&min_cr=4&max_cr=35&sort_by=pdk&sort_order=desc&iframe=yes'.format(week)

    all_weeks_url = 'https://www.dunkest.com/api/stats/table?season_id=17&mode=dunkest&stats_type=tot&weeks%5B%5D=33&weeks%5B%5D=32&weeks%5B%5D=31&weeks%5B%5D=30&weeks%5B%5D=29&weeks%5B%5D=28&weeks%5B%5D=27&weeks%5B%5D=26&weeks%5B%5D=25&weeks%5B%5D=24&weeks%5B%5D=23&weeks%5B%5D=22&weeks%5B%5D=21&weeks%5B%5D=20&weeks%5B%5D=19&weeks%5B%5D=18&weeks%5B%5D=17&weeks%5B%5D=16&weeks%5B%5D=15&weeks%5B%5D=14&weeks%5B%5D=13&weeks%5B%5D=12&weeks%5B%5D=11&weeks%5B%5D=10&weeks%5B%5D=9&weeks%5B%5D=8&weeks%5B%5D=7&weeks%5B%5D=6&weeks%5B%5D=5&weeks%5B%5D=4&weeks%5B%5D=3&weeks%5B%5D=2&weeks%5B%5D=1&rounds%5B%5D=1&rounds%5B%5D=2&rounds%5B%5D=3&teams%5B%5D=31&teams%5B%5D=32&teams%5B%5D=33&teams%5B%5D=34&teams%5B%5D=35&teams%5B%5D=36&teams%5B%5D=37&teams%5B%5D=38&teams%5B%5D=39&teams%5B%5D=40&teams%5B%5D=41&teams%5B%5D=42&teams%5B%5D=43&teams%5B%5D=44&teams%5B%5D=45&teams%5B%5D=47&teams%5B%5D=48&teams%5B%5D=60&positions%5B%5D=1&positions%5B%5D=2&positions%5B%5D=3&player_search=&min_cr=4&max_cr=35&sort_by=min&sort_order=desc&iframe=yes'
    data=requests.get(url=all_weeks_url if isAllData else url).json()

    processed= processData(data=data,isAllData=isAllData)

    f = open('./resources/data.json'.format(week),'w+')
    # f_example=(open('example.json',"w+"))
    # json.dump(processed[0],f_example,indent=2)
    json.dump(processed,f,indent=2)
