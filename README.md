## Arbitrum Grants Distributor  - STIP-Bridge
Distribution program pays out 50,000 ARB per week for 12 weeks based on veBAL voting for whitelisted pools on Arbitrum

Pools are capped at 20% of the total weekly $ARB by default.

$ARB to a pool is boosted by a dynamic boost (described below based on fees vs emissions), and a fixed boost that can be assigned by Balancer BD to support special initiatives.

The pools participating in the program, as well as configuration around overriding caps and fixed boost can be found [here](https://github.com/BalancerMaxis/arbitrum_grants_distributor/blob/main/automation/arbitrum_stip_bridge_start_q2_2024.py#L29).

Pools which are at least 50% interest bearing (LST) are eligible for whitelist addition.

---

## Configuration and Data
- [ARB amounts emitted](https://github.com/BalancerMaxis/arbitrum_grants_distributor/blob/main/automation/constants.py#L12)
- [Pool Whitelist and Modifiers](https://github.com/BalancerMaxis/arbitrum_grants_distributor/blob/main/automation/arbitrum_stip_bridge_start_q2_2024.py)
- [Output Data](https://github.com/BalancerMaxis/arbitrum_grants_distributor/tree/main/output) is collected in output/ directory
- [BAL Emissions per year](https://github.com/BalancerMaxis/arbitrum_grants_distributor/blob/main/automation/emissions_per_year.py)

---

## How boost is calculated

Boost is based on 2 factors.

1. A fixed boost granted to incentive important initiatives
2. A variable boost based on the efficiency of the pool (fees/emissions)

### Fixed boost
By default, all whitelisted pools have a fixed boost of 1.  Here are some examples of situations where fixed boost might be assigned and what it could be:

| Desired Outcome/Activity                               | Fixed Boost |
|--------------------------------------------------------|-------------|
| 100% Intrest Bearing                                   | 1.5x        |
| IB token Mintable on Arbitrum                          | 1.75x       |
| Short term boost for a shared/major marketing campaign | 2x          |

#### 100% Intrest Bearing    
- 100% of the liqudity in this pool is interest bearing
- Get this by pairing your token with something like wstETH, sDAI, or sFRAX (or another partner LST)
- 
#### IB Token Mintable on Arbitrum
- To encourage a more native LST environemnt on Arbitrum.  We are open to considering and granting boost to projects that enable native minting/burning of their LST on Arbi.

#### Short term boost for a shared/major marketing campaign
- Sometimes the best way to grow a pool is fast, with lots of incentives and marketing push.
- In cases where it's all comming together like that and we have a partner looking to also hit it hard, we may consider a short term but high boost or some fixed incentives to help kick things off.


### Variable Fee Based Boost (1-3x)
The variable boost is determined by using the following formula:

`Variable Boost = min(Fees Earned / (USD Value of BAL emitted + 1), 3)`

The variable boosted is capped at 3 and has a minimum of 1.  

The fee based boost is added to the fixed boost, so:

Total Boost = **_Fixed Boost + Variable Boost - 1_** 

where both boosts are >=1 it will be automatically computed by the model and applied. 
