import requests
from bs4 import BeautifulSoup 

CT_List=['AS4134', 'AS4809', 'AS4812', 'AS23724', 'AS4811', 'AS58461', 'AS4816', 'AS63835', 'AS58543', 'AS140903', 'AS140636', 'AS140083']
print('class-list "cl_ISP_CT_v6" ipv6 file')

for item in CT_List:
  url = 'https://bgp.he.net/' + item
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  for row in soup.find('table', id = "table_prefixes6").tbody.findAll('tr'):
    columns = row.find_all('td')
    for td in columns:
      if td.a:
        print(td.a.contents[0])
