import requests, time

def moon_math():
    print("Mantle — Moon Math Monitor (insane APR farming detection)")
    while True:
        r = requests.get("https://api.mantle.xyz/v1/pools")
        for pool in r.json().get("pools", []):
            apr = float(pool.get("apr", 0))
            tvl = float(pool.get("tvl", 0))
            if apr > 1000 and tvl > 100_000:  # >1000% APR + real money locked
                print(f"MOON MATH DISCOVERED 🌙⚡️\n"
                      f"Pool: {pool['name']}\n"
                      f"APR: {apr:,.1f}%  (!!!)\n"
                      f"TVL: ${tvl:,.0f}\n"
                      f"Token: {pool['token']}\n"
                      f"Link: https://mantle.xyz/pool/{pool['id']}\n"
                      f"→ Either the next 1000x... or complete illusion\n"
                      f"→ Yield farmers are already calculating their yachts\n"
                      f"{'🌕'*30}\n")
        time.sleep(15)

if __name__ == "__main__":
    moon_math()
