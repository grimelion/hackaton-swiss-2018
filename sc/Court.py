import time
import os
from boa.blockchain.vm.Neo.Runtime import Notify, GetTrigger, CheckWitness, Log
from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Blockchain import GetBlock, GetHeight
from boa.blockchain.vm.Neo.TransactionType import InvocationTransaction
from boa.blockchain.vm.Neo.Transaction import *

from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Output import GetScriptHash, GetValue, GetAssetId
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete

from neo.SmartContract.ContractParameterType import ContractParameterType

VALID_ARGS = [
    closing_time, judge, case_id, court_id,
    complainant, defendant, complainant_lawyer, defendant_lawyer,
    complainant_witnesses, defendant_witnesses, attorney,
    category, case_type, custom_data, previos_block_height
]

def Main(operation, args):
    args = json.loads(args)
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
        update_case()
        return True
    else if (operation == 'close_case'):
        close_case(args)
        return True
    else:
        return False

def init_court(args):
    Put({os.urandom(32):{'status': 'active'}})

def create_case(case_dict):
    Put({case_dict['case_id']: case_dict})

def update_case(case_dict):
    Put({case_dict['case_id']: case_dict})

def close_case(case_dict):
    case_dict['status'] = 'closed'
    Put({case_dict['case_id']: case_dict}})

def is_block_valid(args):
    for (arg in args):
        if (arg not in VALID_ARGS)
            return False
    return True
