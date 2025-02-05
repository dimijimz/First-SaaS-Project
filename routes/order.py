# routes/order.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.database import db
from models.order import Order

order_bp = Blueprint('order', __name__)

@order_bp.route('/', methods=['POST'])
@jwt_required()
def create_order():
    data = request.get_json()
    current_user = get_jwt_identity()
    
    # Create a new order using the provided data
    order = Order(
        total_amount=data.get("total_amount"),
        user_id=current_user
    )
    db.session.add(order)
    db.session.commit()
    
    return jsonify({
        "msg": "Order created",
        "order": {
            "id": order.id,
            "order_date": order.order_date.isoformat(),
            "total_amount": order.total_amount
        }
    }), 201

@order_bp.route('/', methods=['GET'])
@jwt_required()
def get_orders():
    current_user = get_jwt_identity()
    orders = Order.query.filter_by(user_id=current_user).all()
    
    order_list = [{
        "id": o.id,
        "order_date": o.order_date.isoformat(),
        "total_amount": o.total_amount
    } for o in orders]
    
    return jsonify(order_list), 200
