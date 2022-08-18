# WRITE YOUR SOLUTION HERE:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration

def products_in_shopping_list(shopping_list: ShoppingList, amount: int):
    return [product[0] for product in shopping_list if product[1]>=amount]
    
if __name__ == "__main__":
    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("alcohol free beer", 24)
    my_list.add("pineapple", 1)

    print("the shopping list contains at least 8 of the following items:")
    for product in products_in_shopping_list(my_list, 8):
        print(product)