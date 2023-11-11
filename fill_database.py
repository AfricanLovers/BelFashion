from loader import db, default_image
import random

# Добавление пользователей
db.add_user("test1", "123456789")
db.add_user("test2", "1234", True)
db.add_user("1", "1", True)
db.add_user("car", "car")

# Добавление категорий одежды
db.add_category("Футболки")
db.add_category("Джинсы")
db.add_category("Куртки")
# Добавьте другие категории по необходимости

# Добавление одежды
# Примеры
db.add_clothes("Футболка с принтом", "Adidas", 2021, "Стильная футболка с уникальным дизайном", 1500, 1, default_image)
db.add_clothes("Классические джинсы", "Levi's", 2020, "Удобные синие джинсы, подходят для повседневной носки", 2500, 2, default_image)
db.add_clothes("Кожаная куртка", "Gucci", 2022, "Элегантная кожаная куртка для прохладной погоды", 8000, 3, default_image)
# Добавьте другие предметы одежды по необходимости

def add_sample_orders(num_orders=30):
    users = db.get_all_users()
    if not users:
        print("No users in the database!")
        return

    addresses = ["Main St.", "Elm St.", "Park Ave.", "Broadway", "5th Ave."]
    emails = ["example@example.com", "test@test.com", "user@domain.com"]
    phone_numbers = ["+73917387324", "+375298684719", "+184727352832"]
    payment_types = [0, 1]

    clothes = db.get_all_clothes()
    if not clothes:
        print("No clothes in the database!")
        return

    for _ in range(num_orders):
        user_id = random.choice(users)[0]
        price = round(random.uniform(500, 10000), 2)
        address = random.choice(addresses)
        email = random.choice(emails)
        phone = random.choice(phone_numbers)
        payment_type = random.choice(payment_types)

        order_id = db.add_order(user_id, price, address, email, phone, payment_type)

        for _ in range(random.randint(1, 5)):
            cloth = random.choice(clothes)
            cloth_id = cloth[0]
            quantity = random.randint(1, 5)
            db.add_order_item(order_id, cloth_id, quantity)

add_sample_orders()
