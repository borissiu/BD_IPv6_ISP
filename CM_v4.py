import requests
from bs4 import BeautifulSoup 

# CM_List = ['AS9808', 'AS56048', 'AS56040', 'AS56046', 'AS56041', 'AS140895', 'AS56047', 'AS56044', 'AS56042', 'AS134810']
  CM_List = ['AS9808', 'AS56048', 'AS56040', 'AS56046', 'AS56041', 'AS56044', 'AS56042', 'AS134810']
print('class-list "cl_ISP_CM_v4" ipv4 file')

for item in CM_List:
  url = 'https://bgp.he.net/' + item
  html = requests.get(url)
  soup = BeautifulSoup(html.text, 'html.parser')
  for row in soup.find('table', id = "table_prefixes4").tbody.findAll('tr'):
    columns = row.find_all('td')
    for td in columns:
      if td.a:
        print(td.a.contents[0])

