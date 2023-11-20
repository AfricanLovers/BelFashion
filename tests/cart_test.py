import unittest
from model.cart import Cart


class TestCart(unittest.TestCase):
    # Тест для проверки добавления одежды
    def test_add_clothes(self):
        cart = Cart()
        cart.add_clothes(1, 2)
        self.assertIn([1, 2], cart.get_clothes())

    # Тест для проверки удаления одежды
    def test_remove_clothes(self):
        cart = Cart()
        cart.add_clothes(1)
        cart.add_clothes(2)
        cart.remove_clothes(1)
        self.assertNotIn([1, 1], cart.get_clothes())

    # Тест для проверки обновления одежды
    def test_update_clothes(self):
        cart = Cart()
        cart.add_clothes(1)
        cart.update_clothes(1, 3)
        self.assertIn([1, 3], cart.get_clothes())

    # Тест для проверки очистки корзины
    def test_clear_cart(self):
        cart = Cart()
        cart.add_clothes(1)
        cart.clear_cart()
        self.assertEqual(cart.get_clothes(), [])

# Запуск тестов
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)