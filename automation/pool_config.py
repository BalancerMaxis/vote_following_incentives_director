from web3 import Web3
from automation.constants import (
    FIXED_INCENTIVE_TOKENS_PER_EPOCH,
    DESIRED_DEFAULT_VOTE_CAP,
)

#####
# Notes for the maintainers of this config file
#####
# Default cap was set to 10% when this comment was written, will be used if not overridden. (see constants.py)
# Default fixedBoost is 1 if not specified
# Default fixexEmissions is 0 if not specified
# All fixedEmissions should equal up to under constants.py/FIXED_INCENTIVE_TOKENS_PER_EPOCH

# meta information is not required to run, and you can put whatever you want there in json format as notes.
# gauge

#  THIS CONFIG IS FOR OPTIMISM CHAIN
ACTIVE_POOLS_AND_OVERRIDES = [
    {
        "pool_id": "0x4fd63966879300cafafbb35d157dc5229278ed2300020000000000000000002b",
        "meta": {"symbol": "weth-rETG", "boostReason": "OG"},
        "fixedBoost": 1.5,
        "capOverride": 20,
        "fixedEmissions": 3_000,
    },
    {
        "pool_id": "0x5f8893506ddc4c271837187d14a9c87964a074dc000000000000000000000106",
        "meta": "sfrax 3-pool",
    },
    {
        "pool_id": "0x7ca75bdea9dede97f8b13c6641b768650cb837820002000000000000000000d5",
        "meta": "wstETH eCLP",
    },
    {
        "pool_id": "0x004700ba0a4f5f22e1e78a277fca55e36f47e09c000000000000000000000104",
        "meta": "ankreth/reth",
    },
    {
        "pool_id": "0xa71021492a3966eec735ed1b505afa097c7cfe6f00000000000000000000010d",
        "meta": "sfrxETH",
    },
    {
        "pool_id": "0xe906d4c4fc4c3fe96560de86b4bf7ed89af9a69a000200000000000000000126",
        "meta": "sfrax",
    },
    {"pool_id": ""},
]


# assert that the total sum of all fixedEmissions is equal to FIXED_INCENTIVE_TOKENS_PER_EPOCH
total_fixed_emissions = sum(
    [x.get("fixedEmissions", 0) for x in ACTIVE_POOLS_AND_OVERRIDES]
)
assert (
    total_fixed_emissions == FIXED_INCENTIVE_TOKENS_PER_EPOCH
), f"Sum of fixed emissions configured:{total_fixed_emissions} does not equal FIXED_INCENTIVE_TOKENS_PER_EPOCH:{FIXED_INCENTIVE_TOKENS_PER_EPOCH} configured in constants.py"

# Load static boost data
boost_data = {}
cap_override_data = {}
fixed_emissions_per_pool = {}
# Load static boost here
for pooldata in ACTIVE_POOLS_AND_OVERRIDES:
    pool_id_lower = pooldata["pool_id"].lower()
    boost_data[pool_id_lower] = pooldata.get("fixedBoost", 1)
    cap_override_data[pool_id_lower] = pooldata.get(
        "capOverride", DESIRED_DEFAULT_VOTE_CAP
    )
    fixed_emissions_per_pool[pool_id_lower] = pooldata.get("fixedEmissions", 0)
