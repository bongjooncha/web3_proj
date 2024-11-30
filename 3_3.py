from solana.rpc.api import Client
from solana.publickey import PublicKey

# Solana 클러스터에 연결 (메인넷 베일러 기준)
solana_client = Client("https://api.devnet.solana.com")

# USDC의 Mint 주소 (Solana 메인넷 기준)
token_address = "wbUyCKSNwbeeEXoaMDCk4rNqKXeH36Nt9A1FBnQbiiB"

def get_usdc_total_supply(token_address):
    mint_pubkey = PublicKey(token_address)
    try:
        response = solana_client.get_token_supply(mint_pubkey)
        total_supply = int(response.value.amount) / 10**6
        print(f"실시간 mock USDC 총 발행량: {total_supply:,} mock USDC")
    except:
        print(response)

get_usdc_total_supply(token_address)