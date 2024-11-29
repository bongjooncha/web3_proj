from web3 import Web3

provider_url = "https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4"
wallet_address = '0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE'

def problem4_uniswap_allow(provider_url, wallet_address):
    w3 = Web3(Web3.HTTPProvider(provider_url))
    uniswap_address = "0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD"

    usdc_smart_contract_address = '0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
    usdc_abi = [
        {
            "constant": True,
            "inputs": [
                {"name": "_owner", "type": "address"},
                {"name": "_spender", "type": "address"}
            ],
            "name": "allowance",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]
    usdc_contract = w3.eth.contract(address=w3.to_checksum_address(usdc_smart_contract_address), abi=usdc_abi)
    allowance_amount = usdc_contract.functions.allowance(w3.to_checksum_address(wallet_address), 
                                                         w3.to_checksum_address(uniswap_address)).call()
    print(allowance_amount)

problem4_uniswap_allow(provider_url,wallet_address)