# routes/forecast.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import numpy as np
import pickle

forecast_bp = Blueprint('forecast', __name__)

# Load the pre-trained demand forecasting model
with open('demand_model.pkl', 'rb') as f:
    demand_model = pickle.load(f)

@forecast_bp.route('/forecast', methods=['POST'])
@jwt_required()
def forecast_demand():
    """
    Expects JSON with features:
    {
      "temperature": 75,
      "humidity": 50,
      "day_of_week": 5,
      "local_event": 1  # 1 if a local event is happening, else 0
    }
    """
    data = request.get_json()
    # Ensure that all expected keys are provided
    features = np.array([
        data.get('temperature'),
        data.get('humidity'),
        data.get('day_of_week'),
        data.get('local_event')
    ]).reshape(1, -1)
    
    predicted_demand = demand_model.predict(features)[0]
    return jsonify({"predicted_demand": predicted_demand}), 200
