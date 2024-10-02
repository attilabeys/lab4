import json
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
      """)
with open('json/sampledata.json') as t:
    data = json.load(t)


print("Interface")
print("=" * 80)
print("{:<50}{:<20}{:<8}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in data["imdata"]:
    attributes = interface["l1PhysIf"]["attributes"]  
    dn = attributes["dn"]  
    description = attributes["descr"] 
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "inherit")
    print("{:<50}{:<20}{:<8}{:<6}".format(dn, description, speed, mtu))