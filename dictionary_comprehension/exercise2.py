weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def temp_to_f(t):
    return (t * 9 / 5) + 32


weather_f = {day: temp_to_f(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)
