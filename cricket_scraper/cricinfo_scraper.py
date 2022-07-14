from html.entities import html5
import bs4 as bs
import urllib.request
import json
import re

def extract_json():
    url = "https://www.espncricinfo.com/"
    page = urllib.request.urlopen(url).read()
    # html = page.read().decode("utf-8")
    soup = bs.BeautifulSoup(page, "html.parser")
    jsData = soup.findAll('script', type='application/json')
    # print(jsData[0])
    data = json.loads(jsData[0].text)
    result_list = data['props']['appPageProps']['data']['content']['feed']['results']
    return result_list

def extract_match_data(result_list):
    
    pass


if __name__ == "__main__":
    print(extract_json())
