
#CHEKS IF MASK IS VALID
def subnet_checker():
  subnet = input ("Enter subnet mask in decimal format: ")
  l = list(subnet)
  if l[0] == ('/') and (''.join(l[1:])).isdigit():
    global l_num
    l_num = int(''.join(l[1:]))
    if 0 <= l_num <= 32:
     binaryprint()
    else:
      print ("Subnet mask is invalid")
      subnet_checker()
  else:
    print ("Subnet mask is invalid")
    subnet_checker()
#CHECKS IF IP IS VALID
def ip_checker():
  ip_add = input ("Enter Ip address: ")
  check_list = ip_add.split('.')
  if len(check_list) == 4:
    global a, b, c, d
    a,b,c,d = ip_add.split('.')
    if a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit():
      if 0 <= int(a) < 256 and 0 <= int(b) < 256 and 0 <= int(c) < 256 and 0 <= int(d) < 256:
        subnet_checker()
      else:
        print("invalid IP address")
        ip_checker()
    else:
      print("invalid IP address")
      ip_checker()
  else:
    print("invalid IP address")
    ip_checker()
  
#PRINTS BINARY AND ADDRESSES
def binaryprint():
  to_join = [a, b, c, d]
  def binarization(to_join):
    ii = []
    for i in to_join:
      i0 =format(int(i), '08b')
      ii.append(i0)
    return ii
  binary_join = binarization(to_join)
  print ('{:>8}'.format((to_join)[0]), '{:>8}'.format((to_join)[1]), '{:>8}'.format((to_join)[2]), '{:>8}'.format((to_join)[3]))
  print (binary_join[0], binary_join[1], binary_join[2], binary_join[3])
  y=0
  z=8
  zeroadd = []
  bcast = []
  while y < 25:
    zeroadd_o = str(int(((''.join(((str(''.join(binary_join[0:]))[0:l_num]),(32-l_num)*'0')))[y:z]), 2))
    zeroadd.append(zeroadd_o)
    y=y+8 
    z=z+8
  v=0
  w=8
  while v < 25:
    bcast_o = str(int(((''.join(((str(''.join(binary_join[0:]))[0:l_num]),(32-l_num)*'1')))[v:w]), 2))
    bcast.append(bcast_o)
    v=v+8 
    w=w+8
  print ('network address is:', '.'.join(zeroadd))
  print ('broadcast address is:', '.'.join(bcast))
#RUNS EVERYTHING
ip_checker()