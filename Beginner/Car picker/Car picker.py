import random


cars= input("Enter names of cars separated by commas and a space: ")

list_of_cars=cars.split(", ")
# print(list_of_cars)

random_car=random.choice(list_of_cars)
print(f"You should selecte {random_car} ")


