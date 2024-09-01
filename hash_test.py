# Programmed by chatGpt

# ismert hibák: villog a kijelzés

import hashlib

# Adathalmaz definiálása
data = [0.978, 1.028, 0.984, 0.974, 0.956, 1.017, 0.983, 0.981, 1.044, 1.009, 1.015, 0.973, 1.035, 1.032]

# Az adathalmaz konvertálása string formátumba, hogy hash-elhető legyen
data_string = ",".join(str(x) for x in data)

# Változók inicializálása
previous_hash = ""
hash_count = 0

# Végtelen ciklus a hash generálásához és összehasonlításhoz
while True:
    # Hash generálása (SHA-256 algoritmus használatával)
    current_hash = hashlib.sha256(data_string.encode()).hexdigest()
    hash_count += 1

    # Kiírás ugyanabba a sorba
    print(f"\rGenerálások száma: {hash_count}", end="", flush=True)

    # Ha az előző hash nem üres (tehát már történt egy hash generálás), ellenőrizzük, hogy eltérőek-e
    if previous_hash and current_hash != previous_hash:
        print(f"\nA hash értékek eltérnek. A generálások száma: {hash_count}")
        break  # Kilépés a ciklusból

    # Az előző hash érték frissítése az új hash értékkel
    previous_hash = current_hash
