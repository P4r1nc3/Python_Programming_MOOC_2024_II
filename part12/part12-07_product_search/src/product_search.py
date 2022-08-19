# Write your solution here
def search(products: list, criterion: callable):
    return [product for product in products if criterion(product)]