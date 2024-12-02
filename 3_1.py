from solana.keypair import Keypair
from base58 import b58decode
from solana.rpc.api import Client
from solana.publickey import PublicKey

private_key_b58 = "2gLvCiKBCf8gy2HJY9MmkesfBt7GkWf9g1L9dTzTXhkMifGoS2MebWbi4FBjPmBAKcnWDDqG9baMaays68JWKSbR"
# 퍼블릭 키 변환시 FaPTEkPkBR7hrSQ12i4Z6XcC7u4YDY8vZM5rmJD3zdNw

def problem1_sol_balance_check(private_key):
    private_key_bytes = b58decode(private_key)
    public_address = Keypair.from_secret_key(private_key_bytes).public_key

    client = Client("https://api.devnet.solana.com")

    wallet_address = PublicKey(public_address)
    balance = client.get_balance(wallet_address)
    print(f"지갑의 솔라나 잔액: {balance.value / 1_000_000_000} SOL")

problem1_sol_balance_check(private_key_b58)