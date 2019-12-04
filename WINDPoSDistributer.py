

import requests
import json
import windpy as pw
import time



seedy = "SEED"
myAddress = pw.Address(seed=seedy)


while 1:
    
    time.sleep(86400)
    
    leasing_addr = ".........................."
    ceo_addr = ".............................."
    node = "http://144.91.84.27:6869"

    r = requests.get(node +"/leasing/active/" + leasing_addr)
    r = r.text
    r = json.loads(r)


    leasing_addr_balance =(json.loads((requests.get(node +"/addresses/balance/" + (leasing_addr))).text))['balance']
    


    block_height = json.loads((requests.get(node+"/blocks/height")).text)['height']
    


    if leasing_addr_balance >= 500000000:
        sender = []
        amount = []
        height = []
        n = 0
        t_amount = 0
        for i in r:
            heightt = i['height']
            if block_height - heightt > 1000:
                sender =sender + [i['sender']]
                amount =amount + [i['amount']]
                height =height + [i['height']]
                t_amount = t_amount + i['amount']
                n = n + 1
        transfer_total_fee = 100000 * (n+1)
        
        transfer_amount = ((leasing_addr_balance - transfer_total_fee) * 0.95)
        
        ceo_amount = leasing_addr_balance - transfer_amount
        
        for j in range(n):
            
            print(sender[j], ((amount[j] / t_amount)* transfer_amount))
            myAddress.sendWind(recipient = pw.Address(sender[j]), amount = int(((amount[j] / t_amount)* transfer_amount)))
            
        print(ceo_addr, ceo_amount - transfer_total_fee)       
        myAddress.sendWind(recipient = pw.Address(ceo_addr), amount =int(ceo_amount - transfer_total_fee))




