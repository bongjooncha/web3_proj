from web3 import Web3

provider_url = "https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4"
w3 = Web3(Web3.HTTPProvider(provider_url))

def problem3_get_usdc_supply():
    usdc_address = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
    usdc_abi = [
        {
            "constant": True,
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]

    usdc_contract = w3.eth.contract(address=usdc_address, abi=usdc_abi)
    total_supply = usdc_contract.functions.totalSupply().call()
    print(f'이더리움 네트워크내 발행된 USDC: {total_supply:,} 개')

problem3_get_usdc_supply()