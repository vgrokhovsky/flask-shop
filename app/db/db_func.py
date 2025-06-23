from .models import User,Category,Product,Order,OrderItem,Cartitem,Wishlist
from . import db_object as db 


def create_user(username, email, password):
    """Создать нового пользователя"""
    user = User(
            username=username,
            email=email,
            password=password,
        )
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_id(user_id):
    """Получить пользователя по ID"""
    return User.query.get(user_id)

def get_user(email):
    return User.query.filter_by(email=email).first()

def get_user_by_email(email):
    """Получить пользователя по email"""
    return User.query.filter_by(email=email).first()



def create_category(name, description):
    """Создать новую категорию"""
    category = Category(name=name, description=description)
    db.session.add(category)
    db.session.commit()
    return category

def get_category_by_id(category_id):
    """Получить категорию по ID"""
    return Category.query.get(category_id)

def get_all_categories():
    """Получить все категории"""
    return Category.query.all()



def add_product(name, price, description, stock, image_path, user_id, category_id):
    """Создать новый продукт"""
    product = Product(
        name=name,
        price=price,
        description=description,
        stock=stock,
        image_path=image_path,
        user_id=user_id,
        category_id=category_id
    )
    db.session.add(product)
    db.session.commit()
    return product

def get_product_by_id(product_id):
    """Получить продукт по ID"""
    return Product.query.get(product_id)

def get_all_products():
    """Получить все продукты"""
    return Product.query.all()



def add_to_cart(user_id, product_id, quantity):
    """Добавить продукт в корзину"""
    cart_item = Cartitem(user_id=user_id, product_id=product_id, quantity=quantity)
    db.session.add(cart_item)
    db.session.commit()
    return cart_item

def get_cart_items(user_id):
    """Получить все продукты в корзине пользователя"""
    return Cartitem.query.filter_by(user_id=user_id).all()

def remove_from_cart(cart_item_id):
    """Удалить продукт из корзины"""
    cart_item = Cartitem.query.get(cart_item_id)
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()




def create_order(user_id, status):
    """Создать новый заказ"""
    order = Order(user_id=user_id, status=status)
    db.session.add(order)
    db.session.commit()
    return order

def get_order_by_id(order_id):
    """Получить заказ по ID"""
    return Order.query.get(order_id)

def get_orders_by_user(user_id):
    """Получить все заказы пользователя"""
    return Order.query.filter_by(user_id=user_id).all()



def add_order_item(order_id, product_id, quantity, price):
    """Добавить продукт в заказ"""
    order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    db.session.add(order_item)
    db.session.commit()
    return order_item

def get_order_items(order_id):
    """Получить все элементы заказа по ID заказа"""
    return OrderItem.query.filter_by(order_id=order_id).all()



def add_to_wishlist(user_id, product_id):
    """Добавить продукт в список желаемого"""
    wishlist_item = Wishlist(user_id=user_id, product_id=product_id)
    db.session.add(wishlist_item)
    db.session.commit()
    return wishlist_item

def get_wishlist(user_id):
    """Получить список желаемого для пользователя"""
    return Wishlist.query.filter_by(user_id=user_id).all()

def remove_from_wishlist(wishlist_item_id):
    """Удалить продукт из списка желаемого"""
    wishlist_item = Wishlist.query.get(wishlist_item_id)
    if wishlist_item:
        db.session.delete(wishlist_item)
        db.session.commit()