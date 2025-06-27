from sqlalchemy import func
from .models import User, Category, Product, Order, OrderItem, Cartitem, Wishlist
from . import db_object as db



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

def update_cart_item_quantity(cart_item_id, new_quantity):
    """Обновить количество продукта в корзине"""
    cart_item = Cartitem.query.get(cart_item_id)
    if cart_item and new_quantity > 0:
        cart_item.quantity = new_quantity
        db.session.commit()
    elif cart_item:
        remove_from_cart(cart_item_id)

def get_cart_total(user_id):
    """Получить общую стоимость всех товаров в корзине"""
    total = db.session.query(func.sum(Cartitem.quantity * Product.price)).\
            join(Product).\
            filter(Cartitem.user_id == user_id).\
            scalar() or 0
    return total