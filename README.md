# Fuel Route Optimization API

A Django REST API that calculates the optimal fuel stops for a road trip across the USA based on fuel prices and vehicle range.

The API:
- Generates the driving route between two locations
- Finds fuel stations near the route
- Selects cost-effective fuel stops
- Calculates total fuel cost
- Returns route geometry for map rendering

---

# Tech Stack

- Python
- Django 6
- Django REST Framework
- OpenRouteService API
- Pandas
- Geopy

---

# Features

- Route generation using a single routing API call
- Fuel station filtering based on geographic proximity
- Cost-effective fuel stop optimization
- Fuel cost estimation
- Route geometry support for map rendering
- Modular service-based architecture

---

# Project Structure

```text
routes/
│
├── services/
│   ├── routing_service.py
│   ├── fuel_service.py
│   ├── optimizer.py
│   └── utils.py
│
├── serializers.py
├── views.py
├── urls.py
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd fuel_route_optimizer
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Environment Variables

Create a `.env` file in the project root.

```env
ORS_API_KEY=your_openrouteservice_api_key
```

---

## 5. Run Migrations

```bash
python manage.py migrate
```

---

## 6. Start Server

```bash
python manage.py runserver
```

---

# API Endpoint

## Optimize Route

### POST

```text
/api/optimize-route/
```

---

# Sample Request

```json
{
    "start": "New York",
    "finish": "Chicago"
}
```

---

# Sample Response

```json
{
    "start": "New York",
    "finish": "Chicago",
    "distance_miles": 792.76,
    "total_fuel_cost": 130.36,
    "fuel_stops": [
        {
            "truckstop_name": "TURNPIKE MARKET EXPRESS",
            "city": "Newton Falls",
            "state": "OH",
            "price_per_gallon": 3.26,
            "gallons_purchased": 40.0,
            "estimated_fuel_cost": 130.36
        }
    ],
    "nearby_station_count": 83,
    "route_points": 7771,
    "route_geometry": "encoded_polyline_here"
}
```

---

# Optimization Strategy

## Route Sampling

Instead of checking every route coordinate, the route is sampled periodically to reduce expensive geographic distance calculations.

This significantly improves API performance.

---

## Fuel Station Filtering

Fuel stations are filtered geographically before optimization:
- Only stations in relevant route states are processed
- Only stations near the route are considered

This reduces unnecessary computations.

---

## Fuel Optimization Logic

The optimizer:
- Assumes a vehicle range of 500 miles
- Refuels near a safe threshold
- Selects the cheapest reachable nearby station

This minimizes fuel costs while keeping the algorithm efficient.

---

# Assumptions

- Vehicle mileage: 10 MPG
- Maximum vehicle range: 500 miles
- Fuel dataset contains valid fuel prices
- OpenRouteService API is available

---

# Future Improvements

- Real-time fuel prices
- Interactive frontend map
- Better path optimization algorithms
- Redis caching
- Docker deployment
- PostgreSQL support

---

# Author

Amit Mandal