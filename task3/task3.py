import re
iproute_file = open('ShowIpRoute.txt','r')
list = iproute_file.read()
list = re.split(r"\n\n", list)#каждая строка отдельно
codes_dict = {
    'L':'local',
    'C':'connected',
    'S':'static',
    'R':'RIP',
    'M':'mobile',
    'B':'BGP',
    'D':'EIGRP',
    'EX':'EIGRP external',
    'O':'OSPF',
    'IA':'OSPF inter area',
    'N1':'OSPF NSSA external type 1',
    'N2':'OSPF NSSA external type 2',
    'E1':'OSPF external type 1',
    'E2':'OSPF external type 2',
    'E':'GP',
    'i':'IS-IS',
    'su':'IS-IS summary',
    'L1':'IS-IS level-1',
    'L2':'IS-IS level-2',
    'ia':'IS-IS inter area',
    '*':'candidate default',
    'U':'per-user static route',
    'o':'ODR',
    'P':'periodic downloaded static route',
    'H':'NHRP',
    'l':'LISP',
    'a':'application route',
    '+':'replicated route',
    '%':'next hop override'}
n=0
while n<len(list):
    commad = (list[n]).split(', ')
    print('The entry is:')
    print(''.join(list[n]))
    print()
    spaced = (' '.join(commad)).split(' ')

    if len(commad) == 1:
        Gateway = True

    elif len(commad) == 3:
        print("Protocol: ", codes_dict[''.join(spaced[-9])])
        print("Prefix: ", spaced[-8])
        print("AD/Metric: ", spaced[-6])
        print("nexthop: ", spaced[-4])
        print("lastupdate: ", spaced[-2])
        print("Outbound interface: ", spaced[-1])

    else:
        print("Protocol: ", codes_dict[''.join(spaced[-9])])
        print("Prefix: ", spaced[-8])
        print("nexthop: ", spaced[-2], spaced[-3])
        print("Outbound interface: ", spaced[-1])

    print ()
    print()
    n=n+1
