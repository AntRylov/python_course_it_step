
from dev import euro, dollar, gbr


def main(money: int, valuta: str):
    if valuta == "euro":
        print(euro(int(money)))
    if valuta == "dollar":
        print(dollar(int(money)))
    if valuta == "gbr":
        print(gbr(int(money)))


main(400, "euro")
