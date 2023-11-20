from loader import db, default_image
import random

# Добавление пользователей
db.add_user("test1", "123456789")
db.add_user("test2", "1234", True)
db.add_user("1", "1", True)
db.add_user("car", "car")

# Добавление категорий одежды
db.add_category("Худи")
db.add_category("Джинсы")
db.add_category("Куртки")
db.add_category("Лонгсливы")
db.add_category("Свитера")
db.add_category("Футболки")


# Добавление одежды
db.add_clothes("ВЕЛЛСОФТ ХУДИ (GRACE)", "NIKA WEAR", 2023, "Уютная худи с названием Grace от NIKA WEAR", 5500, 1, ".\\images\\hudi1.jpg")
db.add_clothes("ХУДИ (WOLF)", "Gucci", 2021, "Стильная худи с волчьим принтом от Gucci", 7500, 1, ".\\images\\hudi2.jpg")
db.add_clothes("БРЮКИ-КАРГО ОВЕРСАЙЗ (SYMBIOSIS)", "Gucci", 2023, "Просторные брюки-карго с дизайном Symbiosis", 4000, 2, ".\\images\\jeens1.jpg")
db.add_clothes("ПОТЕРТЫЕ ДЖИНСЫ (IDOLS)", "NIKA WEAR", 2020, "Джинсы с потертостями от NIKA WEAR", 3500, 2, ".\\images\\jeens2.jpg")
db.add_clothes("УТЕПЛЕННАЯ КУРТКА (WEREWOLF 2)", "Levi's", 2019, "Утепленная куртка Werewolf 2 от Levi's", 8500, 3, ".\\images\\kurtka1.jpg")
db.add_clothes("УТЕПЛЕННАЯ КУРТКА (HARSH 10 - GREY)", "Gucci", 2021, "Утепленная куртка Harsh 10 в сером цвете", 7000, 3, ".\\images\\kurtka2.jpg")
db.add_clothes("ОВЕРСАЙЗ ЛОНГСЛИВ (SAKURA)", "NIKA WEAR", 2023, "Оверсайз лонгслив с дизайном Sakura", 3500, 4, ".\\images\\long1.jpg")
db.add_clothes("ОВЕРСАЙЗ ЛОНГСЛИВ (ETERNITY 2)", "NIKA WEAR", 2022, "Оверсайз лонгслив Eternity 2 от NIKA WEAR", 4500, 4, ".\\images\\long2.jpg")
db.add_clothes("ОВЕРСАЙЗ ЛОНГСЛИВ (WHITE BLOOD)", "Gucci", 2022, "Белый оверсайз лонгслив с дизайном White Blood", 2000, 4, ".\\images\\long3.jpg")
db.add_clothes("ОВЕРСАЙЗ ЛОНГСЛИВ (CULT IN MY SOUL)", "Adidas", 2021, "Оверсайз лонгслив с дизайном Cult In My Soul от Adidas", 3500, 4, ".\\images\\long4.jpg")
db.add_clothes("ОВЕРСАЙЗ ЛОНГСЛИВ (KILLUA GODSPEED REWORK)", "NIKA WEAR", 2023, "Оверсайз лонгслив с ремесленным дизайном Killua Godspeed Rework", 2500, 4, ".\\images\\long5.jpg")
db.add_clothes("ОВЕРСАЙЗ ЛОНГСЛИВ (ASAGIRI GEN)", "Gucci", 2022, "Оверсайз лонгслив Asagiri Gen от Gucci", 3000, 4, ".\\images\\long6.jpg")
db.add_clothes("ОВЕРСАЙЗ ЛОНГСЛИВ (CHAINSAW MECHANISM)", "Adidas", 2021, "Оверсайз лонгслив с дизайном Chainsaw Mechanism от Adidas", 2500, 4, ".\\images\\long7.jpg")
db.add_clothes("ВЯЗАННЫЙ СВИТЕР (LOST FOREST)", "Gucci", 2022, "Вязаный свитер с дизайном Lost Forest", 6000, 6, ".\\images\\sweater1.jpg")
db.add_clothes("ФУТБОЛКА ОВЕРСАЙЗ (2B)", "Adidas", 2021, "Оверсайз футболка с дизайном 2B от Adidas", 2500, 6, ".\\images\\t-shirt1.jpg")
db.add_clothes("ФУТБОЛКА ОВЕРСАЙЗ (ASKA LANGLEY SORI)", "NIKA WEAR", 2019, "Оверсайз футболка с дизайном Aska Langley Sory от NIKA WEAR", 2500, 6, ".\\images\\t-shirt2.jpg")
db.add_clothes("ФУТБОЛКА ОВЕРСАЙЗ (SHIDO)", "NIKA WEAR", 2022, "Оверсайз футболка с дизайном Shido от NIKA WEAR", 1500, 6, ".\\images\\t-shirt3.jpg")
db.add_clothes("ФУТБОЛКА ОВЕРСАЙЗ (FEITAN)", "Gucci", 2022, "Оверсайз футболка с дизайном Feitan от Gucci", 2000, 6, ".\\images\\t-shirt4.jpg")


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
