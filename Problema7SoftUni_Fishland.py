price_of_makerel = float(input())
price_of_sprats = float(input())
kilos_of_tuna = float(input())
kilos_of_scads = float(input())
kilos_of_mussels = int(input())

tuna_price = price_of_makerel + (0.6 * price_of_makerel)
scads_price = price_of_sprats + (0.8 * price_of_sprats)
mussels_price = 7.50

total_tuna_price = kilos_of_tuna * tuna_price
total_scads_price = kilos_of_scads * scads_price
total_mussels_price = kilos_of_mussels * mussels_price

bill = total_tuna_price + total_scads_price + total_mussels_price
print(f'{bill: .2f}')