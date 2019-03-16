from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
kospi = soup.find('span', id = 'KOSPI_now') # span html 태그 이름, 검색 beautifulsoup span id
print(kospi.string)

