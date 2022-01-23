# Installation

```
pip install magiceden
```

# Usage

Find the slug of the NFT collection you're interested in by referencing the suffix of the collection URL.

Example: https://magiceden.io/marketplace/solana_monkey_business

```
from magiceden import MagicEdenScraper

client = MagicEdenScraper()

print(client.get_floor_price('solana_monkey_business'))
print(client.get_total_volume('solana_monkey_business'))
print(client.get_avg_price('solana_monkey_business'))
```