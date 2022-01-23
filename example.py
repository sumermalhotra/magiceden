from magiceden import MagicEdenScraper

client = MagicEdenScraper()

print(client.get_floor_price('solana_monkey_business'))
print(client.get_total_volume('solana_monkey_business'))
print(client.get_avg_price('solana_monkey_business'))