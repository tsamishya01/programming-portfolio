import math

def get_valid_price(pizza_number):
    """
    Prompts the user for a valid pizza price.
    Repeats until a positive numeric value is entered.
    """
    while True:
        try:
            price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
            if price <= 0:
                print("Please enter a valid price!")
            else:
                return price
        except ValueError:
            print("Please enter a valid price!")


def calculate_total_and_discount(prices):
    """
    Applies the 4-for-3 offer and calculates:
    - Final total
    - Discount percentage (rounded up)
    """
    original_total = sum(prices)
    cheapest_pizza = min(prices)
    discounted_total = original_total - cheapest_pizza

    discount_percentage = math.ceil(
        (cheapest_pizza / original_total) * 100
    )

    return discounted_total, discount_percentage


def main():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================\n")

    prices = []

    for i in range(1, 5):
        price = get_valid_price(i)
        prices.append(price)

    total, discount = calculate_total_and_discount(prices)

    print(
        f"\nOrder Total is £{total:.2f}, "
        f"a fabulous discount of {discount}%!"
    )


main()
