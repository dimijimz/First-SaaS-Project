# RoamX

**Empower Your Mobile Business with AI**

RoamX is an AI-powered mobile business management platform designed specifically for small, mobile enterprises such as food trucks, local couriers, and service providers. Our mission is to simplify operations, optimize routes, forecast demand, and manage orders—all in one intuitive system. Whether you’re a food truck owner looking to serve customers at the right place and time or a local service provider managing on-the-go appointments, RoamX helps you make smarter, data-driven decisions.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Why RoamX?](#why-roamx)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
- [API Endpoints](#api-endpoints)
- [Testing Your API](#testing-your-api)
- [Roadmap & Future Enhancements](#roadmap--future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

RoamX is a prototype for an integrated management system that leverages artificial intelligence to help mobile businesses operate more efficiently. The core components of RoamX include:

- **User Authentication:** Secure registration and login using JWT.
- **Order Management:** Create, track, and manage orders easily.
- **AI-Driven Demand Forecasting:** A machine learning model (currently a dummy model) predicts customer demand based on factors such as weather, local events, and historical trends.
- **Route Optimization (Planned):** A placeholder endpoint to integrate real-time mapping (Google Maps/Mapbox) for optimal routing.
- **Third-Party Integrations (Future):** Planned support for notification (Twilio, SendGrid) and payment APIs (Stripe, Square).

---

## Key Features

- **User Authentication & Security:**  
  Simple and secure access using JWT-based authentication.

- **Order Management:**  
  Streamlined API endpoints to create and monitor orders, ideal for on-the-go business operations.

- **Demand Forecasting:**  
  Utilize AI to predict high-demand periods, helping you optimize staffing and inventory.

- **Route Optimization:**  
  *(Coming Soon)* Integrate mapping APIs to provide the most efficient routes and locations for mobile businesses.

- **Extensibility:**  
  Designed with scalability in mind—ready for further integrations like notifications and payment processing.

---

## Why RoamX?

### For Food Truck Operators:
- **Maximize Sales:** Identify peak traffic areas and times.
- **Reduce Wait Times:** Efficient order management improves customer experience.
- **Cut Costs:** Optimize routes to save fuel and time.

### For Mobile Service Providers:
- **Efficient Scheduling:** Automatically assign and route service calls.
- **Predict Demand:** Stay ahead with AI-driven insights.
- **Enhanced Communication:** Keep customers updated in real time.

---

## Technology Stack

- **Backend:** Python, Flask, Flask-JWT-Extended, Flask-SQLAlchemy
- **Database:** PostgreSQL
- **Machine Learning:** scikit-learn (for a dummy forecasting model; to be enhanced)
- **Frontend (Upcoming):** React (or your preferred modern JavaScript framework)
- **Planned API Integrations:** Google Maps/Mapbox for routing, Twilio/SendGrid for notifications, Stripe/Square for payments

---

## Getting Started

### Prerequisites

- **Python 3.13.1 or later**
- **PostgreSQL:** Ensure PostgreSQL is installed and running (e.g., via Homebrew).
- **Git** installed on your system.

### Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/dimijimz/First-SaaS-Project.git
   cd First-SaaS-Project

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencides:**

   ```bash
   pip install -r requirements.txt

4. **Configure Environment Variables:**

Create a .env file in the root of the project and add:

   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_super_secret_key
   JWT_SECRET_KEY=your_jwt_secret
   DATABASE_URL=postgresql://dimijimz@localhost:5432/roamx
   ```

5. **Setup the Database:**
Ensure your PostgreSQL server is running and create the database:

   ```bash
   createdb -U dimijimz roamx
   ```

6. **Run the App:**
Start your Flask server:

  ```bash
  python app.py
  ```
### Your app should now be running at http://127.0.0.1:5000

---

## API Endpoints
### Authentication

Register: POST /api/roamx/auth/register
Payload example:

  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
Login: POST /api/roamx/auth/login
Payload example:

  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
Response: Returns a JWT token for authenticated requests.
### Order Management
Create Order: POST /api/roamx/order/
Payload example:
  ```json
  {
    "total_amount": 25.50
  }
  ```
*Requires JWT auth in header*
Retrieve Orders: GET /api/roamx/orders/
*Requires JWT auth in header.*

### Demand Forecasting
Forecast Demand: POST /api/roamx/forecast/forecast
Payload example:

  ```json
  {
    "temperature": 75,
    "humidity": 50,
    "day_of_week": 5,
    "local_event": 1
  }
  ```
  *Response: Returns a predicted demand value using our AI model. Requires JWT Auth in header.*
