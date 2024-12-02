from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.rpc.types import TokenAccountOpts
from base58 import b58decode
from solana.keypair import Keypair


private_key_b58 = "2gLvCiKBCf8gy2HJY9MmkesfBt7GkWf9g1L9dTzTXhkMifGoS2MebWbi4FBjPmBAKcnWDDqG9baMaays68JWKSbR"
# 퍼블릭 키 변환시 FaPTEkPkBR7hrSQ12i4Z6XcC7u4YDY8vZM5rmJD3zdNw


def get_token(private_key):
    private_key_bytes = b58decode(private_key)
    public_address = Keypair.from_secret_key(private_key_bytes).public_key
    client = Client("https://api.devnet.solana.com")
    public_address = PublicKey(public_address)
    usdc_mint_address = PublicKey("wbUyCKSNwbeeEXoaMDCk4rNqKXeH36Nt9A1FBnQbiiB")
    token_accounts_resp = client.get_token_accounts_by_owner_json_parsed(public_address, TokenAccountOpts(mint=usdc_mint_address))
    token_account_info  = token_accounts_resp.value[0].account.data.parsed['info']['tokenAmount']
    token_amount=int(token_account_info['amount'])/(10**token_account_info['decimals'])
    print(f"mock USDC의 보유량: {token_amount:.8f}")
    

get_token(private_key_b58)