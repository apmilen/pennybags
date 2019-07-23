from decimal import Decimal


def get_amount_plus_fee(amount):
    stripe_fixed_comission = Decimal(0.30)
    total_paid = (amount+stripe_fixed_comission)/Decimal(1-0.029)
    total_paid = total_paid
    return total_paid
