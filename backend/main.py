import os
import socket

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

try:
    from .database import SessionLocal, init_db
    from .models.trip import Trip
    from .services.trip_service import (
        calculate_daily_budget,
        daily_budget,
        get_recommended_place,
        get_travel_season,
        get_trip_category,
    )
except ImportError:  # direct script execution from the backend folder
    from database import SessionLocal, init_db
    from models.trip import Trip
    from services.trip_service import (
        calculate_daily_budget,
        daily_budget,
        get_recommended_place,
        get_travel_season,
        get_trip_category,
    )


class TripRequest(BaseModel):
    destination: str
    days: int
    budget: float
    travel_style: str
    hotel_cost: float
    transportation_cost: float
    food_cost: float
    travel_month: str
    miscellaneous_cost: float


class TripUpdateRequest(BaseModel):
    budget: float


# Initialize the database
init_db()

app = FastAPI(title="Candrasa API", version="1.0.0")


def serialize_trip(trip: Trip):
    return {
        "id": trip.id,
        "destination": trip.destination,
        "days": trip.days,
        "budget": trip.budget,
        "category": trip.category,
        "daily_budget": trip.daily_budget,
        "created_at": trip.created_at.isoformat() if trip.created_at else None,
    }


@app.get("/")
def home():
    return {"message": "Welcome to Candrasa API!"}


@app.get("/health")
def health():
    return {"status": "OK"}


@app.get("/api/v1/recommendation")
def get_recommendation(budget: float, travel_style: str = "family"):
    category = get_trip_category(budget)
    place = get_recommended_place(budget)

    return {
        "budget": budget,
        "travel_style": travel_style,
        "category": category,
        "recommended_place": place,
    }


@app.get("/api/v1/transportation")
def transportation_list():
    return {"transportation": ["Bus", "Train", "Car", "Plane"]}


@app.get("/api/v1/trip-categories")
def trip_categories():
    return {"trip_categories": ["Backpacker", "Family", "Standard", "Luxury"]}


@app.get("/api/v1/trips")
def list_trips():
    db = SessionLocal()
    trips = db.query(Trip).all()
    db.close()
    return [serialize_trip(trip) for trip in trips]


@app.post("/api/v1/trips")
def create_trip(request: TripRequest):
    category = get_trip_category(request.budget)
    daily_cost = calculate_daily_budget(request.budget, request.days)
    season = get_travel_season(request.travel_month)
    recommended_place = get_recommended_place(request.budget)

    total_estimated_cost = (
        request.hotel_cost
        + request.transportation_cost
        + request.food_cost
        + request.miscellaneous_cost
    )

    trip = Trip(
        destination=request.destination,
        days=request.days,
        budget=request.budget,
        category=category,
        daily_budget=daily_cost,
    )
    db = SessionLocal()
    db.add(trip)
    db.commit()
    db.refresh(trip)
    db.close()

    return {
        "id": trip.id,
        "destination": request.destination,
        "days": request.days,
        "budget": request.budget,
        "travel_style": request.travel_style,
        "hotel_cost": request.hotel_cost,
        "transportation_cost": request.transportation_cost,
        "food_cost": request.food_cost,
        "miscellaneous_cost": request.miscellaneous_cost,
        "category": category,
        "daily_budget": daily_cost,
        "travel_month": request.travel_month,
        "season": season,
        "recommended_place": recommended_place,
        "total_estimated_cost": total_estimated_cost,
        "created_at": trip.created_at.isoformat() if trip.created_at else None,
    }


@app.get("/api/v1/trips/{trip_id}")
def get_trip(trip_id: int):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    db.close()
    if trip is None:
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")
    return serialize_trip(trip)


@app.put("/api/v1/trips/{trip_id}")
def update_trip_budget(trip_id: int, update: TripUpdateRequest):
    db = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail=f"Trip with id {trip_id} not found")

    trip.budget = update.budget
    trip.category = get_trip_category(trip.budget)
    trip.daily_budget = calculate_daily_budget(trip.budget, trip.days)

    db.commit()
    db.refresh(trip)
    db.close()
    return serialize_trip(trip)


def print_trip_summary(
    destination,
    days,
    budget,
    travel_style,
    hotel_cost,
    transportation_cost,
    food_cost,
    miscellaneous_cost,
    travel_month,
    season,
):
    total_estimated_cost = (
        hotel_cost + transportation_cost + food_cost + miscellaneous_cost
    )

    print("================================")
    print("Candrasa_AI")
    print("================================")
    print(f"Destination: {destination}")
    print(f"Days: {days}")
    print(f"Budget: ${budget}")
    print(f"Travel Style: {travel_style}")
    print(f"Hotel Cost: ${hotel_cost}")
    print(f"Transportation Cost: ${transportation_cost}")
    print(f"Food Cost: ${food_cost}")
    print(f"Travel Month: {travel_month}")
    print(f"Season: {season}")
    print(f"Miscellaneous Cost: ${miscellaneous_cost}")
    print(f"Total Estimated Cost: ${total_estimated_cost}")

    if total_estimated_cost > budget:
        print("Warning: Your estimated cost exceeds your budget!")

    print()


def _find_available_port(host: str = "127.0.0.1", start_port: int = 8000, max_tries: int = 20) -> int:
    for port in range(start_port, start_port + max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
                return port
            except OSError:
                continue
    raise OSError(f"No free port found in range {start_port}-{start_port + max_tries - 1}")


if __name__ == "__main__":
    import uvicorn

    # When running this file directly, uvicorn requires an import string.
    # reload=True is not compatible with passing the app object directly.
    port = int(os.getenv("PORT", _find_available_port()))
    print(f"Starting Candrasa API on http://127.0.0.1:{port}")
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=False)