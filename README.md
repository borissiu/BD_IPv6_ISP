# BD_IPv6_ISP
## Information collected from Hurricane Electric (https://www.he.net/)

### Prefixes Originated  (Not Prefixes Announced)
#### https://bgp.he.net/country/CN
+ https://bgp.he.net/AS4134#_prefixes4
+ https://bgp.he.net/AS4837#_prefixes4
+ https://bgp.he.net/AS9808#_prefixes4
+ https://bgp.he.net/AS4134#_prefixes6
+ https://bgp.he.net/AS4837#_prefixes6
+ https://bgp.he.net/AS9808#_prefixes6

#### Import Class-list
import-periodic class-list cl_ISP_CT_v4 https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CT_v4.txt period 300  
import-periodic class-list cl_ISP_CU_v4 https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CU_v4.txt period 300  
import-periodic class-list cl_ISP_CM_v4 https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CM_v4.txt period 300  
import-periodic class-list cl_ISP_CT_v6 https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CT_v6.txt period 300  
import-periodic class-list cl_ISP_CU_v6 https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CU_v6.txt period 300  
import-periodic class-list cl_ISP_CM_v6 https://raw.githubusercontent.com/borissiu/BD_IPv6_ISP/main/cl_ISP_CM_v6.txt period 300  

#### 
```
vADC-200-Active#show class-list
Name                               Type                     IP       Subnet   DNS      String   Location
cl_ISP_CM_v4                       ipv4                     0        16377    0        0        file
cl_ISP_CM_v6                       ipv6                     0        8267     0        0        file
cl_ISP_CT_v4                       ipv4                     0        6336     0        0        file
cl_ISP_CT_v6                       ipv6                     0        2506     0        0        file
cl_ISP_CU_v4                       ipv4                     0        5823     0        0        file
cl_ISP_CU_v6                       ipv6                     0        5330     0        0        file
Total: 6
vADC-200-Active#
```

```
vADC-200-Active#show log | inc Classlist
Jan 07 2024 07:54:29 Info        [PBSLB]:Classlist cl_ISP_CM_v4: loaded into AX.
Jan 07 2024 07:54:29 Info        [PBSLB]:Classlist cl_ISP_CM_v4: Duplicate IP/Mask 36.138.110.0/24 detected on line 10975.
Jan 07 2024 07:54:29 Info        [PBSLB]:Classlist cl_ISP_CM_v4: Duplicate IP/Mask 202.46.224.0/22 detected on line 10888.
Jan 07 2024 07:54:29 Info        [PBSLB]:Classlist cl_ISP_CM_v4: Duplicate IP/Mask 112.33.120.0/24 detected on line 10513.
Jan 07 2024 07:54:17 Info        [PBSLB]:Classlist cl_ISP_CT_v4: loaded into AX.
Jan 07 2024 07:54:17 Warning     [PBSLB]:Classlist cl_ISP_CT_v4 Too many log messages already generated. Subsequent messages will not be logged.
Jan 07 2024 07:54:17 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 211.151.0.0/16 detected on line 3049.
Jan 07 2024 07:54:17 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 211.99.192.0/19 detected on line 3048.
Jan 07 2024 07:54:17 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 211.99.160.0/19 detected on line 3047.
Jan 07 2024 07:54:17 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 210.77.128.0/19 detected on line 3045.
Jan 07 2024 07:54:17 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 124.250.0.0/15 detected on line 3035.
Jan 07 2024 07:54:17 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 120.134.0.0/15 detected on line 3023.
Jan 07 2024 07:54:16 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 120.133.0.0/16 detected on line 3016.
Jan 07 2024 07:54:16 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 120.132.128.0/17 detected on line 3013.
Jan 07 2024 07:54:16 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 59.151.0.0/17 detected on line 2975.
Jan 07 2024 07:54:16 Info        [PBSLB]:Classlist cl_ISP_CT_v4: Duplicate IP/Mask 58.83.128.0/17 detected on line 2974.
Jan 07 2024 07:54:05 Info        [PBSLB]:Classlist cl_ISP_CU_v4: loaded into AX.
Jan 07 2024 07:54:05 Info        [PBSLB]:Classlist cl_ISP_CU_v4: Duplicate IP/Mask 103.192.132.0/22 detected on line 1257.
Jan 07 2024 07:53:55 Info        [PBSLB]:Classlist cl_ISP_CM_v6: loaded into AX.
Jan 07 2024 07:53:45 Info        [PBSLB]:Classlist cl_ISP_CU_v6: loaded into AX.
Jan 07 2024 07:53:24 Info        [PBSLB]:Classlist cl_ISP_CT_v6: loaded into AX.
vADC-200-Active#
```

+ China Telecom (IPv4)
```
CT_List = ['AS4134', 'AS4809', 'AS4812', 'AS23724', 'AS4811', 'AS58461', 'AS58542', 'AS4816', 'AS58541', 'AS4835', 'AS140292', 'AS137697', 'AS136195', 'AS133774', 'AS63835', 'AS58539', 'AS141998', 'AS141771', 'AS140553', 'AS140279', 'AS140278', 'AS140276', 'AS140265', 'AS137695', 'AS137694', 'AS137693', 'AS137689', 'AS136190', 'AS136188']

boris@Mac BD_IPv6_ISP % python3 CT_v4.py | wc
    6349    6352  100468
```

+ China Unicom (IPv4)
```
CU_List = ['AS4837', 'AS4808', 'AS17621', 'AS136958', 'AS17623', 'AS17622', 'AS140726', 'AS17816', 'AS138421', 'AS133119', 'AS135061', 'AS140979', 'AS140716', 'AS10206', 'AS139007', 'AS136959', 'AS134543']

boris@Mac BD_IPv6_ISP % python3 CU_v4.py | wc
    5825    5828   91758
```

+ China Mobile (IPv4)
```
CM_List = ['AS9808', 'AS56048', 'AS56040', 'AS56046', 'AS56041', 'AS56047', 'AS56044', 'AS56042', 'AS134810']

boris@Mac BD_IPv6_ISP % python3 CM_v4.py | wc
   16381   16384  262019
```


+ China Telecom (IPv6)
```
CT_List = ['AS4134', 'AS4809', 'AS4812', 'AS23724', 'AS4811', 'AS58461', 'AS4816', 'AS140330', 'AS140292', 'AS63835', 'AS58543', 'AS140903', 'AS140647', 'AS140636', 'AS140345', 'AS140265', 'AS140083', 'AS137693', 'AS137689', 'AS131285', 'AS140329']

boris@Mac BD_IPv6_ISP % python3 CT_v6.py | wc
    2507    2510   44225
```

+ China Unicom (IPv6)
```
CU_List = ['AS4837', 'AS4808', 'AS17621', 'AS136958', 'AS17623', 'AS17622', 'AS140726', 'AS17816', 'AS139007', 'AS134543']

boris@Mac BD_IPv6_ISP % python3 CU_v6.py | wc
    5331    5334  103180
```

+ China Mobile (IPv6)
```
CM_List = ['AS9808', 'AS56048', 'AS56040', 'AS56046', 'AS56041', 'AS56047', 'AS56044', 'AS56042', 'AS134810']

boris@Mac BD_IPv6_ISP % python3 CM_v6.py | wc
    8268    8271  161194
```