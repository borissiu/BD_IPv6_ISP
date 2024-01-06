# BD_IPv6_ISP
## Information collected from Hurricane Electric (https://www.he.net/)

### Prefixes Originated  (Not Prefixes Announced)
#### https://bgp.he.net/country/CN
+ https://bgp.he.net/AS4134
+ https://bgp.he.net/AS4837
+ https://bgp.he.net/AS9808

#### Import Class-list
https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CT_v6.txt
https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CU_v6.txt
https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CM_v6.txt

#### 
+ China Telecom (AS4134)
```
boris@Mac BD_IPv6_ISP % python3 6Any.py AS4134 | wc
     605     605    9039
```

+ China Unicom (AS4937)
```
boris@Mac BD_IPv6_ISP % python3 6Any.py AS4837 | wc
     448     448    7028
```

+ China Mobile (AS9808)
```
boris@Mac BD_IPv6_ISP % python3 6Any.py AS9808 | wc
    4657    4657   90840
```