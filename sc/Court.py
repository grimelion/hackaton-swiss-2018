from boa.blockchain.vm.Neo.Runtime import Notify, GetTrigger, CheckWitness, Log
from boa.blockchain.vm.Neo.Runtime import GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.blockchain.vm.Neo.TriggerType import Application, Verification

TOKEN_NAME = 'LOCALTOKEN'

def Name():
    return TOKEN_NAME

def Main(operation, args):
    trigger = GetTrigger()
    OWNER = b'6b1410519d09f00bde5121bab0b56a6c916095b2'
    
    if trigger == Verification():

        print("doing verification!")
        owner_len = len(OWNER)

        if owner_len == 20:
            res = CheckWitness(OWNER)
            print("owner verify result")
            return res

    elif trigger == Application():
        if operation == 'name':
            n = Name()
            return n
    return False
