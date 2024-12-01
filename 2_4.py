from web3 import Web3

provider_url = "https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4"
wallet_address = '0xb84755de0d9ccf0e5b1f27354ed4888ed0cec5a8'

def problem4_uniswap_allow(provider_url, wallet_address):
    w3 = Web3(Web3.HTTPProvider(provider_url))
    uniswap_address = "0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD" # 문제에 해당하는 uniswap: universal router
    # uniswap_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D" #<- uniswap v2:router2

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
            "stateMutability": "view",
            "type": "function"
        }
    ]
    usdc_contract = w3.eth.contract(address=w3.to_checksum_address(usdc_smart_contract_address), abi=usdc_abi)
    allowance_amount = usdc_contract.functions.allowance(w3.to_checksum_address(wallet_address), 
                                                         w3.to_checksum_address(uniswap_address)).call()/1e6
    print(f"허용된 토큰 수량: {allowance_amount}")

problem4_uniswap_allow(provider_url,wallet_address)