from typing import TypeVar
import noise.noise as noise



seed = 0

def get_seed() -> int:
    return seed

def set_seed(value : int) -> None:
    global seed
    seed = value

'''
Seeded Noise functions
Combine game seed with given seed
'''

T = TypeVar('T')
# returns a random element from list
def choose(seed, list : list[T]) -> T:
    return list[recursive_hash(seed) % len(list)]

def mix_seed(seed) -> int:
    if isinstance(seed, tuple):
        return noise.hash_vector(get_seed(), seed)
    else:
        return noise.hash(get_seed(), seed)

# returns true or false based on successes to total odds
def odds(seed, successes, total) -> bool:
    return noise.odds(mix_seed(seed), successes, total)

# hashes together a seed and a position
def hash(pos) -> int:
    return noise.hash(get_seed(), pos)

# recursive hash function with any amount of inputs
def recursive_hash(*args) -> int:
    return noise.recursive_hash(get_seed(), *args)

# hashes vector using recursive hash
def hash_vector(vector) -> int:
    return recursive_hash(get_seed(), *vector)