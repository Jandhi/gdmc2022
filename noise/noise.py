BITNOISE1 = 0x85297a4d
BITNOISE2 = 0x68e31da4
BITNOISE3 = 0x1859c4e9
BITNOISE4 = 0x0c1fc20b

# returns true or false based on successes to total odds
def odds(seed, successes, total) -> bool:
    return hash(BITNOISE4, seed) % total < successes

# test function for above
def test_odds(seed, trials, successes, total):
    success_counter = 0

    for trial in range(trials):
        trial_seed = hash(seed, trial)
        if odds(trial_seed, successes, total):
            success_counter += 1

    expected_percent = (successes * 100.0) / total
    trial_percent = (success_counter * 100.0) / trials
    print("Expected odds: %", expected_percent)
    print("True odds: %", trial_percent)

# recursive hash function with any amount of inputs
def recursive_hash(seed, *args) -> int:
    noise = seed

    for pos in args:
        noise = hash(noise, pos)

    return noise

# hashes vector using recursive hash
def hash_vector(seed, vector) -> int:
    return recursive_hash(seed, *vector)

# hashes together a seed and a position
def hash(seed, pos) -> int:
    noise = pos
    noise = noise * BITNOISE1
    noise = noise + seed
    noise = noise ^ (noise >> 8)
    noise = noise + BITNOISE2
    noise = noise ^ (noise << 8)
    noise = noise * BITNOISE3
    noise = noise ^ (noise >> 8)
    return noise

# tests the above
def test_hash(seed, trials, base):
    counter = [base * [0]]

    for pos in range(trials):
        noise = hash(seed, pos)
        counter[noise % base] += 1

    for number in range(base):
        val = counter[number]
        percent = (val * 100.0) / trials
        print(number, ": %", percent)  