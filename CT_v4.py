import requests
from bs4 import BeautifulSoup 

CT_List = ['AS4134', 'AS4809', 'AS4812', 'AS23724', 'AS4811', 'AS58461', 'AS58542', 'AS4816', 'AS58541', 'AS4835', 'AS140292', 'AS137697', 'AS136195', 'AS133774', 'AS63835', 'AS58539', 'AS141998', 'AS141771', 'AS140553', 'AS140279', 'AS140278', 'AS140276', 'AS140265', 'AS137695', 'AS137694', 'AS137693', 'AS137689', 'AS136190', 'AS136188']
print('class-list "cl_ISP_CT_v4" ipv4 file')

for item in CT_List:
  url = 'https://bgp.he.net/' + item
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  for row in soup.find('table', id = "table_prefixes4").tbody.findAll('tr'):
    columns = row.find_all('td')
    for td in columns:
      if td.a:
        print(td.a.contents[0])
