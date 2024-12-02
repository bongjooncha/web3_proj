from web3 import Web3

# 이벤트 시그니처
event_signature = "Liquidate(bytes32,address,address,uint256,uint256,uint256,uint256,uint256)"

# Keccak-256 해시 계산
event_hash = Web3.keccak(text=event_signature).hex()
print(event_hash)
