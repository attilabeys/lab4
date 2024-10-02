import json 
 
print(""" 
Interface Status 
================================================================================ 
DN                                                 Description           Speed    MTU 
-------------------------------------------------- --------------------  ------  ------ 
""" 
) 
 
import json

with open('sample-data.json') as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<8}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', 'inherit')
    print("{:<50}{:<20}{:<8}{:<6}".format(dn, description, speed, mtu))