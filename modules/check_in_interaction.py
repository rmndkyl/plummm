import config

web3=config.web3

# Information about the proxy contract and the implementation contract
PROXY_CONTRACT_ADDRESS = '0x8Dc5b3f1CcC75604710d9F464e3C5D2dfCAb60d8'
IMPLEMENTATION_CONTRACT_ADDRESS = '0x2a205aA43fDF7Fe25A14D1777b0F770A1A34950B'
PROXY_ABI = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "_data",
                "type": "bytes"
            }
        ],
        "stateMutability": "payable",
        "type": "constructor"
    },
    {
        "stateMutability": "payable",
        "type": "fallback"
    }
]
IMPLEMENTATION_ABI = [
    {
        "inputs": [],
        "name": "checkIn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

def check_in(private_key):
    proxy_contract = web3.eth.contract(address=PROXY_CONTRACT_ADDRESS, abi=PROXY_ABI)
    implementation_contract = web3.eth.contract(address=IMPLEMENTATION_CONTRACT_ADDRESS, abi=IMPLEMENTATION_ABI)
    account = web3.eth.account.from_key(private_key)
    
    # Data for Calling the checkIn Function of the Implementation Contract
    check_in_data = implementation_contract.encodeABI(fn_name="checkIn")
    
    tx = {
        'to': PROXY_CONTRACT_ADDRESS,
        'from': account.address,
        'nonce': web3.eth.get_transaction_count(account.address),
        'data': check_in_data,
        'gas': config.gas_limit,
        'gasPrice': config.gas_price
    }
    
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    
    return receipt
