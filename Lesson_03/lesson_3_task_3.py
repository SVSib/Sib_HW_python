from address import Address
from mailing import Mailing

to_address = Address(676659, "Новосибирск", "Южная", 47, 33)
from_address = Address(435677, "Белово", "Отменная", 11, 3)

mailing = Mailing(to_address, from_address, 1500, 56883335566)
print(mailing)
