
def ground_shipping_cost(weight):
  if weight <= 2.00:
   return 1.50*(weight)+20.00
  elif weight >2.00 and weight<= 6.00:
   return 3.00*(weight)+20.00
  elif weight >6.00 and weight <= 10.00:
   return 4.00*(weight)+20.00
  else:
   return 4.74*(weight)+20.00

print(ground_shipping_cost(8.4))

premium= 125.00


def cost_drone_shipping(weight):
  if weight <= 2.00:
    return 4.50*(weight)
  elif weight >2.00 and weight <=6.00:
    return 9.00*(weight)
  elif weight >6.00 and weight <=10.00:
    return 12*(weight)
  else:
    return 14.24*(weight)

print(cost_drone_shipping (1.5))

def cheapest_option(weight):

  ground= ground_shipping_cost(weight)
  premium= 125.00
  drone= cost_drone_shipping(weight)

  if ground < premium and ground < drone:
    return "Ground shipping for $"+ str(ground) + " is the lowest price offered by Sal's Shipping."
  elif  premium < ground and premium < drone:
    return "Premium Ground Shipping for $"+ str(premium) + " is the lowest price offered by Sal's Shipping."
  else:
    return "Drone shipping for $"+ str(drone)+ " is the lowest price offered by Sal's Shipping."
  
print(cheapest_option(4.8))




  
