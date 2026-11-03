from menu import get_price

def order_total(items):
    return sum(get_price(i) for i in items)

if __name__ == "__main__":
    print(order_total(["latte", "espresso"]))
#TODO: add tax calculation
# TODO: Add discount codes
def total_with_tax(items, rate=0.08):
    return round(order_total(items) * (1 + rate), 2)
    
def loyalty_points(total):
# work in progress, not finished
    return int(total)
