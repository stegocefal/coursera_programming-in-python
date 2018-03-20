import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        _, file_ext = os.path.splitext(self.photo_file_name)
        # assert file_ext != '', 'Photo file name does not contain extension.'
        return file_ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        if body_whl:
            dimensions = tuple(map(float, body_whl.split(sep='x')))
        else:
            dimensions = (0, 0, 0)
        self.body_width, self.body_height, self.body_length = dimensions

    def get_body_volume(self):
        body_volume = self.body_width * self.body_height * self.body_length
        return body_volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        headers = next(reader)
        for row in reader:
            if len(row) != len(headers):
                continue

            car_dict = {headers[i]: row[i] for i in range(len(headers))}

            try:
                if car_dict['car_type'] == 'car':
                    car_dict['passenger_seats_count'] = int(
                        car_dict['passenger_seats_count'])
                car_dict['carrying'] = float(car_dict['carrying'])
            except ValueError:
                continue
            except KeyError:
                print('Invalid CSV file headers')
                raise

            if car_dict['car_type'] == 'car':
                car_list.append(Car(car_dict['brand'],
                                    car_dict['photo_file_name'],
                                    car_dict['carrying'],
                                    car_dict['passenger_seats_count']))
            elif car_dict['car_type'] == 'truck':
                car_list.append(Truck(car_dict['brand'],
                                      car_dict['photo_file_name'],
                                      car_dict['carrying'],
                                      car_dict['body_whl']))
            elif car_dict['car_type'] == 'spec_machine':
                car_list.append(SpecMachine(car_dict['brand'],
                                            car_dict['photo_file_name'],
                                            car_dict['carrying'],
                                            car_dict['extra']))
            else:
                continue

    return car_list
#
#
# if __name__ == '__main__':
#     print(get_car_list('coursera_week3_cars.csv'))
