def print_trip_summary(
        destination, 
        days, 
        budget, 
        travel_style, 
        hotel_cost, 
        transportation_cost, 
        food_cost, 
        miscellaneous_cost
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
    print(f"Miscellaneous Cost: ${miscellaneous_cost}")
    print(f"Total Estimated Cost: ${total_estimated_cost}")

    if total_estimated_cost > budget:
        print("Warning: Your estimated cost exceeds your budget!")

    print()

# Variables store the trip data
# Ini muncul pertama kali kita menjalankan program,
# dan bisa digunakan di mana saja
destination = input("Destination: ")
days = int(input("Days: "))
budget = float(input("Budget: "))
travel_style = input("Travel Style: ")
hotel_cost = float(input("Hotel Cost: "))
transportation_cost = float(input("Transportation Cost: "))
food_cost = float(input("Food Cost: "))
miscellaneous_cost = float(input("Miscellaneous Cost: "))

# Reuse them anywhere
# Ini sama dengan diatas 
# tapi lebih fleksibel dan komunikatif
print(f"Destination: {destination}") # Japan
print(f"Days: {days}") # 5
print(f"Budget: ${budget}") # 1500
print(f"Travel Style: {travel_style}") # Family
print(f"Hotel Cost: ${hotel_cost}") # 300
print(f"Transportation Cost: ${transportation_cost}") # 200
print(f"Food Cost: ${food_cost}") # 150
print(f"Miscellaneous Cost: ${miscellaneous_cost}") # 100

# Ini dari function def yang kita buat diatas
# lebih ringkas dan tinggal memasukkan 
# parameter yang dibutuhkan
print_trip_summary("Singapore", 7, 1000, "formal", 3000, 200, 150, 100)
print_trip_summary("Bontang", 3, 500, "adventure", 200, 100, 50, 30)


