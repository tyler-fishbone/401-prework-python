def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
	if city == "Charlotte":
 		return 183
	elif city == "Tampa":
		return 220
	elif city == "Pittsburgh":
		return 222
	elif city == "Los Angeles":
		return 475
  
def rental_car_cost(days):
  total = days * 40
  if days >= 7:
  	total -= 50
  elif days >= 3:
    total -= 20
  return total

def trip_cost(city, days, spending_money):
  total = hotel_cost(days - 1) + rental_car_cost(days) + plane_ride_cost(city) + spending_money
  return total

print trip_cost("Los Angeles", 5, 600)