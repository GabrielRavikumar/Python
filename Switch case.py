#SWITCH CASE
def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            print(f"Yes {day} is a holiday")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print(f"No {day} is not a holiday")
        case _:
            print("Invalid day")
is_weekend(input().capitalize())