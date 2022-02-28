import csv
import os.path


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:

            self.body_whl = body_whl.split('x')
            if len(self.body_whl) == 3:
                self.body_whl = [float(x) for x in self.body_whl]
            else:
                raise Exception
        except:
            self.body_whl = [0, 0, 0]
        finally:
            self.body_whl = [float(x) for x in self.body_whl]
            self.body_length = self.body_whl[0]
            self.body_width = self.body_whl[1]
            self.body_height = self.body_whl[2]

    def get_body_volume(self):
        return self.body_whl[0] * self.body_whl[1] * self.body_whl[2]


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def check_cls(csvfile):
    car_list = []
    for row in csvfile:
        photo = os.path.splitext(str(row['photo_file_name']))

        if photo[1] in ['.jpg', '.jpeg', '.png', '.gif'] and len(photo) == 2:
            if row['car_type'] == 'car':
                if row['brand'] and row['photo_file_name'] \
                        and row['carrying'] and row['passenger_seats_count']:
                    x = Car(row['brand'], row['photo_file_name'],
                            row['carrying'], row['passenger_seats_count'])
                    x.car_type = 'car'
                    car_list.append(x)
            elif row['car_type'] == 'truck':
                if row['brand'] and row['photo_file_name'] and row['carrying']:
                    x = Truck(row['brand'], row['photo_file_name'],
                              row['carrying'], row['body_whl'])
                    x.car_type = 'truck'
                    car_list.append(x)
            elif row['car_type'] == 'spec_machine':
                if row['brand'] and row['photo_file_name'] and row['carrying'] and row['extra']:
                    x = SpecMachine(row['brand'], row['photo_file_name'], row['carrying'], row['extra'])
                    x.car_type = 'spec_machine'
                    car_list.append(x)

            else:
                continue
        else:
            continue

    return car_list


def get_car_list(namecsv):
    try:
        with open(namecsv, 'r') as file:
            csvfile = csv.DictReader(file, delimiter=";")
            return check_cls(csvfile)
    except:
        return []
