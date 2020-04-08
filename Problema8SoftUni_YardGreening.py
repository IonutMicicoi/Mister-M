square_meter = float(input())
price_per_square_meter = 7.61
total_price = square_meter * price_per_square_meter
discount = ((18 / 100) * total_price)
total_with_discount = total_price - discount
print(f'The final price is: {total_with_discount: .2f} dollars')
print(f'The discount is: {discount: .2f} dollars')