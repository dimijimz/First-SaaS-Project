from flask import Flask
from config import Config
from utils.database import db
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.order import order_bp
from routes.route import route_bp
from routes.forecast import forecast_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/api/roamx/auth")
app.register_blueprint(order_bp, url_prefix="/api/roamx/orders")
app.register_blueprint(route_bp, url_prefix="/api/roamx/routes")
app.register_blueprint(forecast_bp, url_prefix="/api/roamx")

# Instead of using the before_first_request decorator, use an app context block
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
