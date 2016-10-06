from bs4 import BeautifulSoup
import dryscrape
import json
import time



all_links = {}
REMAINING = True
page = 1
session = dryscrape.Session()
time.sleep(5)
dc_url = 'http://opendata.dc.gov'
while REMAINING:
    base_url= 'http://opendata.dc.gov/datasets?q=*&page=%s&sort_by=updated_at' % page
    session.visit(base_url)
    time.sleep(10)
    response = session.body()
    soup = BeautifulSoup(response, 'html.parser')
    data_links = {a.text: dc_url + a['href'] for a in soup.find_all('a', {'class':"dataset-link", 'itemprop':'url'})}
    all_links.update(data_links)
    page += 1
    print(data_links)

    if not data_links:
        REMAINING = False

parking_violations = {name.strip(): url for name, url in all_links.items() if 'Parking Violations in' in name}

with open('dc_parking_violations.json', 'w') as outfile:
    json.dump(parking_violations, outfile)
