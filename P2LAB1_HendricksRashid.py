
gas_cost = float (input())

mileage = float (input())

per_mile = mileage / gas_cost

twenty_mile = per_mile * 20

seventy_five_mile = per_mile * 75

five_hundred_mile = per_mile * 500

print(f'{twenty_mile:.2f} {seventy_five_mile:.2f} {five_hundred_mile:.2f}')