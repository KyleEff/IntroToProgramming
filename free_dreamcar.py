
numCars = int(input('How many dream cars would you like to own? '))
carMakeModel = [[''] * numCars, [''] * numCars]
carPrices = [0] * numCars


cars = ['Ford Mustang', 'Chevrolet Camaro 1-LE', 'Chevrolet Camaro SS',
        'Ford Mustang GT', 'Mazda MX-5', 'Dodge Challenger', 'Dodge Charger',
        'Fiat Spider']
prices = [34000, 37000, 48000, 47000, 31000, 49000, 46000, 35000]
# arrayName.split


def main():
    auto_pop()
#   populate()
    display()


def populate():
    for info in range(numCars):
        print('Car', info+1)
        carMakeModel[0][info] = input('Enter make: ')
        carMakeModel[1][info] = input('Enter model: ')
        carPrices[info] = int(input('Enter price: $'))


def auto_pop():
    ''' Automatic array population '''
    for info in range(numCars):
        make_model = cars[info].split()
        make = make_model[0]
        model = make_model[1:]
        carMakeModel[0][info] = make
        if len(model) > 1:
            carMakeModel[1][info] = make_model[1] + ' ' + make_model[2]
        else:
            carMakeModel[1][info] = model[0]
        carPrices[info] = prices[info]


def display():
    print(f"\n{'Car Make':^10}|{'Car Model':^11}|{'Price':^10}\n"
          f"----------+-----------+----------")
    for content in range(numCars):
        print(f"{carMakeModel[0][content]:^10}|"
              f"{carMakeModel[1][content]:^11}| $"
              f"{carPrices[content]:<8,}")

    max_price = carPrices.index(max(carPrices))
    min_price = carPrices.index(min(carPrices))
    print(f"\nHighest Priced Car: {carMakeModel[0][max_price]} {carMakeModel[1][max_price]}\n"
          f"Lowest Priced Car: {carMakeModel[0][min_price]} {carMakeModel[1][min_price]}")


main()























