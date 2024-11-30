from solana.keypair import Keypair
from base58 import b58decode
from solana.rpc.api import Client
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID

private_key_b58 = "2gLvCiKBCf8gy2HJY9MmkesfBt7GkWf9g1L9dTzTXhkMifGoS2MebWbi4FBjPmBAKcnWDDqG9baMaays68JWKSbR "

def problem1_sol_balance_check(private_key):
    private_key_bytes = b58decode(private_key)
    public_address = Keypair.from_secret_key(private_key_bytes).public_key
    print(public_address)

    client = Client("https://api.devnet.solana.com")
    
    wallet_address = PublicKey(public_address)
    response = client.get_token_accounts_by_owner(wallet_address)
    print(response)

problem1_sol_balance_check(private_key_b58)