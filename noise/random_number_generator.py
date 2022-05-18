from noise.random import get_seed
from noise.noise import hash
from threading import Lock

# deterministic random number generator with state, built to be thread safe
# I'd recommend sticking to random.py when we can, but this is an alternative
class RandomNumberGenerator:
    def __init__(self, initial_seed = get_seed()) -> None:
        self.__seed = initial_seed
        self.lock = Lock()
    
    def rand_int(self, min : int = 0, max : int = None) -> int:
        self.lock.acquire() # for thread safety
        num = hash(self.get_seed(), 0)
        self.lock.release()

        if max:
            return min + num % (max - min)
        else:
            return min + num 
    
    def get_seed(self) -> int:
        seed = self.__seed
        self.update_seed()
        return seed
    
    def update_seed(self) -> None:
        self.__seed = hash(self.__seed, self.__seed)