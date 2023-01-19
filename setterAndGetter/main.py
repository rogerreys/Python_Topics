from car import Car

def run():
    car = Car("toyota", "s3 ultra")
    car.color = 'blanco'
    print(car.color)


if __name__ == '__main__':
    run()