from __future__ import annotations
import csv
import pprint
from model import Pokemon,Human
def load_pokemons() -> list[Pokemon]:
    with open('pokemon.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        pokemon_list = []
        for row in reader:
            try:
                p =Pokemon(name=row["ポケモン"],weight=float(row["おもさ(kg)"]) ,height=float(row["たかさ(m)"]))
                pokemon_list.append(p)
            except ValueError:#数値以外の値が入ってる可能性がある
                pass
    return pokemon_list

if __name__ == "__main__":
    load_pokemons()