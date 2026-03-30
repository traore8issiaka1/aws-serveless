import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Paramètres
NB_LIGNES = 50000
DATE_DEBUT = datetime(2024, 1, 1)
DATE_FIN = datetime(2024, 3, 31)

# Données de référence Afrique
PAYS = ['Senegal', 'CotedIvoire', 'Mali', 'Guinee', 'Burkina Faso', 'Togo', 'Benin', 'Niger', 'Cameroun', 'Gabon']
OPERATEURS = ['Orange', 'HTN', 'Noov', 'Wave', 'Free']
TYPE_EVENEMENT = ['CALL', 'SMS', 'DATA', 'MOMO']
STATUTS = ['SUCCESS', 'FAILED']

# Fonction pour générer MSISDN
def generate_msisdn(pays):
    prefixes = {
        'Senegal': '221',
        'CotedIvoire': '225',
        'Mali': '223',
        'Guinee': '224',
        'Burkina Faso': '226'
    }
    prefix = prefixes.get(pays, '220')
    return f'+{prefix}{random.randint(70000000, 79999999)}'

# Fonction principale pour générer une ligne
def generate_row():
    pays = random.choice(PAYS)
    operateur = random.choice(OPERATEURS)
    type_evt = random.choice(TYPE_EVENEMENT)

    # Date aléatoire entre DATE_DEBUT et DATE_FIN
    delta = DATE_FIN - DATE_DEBUT
    date_heure = DATE_DEBUT + timedelta(
        seconds=random.randint(0, int(delta.total_seconds()))
    )

    # Valeurs selon le type d'événement
    if type_evt == 'CALL':
        duree = random.randint(5, 600)
        volume_mb = 0
        montant = round(random.uniform(10, 500), 2)
    elif type_evt == 'SMS':
        duree = 0
        volume_mb = 0
        montant = round(random.uniform(5, 50), 2)
    elif type_evt == 'DATA':
        duree = 0
        volume_mb = round(random.uniform(1, 1000), 2)
        montant = round(volume_mb * random.uniform(0.1, 0.5), 2)
    else:  # MOMO
        duree = 0
        volume_mb = 0
        montant = round(random.uniform(100, 10000), 2)

    statut = random.choices(STATUTS, weights=[89.92, 10.08])[0]
    antenne = f'ANT-{pays[:3].upper()}-{random.randint(1, 500):03d}'

    return {
        'msisdn': generate_msisdn(pays),
        'date_heure': date_heure.strftime('%Y-%m-%d %H:%M:%S'),
        'pays': pays,
        'operateur': operateur,
        'type_evenement': type_evt,
        'duree_secondes': duree,
        'volume_mb': volume_mb,
        'montant_xof': montant,
        'statut': statut,
        'antenne_id': antenne,
    }

# Génération des données
print(f'Génération de {NB_LIGNES} lignes...')
rows = [generate_row() for _ in range(NB_LIGNES)]
df = pd.DataFrame(rows)

# Sauvegarde
os.makedirs('data', exist_ok=True)
output_file = 'data/telecom_data_2024.csv'
df.to_csv(output_file, index=False)

print(f'Fichier sauvegardé: {output_file}')
print(f'Taille: {os.path.getsize(output_file) / 1024 / 1024:.1f} MB')
print(f'Colonnes: {list(df.columns)}')
print(df.head(3))