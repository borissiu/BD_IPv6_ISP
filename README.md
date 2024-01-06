# BD_IPv6_ISP
## Information collected from Hurricane Electric (https://www.he.net/)

### Prefixes Originated  (Not Prefixes Announced)
#### https://bgp.he.net/country/CN
+ https://bgp.he.net/AS4134#_prefixes6
+ https://bgp.he.net/AS4837#_prefixes6
+ https://bgp.he.net/AS9808#

#### Import Class-list
https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CT_v6.txt
https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CU_v6.txt
https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CM_v6.txt

#### 
+ China Telecom (AS4134)
```
CT_List=['AS4134', 'AS4809', 'AS4812', 'AS23724', 'AS4811', 'AS58461', 'AS4816', 'AS63835', 'AS58543', 'AS140903', 'AS140636', 'AS140083']

boris@Mac BD_IPv6_ISP % python3 CT.py | wc
    1193    1196   19777
```

+ China Unicom (AS4937)
```
CU_List=['AS4837', 'AS4808', 'AS17621', 'AS136958', 'AS17623', 'AS17622', 'AS140726', 'AS17816', 'AS138421', 'AS133119', 'AS135061', 'AS134542', 'AS140979', 'AS140716', 'AS10206', 'AS140886', 'AS140717', 'AS140707', 'AS139007', 'AS137539', 'AS136959', 'AS134543', 'AS133118']

boris@Mac BD_IPv6_ISP % python3 CU.py | wc
    5467    5470  105814
```

+ China Mobile (AS9808)
```
CM_List=['AS9808', 'AS56048', 'AS56040', 'AS56046', 'AS56041', 'AS56047', 'AS56044', 'AS56042' ,'AS134810']

boris@Mac BD_IPv6_ISP % python3 CM.py | wc
    8268    8271  161194
```