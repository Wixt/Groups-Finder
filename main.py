import requests
import random
import threading
min=2000000
max=10000000
banner=("""\n\n
____    __    ____  __  ___   ___ .___________.
\   \  /  \  /   / |  | \  \ /  / |           |
 \   \/    \/   /  |  |  \  V  /  `---|  |----`
  \            /   |  |   >   <       |  |     
   \    /\    /    |  |  /  .  \      |  |     
    \__/  \__/     |__| /__/ \__\     |__|     
                                               
\n""")
print(banner)
webhook=input("Webhook URL >> ")
def find():
    id=random.randint(min,max)
    q=requests.get(f"https://groups.roblox.com/v1/groups/{id}")
    e=q.json()
    if q.status_code==200 and e['owner'] == None and e['publicEntryAllowed'] == True:
        dc=requests.post(webhook,data={"content": "https://www.roblox.com/groups/"+id})
    elif q.status_code == 429:
        exit()
    else:
        pass
while True:
    a=threading.Thread(target=find)
    a.start()
