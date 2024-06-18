from bal_tools import Aura
import json
import os
import copy
from datetime import datetime
from decimal import Decimal, ROUND_DOWN
from typing import Dict
from .constants import FILE_PREFIX


def get_root_dir() -> str:
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def generate_and_save_aura_transaction(
    tokens_gauge_distributions: Dict,
    start_date: datetime,
    end_date: datetime,
    chain_name: str,
) -> Dict:
    """
    Take a set of distributions and send them to aura direct
    """
    aura = Aura(chain_name)
    # Dump into output.json using:
    with open(f"{get_root_dir()}/data/aura_direct_stream.json") as f:
        output_data = json.load(f)
    # Find transaction with func name `setRecipientList` and dump gauge
    gauge_distributions = tokens_gauge_distributions.values()
    tx_template = output_data["transactions"][1]

    tx_list = []
    total_amount = 0
    # Inject list of gauges addresses:
    ## TODO for special week redeuced from 1 period to 2 and divided amount over 2 for aurasplit
    for gauge in gauge_distributions:
        aura_pid = aura.aura_pids_by_address.get(gauge["recipientGaugeAddr"])
        if not aura_pid:
            print(
                f"WARNING: No aura pid found for gauge {gauge['recipientGaugeAddr']}, using gauge address in payload instead for easy debugging."
            )
            aura_pid = gauge["recipientGaugeAddr"]
        tx = copy.deepcopy(tx_template)
        tx["contractInputsValues"]["_pid"] = aura_pid
        amount = Decimal(gauge["distribution"]) * Decimal(1e18)
        amount = amount.to_integral_value(rounding=ROUND_DOWN)
        tx["contractInputsValues"]["_amount"] = str(int(amount / 2))
        tx["contractInputsValues"][
            "_periods"
        ] = "1"  ## 2 weeks TODO was chagned to 1 for aura split
        tx_list.append(tx)
        total_amount += amount

    # Add approve tx
    approve_tx = output_data["transactions"][0]
    approve_tx["contractInputsValues"]["amount"] = str(total_amount)
    tx_list.insert(0, approve_tx)
    output_data["transactions"] = tx_list
    with open(
        f"{get_root_dir()}/output/{FILE_PREFIX}_{start_date.date()}_{end_date.date()}_aura_direct_stream.json",
        "w",
    ) as _f:
        json.dump(output_data, _f, indent=4)
    print(f"{total_amount}({int(total_amount)/1e18}) $ARB approved for aura direct")
    return output_data
