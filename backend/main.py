from fastapi import FastAPI
from pydantic import BaseModel
from services.trip_service import (
    get_trip_category,
    daily_budget,
    get_recommended_place,
    get_travel_season,
)

app = FastAPI()

# Get endpoint at root path
@app.get("/")
def home():
    return {"message": "Welcome to Candrasa API!"}

# Get health endpoint at the root path
@app.get("/health")
def health():
    return {"status": "OK"}

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


@app.post("/api/v1/trips")
def create_trip(request: TripRequest):
    category = get_trip_category(request.budget)
    daily_cost = daily_budget(request.budget, request.days)
    season = get_travel_season(request.travel_month)
    recommended_place = get_recommended_place(request.budget)

    return {
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
    }


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)