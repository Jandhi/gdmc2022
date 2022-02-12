def sum_vectors(*vectors):
    return tuple(map(sum, zip(*vectors)))

def product(vector):
    value = 1
    for num in vector:
        value *= num
    return value

def product_vectors(*vectors):
    return tuple(map(product, zip(*vectors)))

def multiply_vector(vector, num):
    return tuple(map(lambda x : x * num, vector))