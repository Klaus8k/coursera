import csv
import os.path

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        print(self.photo_file_name)
        # просто показывает что есть метод в базовом классе. Но не выполняется!




class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl

    # Добавить метод подсчета объема

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


def check(dict):
    pass



car_list = []

with open('1.csv', 'r') as file:
    csvfile = csv.DictReader(file, delimiter = ";")
    for row in csvfile:
        if row['car_type'] == 'car':
            if row['brand'] and row['photo_file_name'] and row['carrying'] and row['passenger_seats_count']:
                x = Car(row['brand'], row['photo_file_name'], row['carrying'],row['passenger_seats_count'])
        elif row['car_type'] == 'truck':
            if row['brand'] and row['photo_file_name'] and row['carrying'] and row['body_whl']:
                x = Truck(row['brand'], row['photo_file_name'], row['carrying'],row['body_whl'])

                                
        else: continue

        car_list.append(x)

print([x.__dict__ for x in car_list])
