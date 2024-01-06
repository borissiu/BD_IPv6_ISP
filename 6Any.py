import sys
import requests
from bs4 import BeautifulSoup 

url = 'https://bgp.he.net/' + sys.argv[1]
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# print('class-list "cl_ISP_AnyAS_v6" ipv6 file')
for row in soup.find('table', id = "table_prefixes6").tbody.findAll('tr'):
  columns = row.find_all('td')
  for td in columns:
    if td.a:
      print(td.a.contents[0])