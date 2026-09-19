
# Business category based on budget
def get_trip_category(budget):
    if budget < 1000:
        return "Backpacker"
    elif budget <= 3000:
        return "Family"
    elif budget <= 5000:
        return "Standard"
    else:
        return "Luxury"


# Arithmetic operators: + - * / //
def calculate_daily_budget(budget, days):
    if days <= 0:
        raise ValueError("days must be greater than 0")
    return budget / days


def daily_budget(budget, days):
    return calculate_daily_budget(budget, days)


def get_recommended_place(budget):
    category = get_trip_category(budget)

    if category == "Backpacker":
        return "Recommended place: Bali for backpackers, travel by bus."
    elif category == "Family":
        return "Recommended place: Kyoto for family travelers, travel by train." 
    elif category == "Standard":
        return "Recommended place: Paris for standard travelers, travel by Car."
    else:
        return "Recommended place: Maldives for luxury travelers, travel by plane."

def get_travel_season(month):
    month_name = month.strip().title()
    if month_name in ["December", "January", "February"]:
        return "Winter, Peak Season"
    elif month_name in ["March", "April", "May"]:
        return "Spring, Regular Season"
    elif month_name in ["June", "July", "August"]:
        return "Summer, Holiday Season"
    elif month_name in ["September", "October", "November"]:
        return "Autumn, Regular Season"
    else:
        return "Invalid month. Please provide a valid month name (e.g., January, February, etc.)."