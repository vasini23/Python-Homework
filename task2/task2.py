import re
commands_file = open('commands.txt','r')
list = commands_file.read()
good_commands = re.findall(r'switchport trunk allowed vlan .*', list)
vlans = re.findall(r'\d+\w', str(good_commands))
vlans = [int(i) for i in vlans]

vlans_sorted = sorted(vlans)

common_list = []
unique_list = []

for i in range(0, len(vlans_sorted)):
    m = re.findall((str(vlans_sorted[i])), str((vlans_sorted)))
    if len(m) == 1:
        unique_list.append(vlans_sorted[i])
    else:
        common_list.append(vlans_sorted[i])

common_list = set(common_list)

print("common vlans:", common_list)
print("unique vlans:", unique_list)













