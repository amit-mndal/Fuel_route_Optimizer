<img width="811" height="796" alt="image" src="https://github.com/user-attachments/assets/a1ab15ee-4d9b-4996-a21b-0535430c65fb" />












# Fuel Route Optimizer

A full-stack fuel route optimization platform that calculates optimal fuel stops for long-distance road trips across the USA using real-world routing data and fuel station datasets.

The system:
- Generates routes between two locations
- Finds fuel stations near the route
- Optimizes fuel stops based on fuel range and fuel prices
- Calculates estimated trip fuel cost
- Displays route visualization on an interactive map
- Provides a modern React frontend with live API integration

---

# Live Features

✅ Route Optimization  
✅ Fuel Cost Estimation  
✅ Interactive Route Map  
✅ Fuel Stop Recommendations  
✅ Real-world Route Geometry  
✅ Responsive Frontend UI  
✅ Django REST API Backend  
✅ React + Tailwind Frontend  







<img width="1230" height="847" alt="image" src="https://github.com/user-attachments/assets/1778856c-1894-488c-a0d3-35759964e31a" />






---

# Tech Stack

## Backend
- Python
- Django 6
- Django REST Framework
- OpenRouteService API
- Pandas
- Geopy
- Polyline

## Frontend
- React
- Vite
- Tailwind CSS
- React Leaflet
- Axios
- Framer Motion

---

# System Architecture

```text
Frontend (React + Tailwind)
        ↓
Django REST API
        ↓
Routing + Fuel Optimization Services
        ↓
OpenRouteService API + Fuel Dataset
```

---

# Project Structure

```text
fuel_route_optimizer/
│
├── Frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   │
│   └── package.json
│
├── routes/
│   ├── services/
│   │   ├── routing_service.py
│   │   ├── fuel_service.py
│   │   ├── optimizer.py
│   │   └── utils.py
│   │
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── config/
├── data/
├── manage.py
└── requirements.txt
```

---

# Core Features

## Route Generation

Uses OpenRouteService API to generate real driving routes between locations.

---

## Fuel Station Discovery

Scans fuel station datasets and filters stations geographically near the route.

---

## Fuel Optimization

The optimizer:
- tracks traveled distance
- estimates fuel usage
- selects nearby stations
- chooses cheaper fuel stops
- minimizes overall fuel cost

---

## Interactive Map Rendering

The frontend renders:
- route polylines
- optimized trip visualization
- fuel stop information

using React Leaflet maps.

---

# Setup Instructions

# 1. Clone Repository

```bash
git clone https://github.com/amit-mndal/Fuel_route_Optimizer.git
cd Fuel_route_Optimizer
```

---

# 2. Backend Setup

## Create Virtual Environment

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

## Install Backend Dependencies

```bash
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install pandas
pip install geopy
pip install polyline
pip install requests
pip install python-dotenv
```

---

## Create `.env`

Create a `.env` file in project root:

```env
ORS_API_KEY=your_openrouteservice_api_key
```

---

## Run Django Server

```bash
python manage.py runserver
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# 3. Frontend Setup

Go to frontend folder:

```bash
cd Frontend
```

Install dependencies:

```bash
npm install
```

Start frontend:

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
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
  "finish": "Los Angeles"
}
```

---

# Sample Response

```json
{
  "start": "New York",
  "finish": "Los Angeles",
  "distance_miles": 2793.61,
  "total_fuel_cost": 321.57,
  "fuel_stops": [
    {
      "truckstop_name": "Pilot Travel Center",
      "city": "Ohio",
      "state": "OH",
      "price_per_gallon": 3.21,
      "gallons_purchased": 50.0,
      "estimated_fuel_cost": 160.5
    }
  ],
  "nearby_station_count": 300,
  "route_points": 15000,
  "route_geometry": "encoded_polyline_here"
}
```

---

# Optimization Logic

## Route Sampling

Instead of checking every route coordinate, the route is sampled periodically for faster geographic computations.

This dramatically improves API performance.

---

## Geographic Filtering

Fuel stations are filtered based on:
- route proximity
- geographic distance
- reachable fuel range

This reduces unnecessary computations.

---

## Fuel Strategy

The optimizer:
- estimates vehicle range
- calculates safe refueling intervals
- searches nearby stations
- selects lower-cost stations

---

# Assumptions

- Vehicle MPG: 10
- Safe fuel range: 500 miles
- Fuel dataset contains valid station coordinates
- OpenRouteService API availability

---

# Future Improvements

- Real-time fuel pricing APIs
- Authentication system
- Docker deployment
- PostgreSQL integration
- Redis caching
- Advanced optimization algorithms
- AI-based route prediction
- Deployment on AWS/GCP

---

# Author

Amit Mandal
