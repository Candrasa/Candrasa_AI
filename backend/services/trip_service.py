
# Business category based on budget
def get_trip_category(budget):
    if budget < 1000:
        return "Backpacker"
    elif budget <= 3000:
        return "Standard"
    else:
        return "Luxury"


# Arithmetic operators: + - * / //
def daily_budget(budget, days):
    return budget / days


def get_recommended_place(budget):
    category = get_trip_category(budget)

    if category == "Backpacker":
        return "Recommended place: Bali for backpackers, travel by bus."
    elif category == "Standard":
        return "Recommended place: Kyoto for standard travelers, travel by train."
    else:
        return "Recommended place: Maldives for luxury travelers, travel by plane."

def get_travel_season(month):
    if month in [12, 1, 2]:
        return "Winter, Peak Season"
    elif month in [3, 4, 5]:
        return "Spring, Regular Season"
    elif month in [6, 7, 8]:
        return "Summer, Holiday Season"
    else:
        return "Autumn, Season"