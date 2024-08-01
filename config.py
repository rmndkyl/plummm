from web3 import Web3

# Configuration file for setting delays between modules and wallets

# RPC settings
RPC = 'https://testnet-rpc.plumenetwork.xyz/http'
web3 = Web3(Web3.HTTPProvider(RPC))

# Gas settings
gas_limit = 2000000
gas_price = web3.to_wei(1, 'gwei')

# Delay between modules in seconds (minimum and maximum)
module_delay_min = 10
module_delay_max = 120

# Delay between using different wallets in seconds (minimum and maximum)
wallet_delay_min = 10
wallet_delay_max = 120

# Retry settings for failed transactions
retry_attempts = 5
retry_delay = 10

# Module route configuration
# Available modules:
# "faucet" - Faucet module
# "swap" - Swap module
# "stake" - Staking module
# "check_in" - Check-in module
# "prediction" - Prediction module
# "rwa": - RWA module
# Example:
# STRICT_ORDER_MODULES = [
#     ("faucet", 1),       # Runs the faucet module once
#     ("swap", 1),         # Runs the swap module once
#     ("stake", 1)         # Runs the staking module once
# ]
# RANDOM_ORDER_MODULES = [
#     ("check_in", 1),     # Runs the check-in module once
#     ("prediction", 1),   # Runs the prediction module once
#     ("rwa", 2)           # Runs the RWA module twice
# ]

STRICT_ORDER_MODULES = [
    ("faucet", 1),
    ("swap", 1),
    ("stake", 1)
]

RANDOM_ORDER_MODULES = [
    ("check_in", 1),
    ("prediction", 1),
    ("rwa", 1)
]