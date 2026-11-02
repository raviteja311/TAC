from menu import get_price

def order_total(items):
    return sum(get_price(i) for i in items)

if __name__ == "__main__":
    print(order_total(["latte", "espresso"]))
#TODO: add tax calculation
