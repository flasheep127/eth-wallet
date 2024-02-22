import json
from web3 import Web3
from eth_account import Account
import time

def newAccount():
    privateKey = Account.create()._private_key.hex()
    print(f'''gening:{privateKey}''')
    address = Account.from_key(privateKey).address

    

    with open('private.txt', 'a') as file:

        file.write(privateKey + "\n")

    with open('pulic+private.txt', 'a') as file:

        file.write(address + ',' +  privateKey + "\n")


num = int(input('count:'))
for i in range(num):
    newAccount()

    time.sleep(0.0001)
