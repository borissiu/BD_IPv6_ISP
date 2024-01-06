import requests
from bs4 import BeautifulSoup 

CU_List = ['AS4837', 'AS4808', 'AS17621', 'AS136958', 'AS17623', 'AS17622', 'AS140726', 'AS17816', 'AS139007', 'AS134543']

for item in CU_List:
  url = 'https://bgp.he.net/' + item
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  for row in soup.find('table', id = "table_prefixes6").tbody.findAll('tr'):
    columns = row.find_all('td')
    for td in columns:
      if td.a:
        print(td.a.contents[0])
