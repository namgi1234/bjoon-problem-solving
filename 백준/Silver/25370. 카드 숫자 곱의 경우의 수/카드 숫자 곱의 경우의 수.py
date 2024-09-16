import itertools

def find_possible_products(n):
    # Possible numbers on the cards
    cards = range(1, 10)
    
    # Use a set to store unique products
    products = set()
    
    # Iterate over all possible combinations of n cards
    for combination in itertools.product(cards, repeat=n):
        # Compute the product of the current combination
        product_value = 1
        for number in combination:
            product_value *= number
        # Add the product to the set
        products.add(product_value)
    
    # Return the number of unique products
    return len(products)

# Reading input
n = int(input().strip())

# Compute the number of unique products
result = find_possible_products(n)

# Print the result
print(result)
