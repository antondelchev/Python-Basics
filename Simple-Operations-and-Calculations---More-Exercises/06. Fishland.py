price_skumriq_kg = float(input())
price_caca_kg = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

price_palamud_kg = price_skumriq_kg + price_skumriq_kg * 0.6
price_safrid_kg = price_caca_kg + price_caca_kg * 0.8
price_midi_kg = kg_midi * 7.5

total_price = price_palamud_kg * kg_palamud + price_safrid_kg * kg_safrid + price_midi_kg

print(f"{total_price:.2f}")
