## Description

This script allows interaction with various smart contracts on the blockchain, performing actions such as:
- Requesting tokens from a faucet (faucet)
- Swapping tokens (swap)
- Staking tokens (stake)
- Check-in (check-in)
- Interacting with a prediction market (prediction)
- Creating NFT tokens (RWA)

## Requirements

- Python 3.10+
- The following Python packages:
  - web3==6.2.0
  - pandas==1.5.3
  - numpy==1.26.4
  - requests==2.31.1
  - openpyxl==3.0.10

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rmndkyl/plummm.git
    cd plummm
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Account Data**:
   - Prepare a file `accounts_data.xlsx` with your private keys and proxies. The script will read this file to obtain the necessary keys and proxy addresses.


  | Private Key                      | Proxy Address                      |
  |----------------------------------|------------------------------------|
  | YourPrivateKey1                  | username:password@proxyserver:port |
  | YourPrivateKey2                  | username:password@proxyserver:port |


2. **Configuring config.py**
   
  - Fill in the `config.py` file with the following parameters:

    - `module_delay_min`: minimum delay between module executions (in seconds)
    - `module_delay_max`: maximum delay between module executions (in seconds)
    - `wallet_delay_min`: minimum delay between wallets (in seconds)
    - `wallet_delay_max`: maximum delay between wallets (in seconds)
    - `gas_limit`: gas limit for transactions
    - `gas_price`: gas price for transactions
    - `STRICT_ORDER_MODULES`: list of modules to be executed in a strict order
    - `RANDOM_ORDER_MODULES`: list of modules to be executed in a random order

## Usage

Run the script and follow the menu instructions to select the module you want to execute.

# Credited By Layer Airdrop
[Telegram Channel](https://t.me/layerairdrop)

[Telegram Group](https://t.me/layerairdropdiskusi)
