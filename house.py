from priceList import bigBazar as bigBazarPriceList

print(bigBazarPriceList)

def bed():
    return "This is bed"


def people():
    return [
        {
            "name": "Ahmad",
            "age": "19.6"
        },
        {
            "name": "Ahmad",
            "age": "19.6"
        },
        {
            "name": "Ahmad",
            "age": "19.6"
        },
    ]

oranges = "this is oranges"

class Car:
    wheels = 4
    def __init__(self, owner, price) -> None:
        self.owner = owner
        self.price = price
    
    def howMuch(self) -> None:
        print(self.price)


class Mandi:
    potato = 22
    tomato = 33

    def __init__(self, title, city, priceList) -> None:
        self.title = title
        self.city = city
        self.priceList = priceList

    def calcPrice(self, items):
        for item in items:
            print(self.priceList[item["name"]])
        print(self.priceList['potato'])
        print(items)

ferrari = Car('Ahmad', "$23322")

bigBazar = Mandi('Big Bazar', 'Gorakhpur', bigBazarPriceList)

bigBazar.calcPrice([
    {
        "name":"potato",
        "quantity":4
    }
])