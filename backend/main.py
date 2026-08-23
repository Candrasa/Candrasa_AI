from services.trip_service import get_trip_category, get_recommended_place, daily_budget, get_travel_season


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
        hotel_cost +
        transportation_cost +
        food_cost +
        miscellaneous_cost
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


def main():
    destination = input("Destination: ")
    days = int(input("Days: "))
    budget = float(input("Budget: "))
    travel_style = input("Travel Style: ")
    hotel_cost = float(input("Hotel Cost: "))
    transportation_cost = float(input("Transportation Cost: "))
    food_cost = float(input("Food Cost: "))
    travel_month = int(input("Travel Month (1-12): "))
    season = get_travel_season(travel_month)
    miscellaneous_cost = float(input("Miscellaneous Cost: "))

    category = get_trip_category(budget)
    daily_cost = daily_budget(budget, days)

    print(f"Destination: {destination}")
    print(f"Days: {days}")
    print(f"Budget: ${budget}")
    print(f"Travel Style: {travel_style}")
    print(f"Hotel Cost: ${hotel_cost}")
    print(f"Transportation Cost: ${transportation_cost}")
    print(f"Food Cost: ${food_cost}")
    print(f"Miscellaneous Cost: ${miscellaneous_cost}")
    print(f"Category: {category}")
    print(f"Daily Budget: ${daily_cost:.2f}")
    print(f"{category} . ${daily_cost:.2f} per day")
    print(f"Month: {travel_month}")
    print(f"Travel Season: {season}")
    print(get_recommended_place(budget))


if __name__ == "__main__":
    main()