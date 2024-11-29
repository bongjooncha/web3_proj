from web3 import Web3

wallet_private_key = "0x49e5e33e2817b2ec595d2136ac0ada6f8d1aebaebca73136218dce34c656448b"
provider_url = "https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4"

web3 = Web3()
wallet_address = web3.eth.account.from_key(wallet_private_key).address

def problem2_calculate_usdc_balance(wallet_address, provider_url):
    web3 = Web3(Web3.HTTPProvider(provider_url))
    contract_address = "0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238"
    usdc_abi = [{
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }]
    usdc_contract = web3.eth.contract(address=web3.to_checksum_address(contract_address), abi=usdc_abi)
    usdc_balance = usdc_contract.functions.balanceOf(web3.to_checksum_address(wallet_address)).call()
    print(usdc_balance)


eth_balance = problem2_calculate_usdc_balance(wallet_address, provider_url)