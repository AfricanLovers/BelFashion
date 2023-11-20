import pytest
from database.database import UserDatabase, CategoryDatabase, ClothesDatabase, OrderDatabase


@pytest.fixture(scope="module")
def user_db():
    db = UserDatabase(":memory:")
    yield db
    db.db.close()


def test_add_user(user_db):
    user_db.add_user("testuser", "password")
    assert user_db.user_in_db("testuser")


def test_get_user(user_db):
    user_db.add_user("getuser", "password")
    user = user_db.get_user("getuser")
    assert user and user[1] == "getuser"


def test_get_all_users(user_db):
    user_db.add_user("user1", "password1")
    user_db.add_user("user2", "password2")
    users = user_db.get_all_users()
    assert len(users) >= 2


def test_get_user_by_id(user_db):
    user_db.add_user("user_by_id", "password")
    user = user_db.get_user("user_by_id")
    user_by_id = user_db.get_user_by_id(user[0])
    assert user_by_id == user


def test_check_user(user_db):
    user_db.add_user("checkuser", "checkpass")
    assert user_db.check_user("checkuser", "checkpass")


def test_fail_check_user_wrong_password(user_db):
    user_db.add_user("failuser", "realpass")
    assert not user_db.check_user("failuser", "wrongpass")


@pytest.fixture(scope="module")
def category_db():
    db = CategoryDatabase(":memory:")
    yield db
    db.db.close()


def test_add_category(category_db):
    category_db.add_category("Test Category")
    assert category_db.get_category_id("Test Category") is not None


def test_get_category_name(category_db):
    category_db.add_category("New Category")
    category_id = category_db.get_category_id("New Category")
    assert category_db.get_category_name(category_id) == "New Category"


def test_get_all_categories(category_db):
    category_db.add_category("Category 1")
    category_db.add_category("Category 2")
    categories = category_db.get_all_categories()
    assert len(categories) >= 2


@pytest.fixture(scope="module")
def clothes_db():
    db = ClothesDatabase(":memory:")
    yield db
    db.db.close()


def test_add_clothes(clothes_db):
    clothes_db.add_clothes("T-Shirt", "Test Brand", 2021, "Description", 29.99, 1)
    assert clothes_db.get_clothes_by_name("T-Shirt") is not None


def test_get_clothes_by_id(clothes_db):
    clothes_db.add_clothes("Jeans", "Brand A", 2022, "Blue Jeans", 59.99, 1)
    clothes = clothes_db.get_clothes_by_name("Jeans")
    clothes_by_id = clothes_db.get_clothes_by_id(clothes[0])
    assert clothes_by_id == clothes


def test_get_all_clothes(clothes_db):
    clothes_db.add_clothes("Jacket", "Brand B", 2021, "Leather Jacket", 99.99, 2)
    all_clothes = clothes_db.get_all_clothes()
    assert len(all_clothes) >= 2


def test_search_clothes_name(clothes_db):
    clothes_db.add_clothes("Sweater", "Brand C", 2023, "Wool Sweater", 39.99, 1)
    search_result = clothes_db.search_clothes_name("Sweater")
    assert len(search_result) >= 1


@pytest.fixture(scope="module")
def order_db():
    db = OrderDatabase(":memory:")
    yield db
    db.db.close()


if __name__ == "__main__":
    pytest.main()