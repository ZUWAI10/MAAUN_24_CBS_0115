from models import FuelDispenser, CarWash
fuel1 = FuelDispenser("Pump 1", 500, 1.5)
fuel2 = FuelDispenser("Pump 2", 300, 1.6)

wash1 = CarWash("Wash Station", 40, 8)
assets = [fuel1, fuel2, wash1]
total_revenue = 0
for asset in assets:
    revenue = asset.calculate_revenue()
    print(asset.name, "Revenue:", revenue)
    total_revenue += revenue
 print("Total Station Revenue:", total_revenue)
from models import FuelDispenser, CarWash

fuel1 = FuelDispenser("Pump 1", 500, 1.5)
fuel2 = FuelDispenser("Pump 2", 300, 1.6)

wash1 = CarWash("Wash Station", 40, 8)

assets = [fuel1, fuel2, wash1]

total_revenue = 0

for asset in assets:
    revenue = asset.calculate_revenue()
    print(asset.name, "Revenue:", revenue)
    total_revenue += revenue

print("Total Station Revenue:", total_revenue)
   