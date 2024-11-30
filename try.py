from web3 import Web3

# 이더리움 네트워크에 연결 (예: Infura 사용)
infura_url = 'https://mainnet.infura.io/v3/b0123c9ee0d74f2e98a99831cbc90ce4'
web3 = Web3(Web3.HTTPProvider(infura_url))

# UMA 스마트 계약 주소 및 ABI
uma_contract_address = '0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828'
uma_abi = '[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'

# UMA 계약 인스턴스 생성
uma_contract = web3.eth.contract(address=uma_contract_address, abi=uma_abi)

# 조회할 주소
address = '0x95513B21C07e410E38DAF3635bD357115Cc8E168'

# UMA 잔액 조회
balance = uma_contract.functions.balanceOf(address).call()

# UMA는 소수점 18자리까지 있으므로, 이를 반영하여 출력
uma_balance = balance / (10 ** 18)
print(f"UMA Balance: {uma_balance}")