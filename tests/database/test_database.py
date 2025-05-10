import pytest
import sqlite3
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
   db = Database()
   db.test_connection()
   
@pytest.mark.database
def test_check_all_users():
   db = Database()
   users = db.get_all_users()

   print(users)


@pytest.mark.database
def test_check_user_sergii():
   db = Database()
   user = db.get_user_address_by_name ('Sergii')

   assert user[0][0] == 'Maydan Nezalezhnosti 1'
   assert user[0][1] == 'Kyiv'
   assert user[0][2] =='3127'
   assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
   db = Database()
   db.update_product_qnt_by_id(1, 25)
   water_qnt = db.select_product_qnt_by_id(1)

   assert water_qnt[0][0] == 25
   
@pytest.mark.database
def test_product_insert():
   db = Database()
   db.insert_product(4, 'печиво', 'солодке', 30)
   water_qnt = db.select_product_qnt_by_id(4)

   assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
   db = Database()
   db.insert_product(99, 'тестові' , 'дані', 999)
   db.delete_product_by_id(99)
   qnt = db.select_product_qnt_by_id(99)

   assert len(qnt) == 0 
   
@pytest.mark.database
def test_detailed_orders():
   db = Database()
   orders = db.get_detailed_orders()
   print("Замовлення", orders)
   assert len(orders) == 1 

   assert orders[0][0] == 1
   assert orders[0][1] =='Sergii'
   assert orders[0][2] =='солодка вода'
   assert orders[0][3] =='з цукром'
   
@pytest.mark.database
def test_insert_invalid_data_type():
    db = Database()
    with pytest.raises(sqlite3.InterfaceError):
        db.insert_product("нечисло", "назва", "опис", "не_число")

@pytest.mark.database
def test_insert_null_into_required_field():
    db = Database()
    with pytest.raises(sqlite3.IntegrityError):
        db.cursor.execute("INSERT INTO products (id, name, description, quantity) VALUES (?, ?, ?, ?)", (100, None, "тест", 10))
        db.connection.commit()

@pytest.mark.database
def test_duplicate_primary_key():
    db = Database()
    db.insert_product(200, "оригінал", "перший запис", 10)
    db.insert_product(200, "дубль", "другий запис", 20)  # REPLACE працює, тому тут не буде помилки
    qnt = db.select_product_qnt_by_id(200)
    assert qnt == 20

@pytest.mark.database
def test_sql_injection_protection():
    db = Database()
    result = db.get_user_address_by_name("' OR 1=1; --")
    assert result is None  # або відповідно до валідації

@pytest.mark.database
def test_large_text_insert():
    db = Database()
    long_description = "x" * 5000
    db.insert_product(201, "великий", long_description, 1)
    db.cursor.execute("SELECT description FROM products WHERE id = 201")
    result = db.cursor.fetchone()
    assert result[0] == long_description

@pytest.mark.database
def test_empty_product_name():
    db = Database()
    db.insert_product(202, "", "пусте ім'я", 5)
    db.cursor.execute("SELECT name FROM products WHERE id = 202")
    result = db.cursor.fetchone()
    assert result[0] == ""

@pytest.mark.database
def test_insert_negative_quantity():
    db = Database()
    db.insert_product(203, "мінус товар", "від'ємна кількість", -5)
    qnt = db.select_product_qnt_by_id(203)
    assert qnt == -5  # якщо не перевіряється на рівні БД

@pytest.mark.database
def test_country_code_format():
    db = Database()
    db.cursor.execute("UPDATE customers SET country = ? WHERE name = ?", ("UA", "Sergii"))
    db.connection.commit()
    result = db.get_user_address_by_name("Sergii")
    assert result[3] == "UA"

@pytest.mark.database
def test_update_and_verify_multiple_fields():
    db = Database()
    db.insert_product(204, "оновлення", "початковий", 3)
    db.insert_product(204, "оновлення", "зміна", 10)
    qnt = db.select_product_qnt_by_id(204)
    assert qnt == 10

@pytest.mark.database
def test_delete_non_existing_product():
    db = Database()
    db.delete_product_by_id(9999)
    qnt = db.select_product_qnt_by_id(9999)
    assert qnt is None     