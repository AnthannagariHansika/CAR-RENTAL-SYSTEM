class Car: 
 def __init__(self, car_id, brand, model, rent_per_day, available=True):

 self.car_id = car_id

 self.brand = brand

 self.model = model

 self.rent_per_day = rent_per_day

 self.available = available

 def __str__(self):

 status = "Available" if self.available else "Rented"

 return f"{self.car_id}: {self.brand} {self.model} - ${self.rent_per_day}/day -

{status}"

class CarRentalSystem:

 def __init__(self):

 self.cars = []

 def add_car(self, car):

 self.cars.append(car)

 def view_cars(self):

 print("\nAvailable Cars:")

 for car in self.cars:

 print(car)

 def rent_car(self, car_id, days):

 for car in self.cars:

if car.car_id == car_id and car.available:

 car.available = False

 total_cost = car.rent_per_day * days

 print(f"\n{car.brand} {car.model} has been rented for {days} days.") return

 print("Car not available or invalid ID.")

 def return_car(self, car_id):

 for car in self.cars:

 if car.car_id == car_id and not car.available:

 car.available = True

 print(f"\n{car.brand} {car.model} has been returned.")

 return

 print("Invalid ID or car is not currently rented.")

# Main

def main():

 system = CarRentalSystem()

 # Add some sample cars

 system.add_car(Car(1, "Toyota", "Camry", 50))

 system.add_car(Car(2, "Honda", "Civic", 45))

 system.add_car(Car(3, "Tesla", "Model 3", 100))

 while True:

 print("\n--- Car Rental System ---")

 print("1. View Cars")

 print("2. Rent a Car")

 print("3. Return a Car")

 print("4. Exit")

 choice = input("Enter your choice: ")

 if choice == "1":

 system.view_cars()

 elif choice == "2":

 try:

 car_id = int(input("Enter Car ID to rent: "))

7 days = int(input("Enter number of days: "))

 system.rent_car(car_id, days)

 except ValueError:

print("Invalid input. Please enter numeric values.")

 elif choice == "3":

 try:

 car_id = int(input("Enter Car ID to return: "))

 system.return_car(car_id)

 except ValueError:

 print("Invalid input. Please enter numeric values.")

 elif choice == "4":

 print("Thank you for using the Car Rental System.")

 break

 else: 
 print("Invali
d choice. Please try again.")

if __name__ == "__main__": 
 main()
Readme file
