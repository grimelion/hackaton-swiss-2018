import time
from boa.blockchain.vm.Neo.Runtime import Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Blockchain import GetBlock, GetHeight
from boa.blockchain.vm.Neo.TransactionType import InvocationTransaction
from boa.blockchain.vm.Neo.Transaction import *

from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete

VALID_ARGS = [
    closing_time, judge, case_id, court_id,
    complainant, defendant, complainant_lawyer, defendant_lawyer,
    complainant_witnesses, defendant_witnesses, attorney,
    category, case_type, custom_data, previos_block_height
]

def Main(operation, args):
    OWNER = b''
    if (not is_block_valid(args)):
        return False
    is_owner = CheckWitness(OWNER)
    if (is_owner && operation == 'init_court'):
        init_court(args)
        return True
    if (operation == 'create_case'):
        create_case(args)
        return True
    else if (operation == 'validate_change'):
        is_valid = is_update_valid()
        if (is_valid):
            update_case()
            return True
        else:
            return False
    else if (operation == 'close_case'):
        close_case(args)
        return True
    else:
        return False

def init_court(args):
    Put({'status': 'active'})
    return True

def create_case(**kwargs):
    case = new Case(args)
    pass

def is_update_valid(args):
    pass

def update_case(args):
    pass

def close_case(args):
    Put({args.case_id: {

    }})
    pass

def is_block_valid(args):
    for (arg in args):
        if (arg not in VALID_ARGS)
            return False
    return True
