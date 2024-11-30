# from web3 import Web3

# def calculate_token_balance(wallet_address, token_contract_address, provider_url):
#     web3 = Web3(Web3.HTTPProvider(provider_url))
#     token_abi = [{
#         "constant": True,
#         "inputs": [{"name": "_owner", "type": "address"}],
#         "name": "balanceOf",
#         "outputs": [{"name": "balance", "type": "uint256"}],
#         "payable": False,
#         "stateMutability": "view",
#         "type": "function"
#     }]
#     token_contract = web3.eth.contract(address=web3.to_checksum_address(token_contract_address), abi=token_abi)
#     token_balance = token_contract.functions.balanceOf(web3.to_checksum_address(wallet_address)).call()
#     return token_balance

# wallet_address = "0x663DC15D3C1aC63ff12E45Ab68FeA3F0a883C251"
# usdc_contract_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
# provider_url = "https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4"

# usdc_balance = calculate_token_balance(wallet_address, usdc_contract_address, provider_url)
# print(f'지갑의 USDC 잔고: {usdc_balance}')

from web3 import Web3

provider_url = 'https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4'
contract_address = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'    #<- 이건 usdc contract address
address = '0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238'
wallet_address = Web3.to_checksum_address(address)

def problem2_get_contract_token_base(provider_url, contract_address, wallet_address):
    web3 = Web3(Web3.HTTPProvider(provider_url))

    # 토큰 수 구하기(소수점 고려x)
    balance_abi = [{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf",
                    "outputs":[{"name":"balance","type":"uint256"}],
                    "payable":False,"stateMutability":"view","type":"function"}]
    balance_contract = web3.eth.contract(address=contract_address, abi=balance_abi)
    balance = balance_contract.functions.balanceOf(wallet_address).call()
    
    # 토큰의 소수점
    decimal_abi = [{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],
                    "payable":False,"stateMutability":"view","type":"function"}]
    decimal_contract = web3.eth.contract(address=contract_address, abi=decimal_abi)
    decimals = decimal_contract.functions.decimals().call()

    token_balance = balance / (10 ** decimals)
    print(f"Token Balance: {token_balance:,}")

problem2_get_contract_token_base(provider_url, contract_address, wallet_address)