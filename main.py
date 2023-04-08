from __future__ import annotations
from  scipy.spatial import KDTree
from  matplotlib import pyplot as plt
from model import Pokemon,Human
from parse import load_pokemons
    
def find_nearest_neighbor(poke_list:list[Pokemon],target:Human) -> Pokemon:
    chood = [(p.weight,p.height) for p in poke_list]
    target_point = (target.weight,target.height)
    tree = KDTree(chood)
    disatance , indexes  = tree.query(target_point,k=5)
    return [poke_list[i] for i in indexes]

#init
pokemons:list[Pokemon] = load_pokemons()

weights = [pokemon.weight for pokemon in pokemons]
heights = [pokemon.height for pokemon in pokemons]

target_point:Human = Human(weight=54,height=1.73)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.scatter(weights, heights, s=10)

nn_pokes:list[Pokemon] = find_nearest_neighbor(poke_list=pokemons,target=target_point)
for nn_poke in nn_pokes:
    print(nn_poke.name)
    print(nn_poke.height)
    print(nn_poke.weight)
    ax.scatter(nn_poke.weight,nn_poke.height,c="r",s=10)



ax.scatter(target_point.weight,target_point.height,c="g",s=10)

ax.set_xlabel("Weight")
ax.set_ylabel("Height")
ax.set_title("Weight and Height of 100 pokemons")
ax.grid(True)
ax.set_aspect('equal')
ax.set_xlim([0, 100])
ax.set_ylim([0, 25])

plt.savefig("test.png", dpi=1200)