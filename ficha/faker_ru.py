from faker import Faker



faker_ru = Faker('ru_RU')
print(faker_ru.name())
print(faker_ru.name_male())
print(faker_ru.address())
print(faker_ru.email())
print(faker_ru.job())
print(faker_ru.text())
print(faker_ru.ipv4())
print(faker_ru.city())
print(faker_ru.credit_card_full())
print(faker_ru.phone_number())


# print(dir(faker_ru))

