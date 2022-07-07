from html.entities import html5
import bs4 as bs
import urllib.request

url = "https://www.espncricinfo.com/"
page = urllib.request.urlopen(url).read()
# html = page.read().decode("utf-8")
soup = bs.BeautifulSoup(page, "lxml")
print(soup.getText())