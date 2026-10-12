"""Discount"""
def calculate_total_and_discount(items):
    """Sums the total items before discount"""
    total = sum(item.price_cents * item.qty for item in items)

    # 10% discount applied if total is above 5000
    if total > 5000:
        total = int(total * 0.9)

    return total

def apply_discount_to_cart(cart):
    """Returns the total with the discount"""
    return calculate_total_and_discount(cart.items)


def generate_invoice(order):
    """Generating invoice for the order"""
    # Format invoice header and customer info
    invoice = f"Invoice for order {order.id}\nCustomer: {order.user_email}\n"

    # Calculate total price of items in the order
    total = calculate_total_and_discount(order.items)

    invoice += f"Total (after discount if applicable): {total} cents"
    return invoice
