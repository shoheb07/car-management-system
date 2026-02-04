import json
import os

DATA_FILE = "cars.json"


def load_cars():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_cars(cars):
    with open(DATA_FILE, "w") as f:
        json.dump(cars, f, indent=4)


def add_car():
    cars = load_cars()
    car = {
        "id": input("Car ID: "),
        "brand": input("Brand: "),
        "model": input("Model: "),
        "year": input("Year: "),
        "price": input("Price: "),
        "status": input("Status (Available/Sold): ")
    }
    cars.append(car)
    save_cars(cars)
    print("Car added successfully.")


def view_cars():
    cars = load_cars()
    if not cars:
        print("No cars found.")
        return

    for car in cars:
        print("-" * 40)
        for key, value in car.items():
            print(f"{key.capitalize()}: {value}")


def search_car():
    cars = load_cars()
    car_id = input("Enter Car ID: ")
    for car in cars:
        if car["id"] == car_id:
            print(car)
            return
    print("Car not found.")


def update_car():
    cars = load_cars()
    car_id = input("Enter Car ID to update: ")

    for car in cars:
        if car["id"] == car_id:
            car["brand"] = input("New Brand: ")
            car["model"] = input("New Model: ")
            car["year"] = input("New Year: ")
            car["price"] = input("New Price: ")
            car["status"] = input("New Status: ")
            save_cars(cars)
            print("Car updated.")
            return

    print("Car not found.")


def delete_car():
    cars = load_cars()
    car_id = input("Enter Car ID to delete: ")

    cars = [car for car in cars if car["id"] != car_id]
    save_cars(cars)
    print("Car deleted.")
