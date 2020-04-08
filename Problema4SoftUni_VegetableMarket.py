price_of_killos_fruits = float(input())
price_of_killos_vegetables = float(input())
total_killos_fruits = int(input())
total_killos_vegetables = int(input())
price_from_fruits = price_of_killos_fruits * total_killos_fruits
price_from_vegetables = price_of_killos_vegetables * total_killos_vegetables
income = (price_from_fruits + price_from_vegetables) * 0.89

print(f'{income: .2f}')