from web3 import Web3

wallet_private_key = "0x49e5e33e2817b2ec595d2136ac0ada6f8d1aebaebca73136218dce34c656448b"
provider_url = "https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4"

web3 = Web3()
wallet_address = web3.eth.account.from_key(wallet_private_key).address
print(wallet_address)

def problem1_get_eth_balance(wallet_address, provider_url):
    web3 = Web3(Web3.HTTPProvider(provider_url))
    balance_wei = web3.eth.get_balance(wallet_address)
    balance_eth = web3.from_wei(balance_wei, 'ether')
    print(f"ETH 잔고: {balance_eth} ETH")



eth_balance = problem1_get_eth_balance(wallet_address, provider_url)
