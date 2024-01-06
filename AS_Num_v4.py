import requests
from bs4 import BeautifulSoup 

i = 0; asNum = 0; v4RouteOrigin = 0
CT_List=[]; CU_List=[]; CM_List=[]
url = 'https://bgp.he.net/' + 'country/CN'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
for row in soup.find('table', id = "asns").tbody.findAll('tr'):
  columns = row.find_all('td')
  i = 0
  for td in columns:
    i += 1
    if td.a:
      asNum=td.a.contents[0]
      name=td.a['title']
    if ( i % 4 == 0 ):
      v4RouteOrigin = int(td.renderContents().decode().replace(',', ''))
    if ( v4RouteOrigin >= 50 and "Unicom".lower() in name.lower()):
      # print(asNum, name, v4RouteOrigin)
      v4RouteOrigin = 0
      CU_List.append(asNum)
    if ( v4RouteOrigin >= 50 and ("China Mobile".lower() in name.lower() or "ChinaMobile".lower() in name.lower())):
      # print(asNum, name, v4RouteOrigin)
      v4RouteOrigin = 0
      CM_List.append(asNum)
    if ( v4RouteOrigin >= 50 and ("ChinaTelecom".lower() in name.lower() or "China Telecom".lower() in name.lower())):
      # print(asNum, name, v4RouteOrigin)
      v4RouteOrigin = 0
      CT_List.append(asNum)
      
print("CU_List =", list( dict.fromkeys(CU_List) ))
print("CM_List =", list( dict.fromkeys(CM_List) ))
print("CT_List =", list( dict.fromkeys(CT_List) ))

