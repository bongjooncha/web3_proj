from web3 import Web3

# 이더리움 layer 내 토큰만 계산 가능
provider_url = 'https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4'
contract_address = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'    #<- usdc contract address
address = '0x1c7D4B196Cb0C7B01d743Fbc6116a902379C7238'      #<- wallet address
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