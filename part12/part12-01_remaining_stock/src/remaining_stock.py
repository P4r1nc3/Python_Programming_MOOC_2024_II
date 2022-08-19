# Write your solution here:
def sort_by_remaining_stock(items: list):
    def order_by_stock(item):
        return item[2]
    return sorted(items, key=order_by_stock)

if __name__ == '__main__':
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")