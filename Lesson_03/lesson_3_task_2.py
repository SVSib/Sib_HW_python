from smartphone import Smartphone

catalog = [
    Smartphone("honor", "X6", "+79998882345"),
    Smartphone("iphone", "10", "+79998882512"),
    Smartphone("xiaomi", "redmi note 10 plus", "+799988833182"),
    Smartphone("sony", "xperia 5", "+79998889643"),
    Smartphone("ZTE", "blade 6", "+79998812252")
    ]

for Smartphone in catalog:
    print(f"{Smartphone.stamp} - {Smartphone.model}, {Smartphone.number}")
