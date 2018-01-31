access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed VLANs: {}']


def inputprompt():
    global interface_mode
    interface_mode = input('Enter interface mode (access/trunk): ')
    after_int_mode()


def after_int_mode():
    if interface_mode == 'access':
        int_name = input('Enter interface type and number: ')

        def accvlan():
            acc_vlan = input('Enter VLAN number: ')
            if acc_vlan.isdigit() != True:
              print('Invalid VLAN number. Try again.')
              accvlan()
            else:
                print('Interface {}'.format(int_name))
                n = 1
                while n < 5:
                    print((access_template[n]).format(acc_vlan))
                    n = n + 1

        accvlan()
    elif interface_mode == 'trunk':
        allowed = input('Enter allowed VLANs, one by one, separated with comma: ')
        #COMMA REQUEST IS ADDED TO VALIDATE IF THERE ARE DIGITS
        allowed_vlans = allowed.split(',')
        allowed_vlans_spaced = allowed.split(', ')
        if (''.join(allowed_vlans[0:])).isdigit() or (''.join(allowed_vlans_spaced[0:])).isdigit():
            m = 0
            while m < 3:
                print((trunk_template[m]).format(allowed))
                m = m + 1
        else:
            print("incorrect vlan value")
            after_int_mode()
    else:
        print("Enter valid interface mode")
        inputprompt()


inputprompt()









