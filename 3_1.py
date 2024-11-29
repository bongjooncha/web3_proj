from solana.keypair import Keypair
from base58 import b58decode

# Base58로 인코딩된 비공개 키
private_key_b58 = "2gLvCiKBCf8gy2HJY9MmkesfBt7GkWf9g1L9dTzTXhkMifGoS2MebWbi4FBjPmBAKcnWDDqG9baMaays68JWKSbR"

# 비공개 키를 바이트 배열로 변환
private_key_bytes = b58decode(private_key_b58)

# 키페어 생성
keypair = Keypair.from_string(private_key_b58)

# 공개 주소 출력
public_address = keypair.public_key
print(public_address)

from solana.rpc.api import Client

# 솔라나 클라이언트 초기화
client = Client("https://api.mainnet-beta.solana.com")

# 지갑 주소 입력
wallet_address = public_address

# 잔액 조회
balance = client.get_balance(wallet_address)

# 잔액 출력
print(f"지갑의 솔라나 잔액: {balance.value / 1_000_000_0000} SOL")