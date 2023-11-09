from faker import Faker

fake = Faker()
mail = str(fake.email())
name = str(fake.name())
password = str(fake.password())
