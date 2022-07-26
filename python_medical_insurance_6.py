names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Create for loop
total_cost = 0

for insurance_cost in actual_insurance_costs:
  total_cost += insurance_cost
  average_cost = total_cost / len(actual_insurance_costs)

print("Average insurance cost: " + str(average_cost) + " dollars.")

# Determine how insurance cost compares to avg
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
# Check if insurance cost is above avg
  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is above average.")
  # Check if insurance cost is below avg
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is below average.")
  # Check if insurance cost is equal to avg
  else:
    print("The insurance cost for " + name + " is equal to the average.")

# Use list comprehension to update costs
updated_estimated_costs = [estimated_cost * 11/10 for estimated_cost in estimated_insurance_costs]
print(updated_estimated_costs)
