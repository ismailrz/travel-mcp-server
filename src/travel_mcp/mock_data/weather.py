from datetime import datetime, timedelta

# Monthly averages keyed by lowercase city name
# Each entry: avg_high_c, avg_low_c, condition, humidity_pct, rain_chance_pct
_MONTHLY: dict[str, list[dict]] = {
    "tokyo": [
        {"month": 1,  "avg_high": 10, "avg_low": 2,  "condition": "Cold & Sunny",          "humidity": 52, "rain_chance": 20},
        {"month": 2,  "avg_high": 12, "avg_low": 3,  "condition": "Cold & Clear",           "humidity": 55, "rain_chance": 22},
        {"month": 3,  "avg_high": 15, "avg_low": 7,  "condition": "Mild, Cherry Blossoms",  "humidity": 60, "rain_chance": 30},
        {"month": 4,  "avg_high": 20, "avg_low": 12, "condition": "Warm & Pleasant",        "humidity": 65, "rain_chance": 35},
        {"month": 5,  "avg_high": 25, "avg_low": 17, "condition": "Warm",                   "humidity": 70, "rain_chance": 38},
        {"month": 6,  "avg_high": 28, "avg_low": 21, "condition": "Rainy Season",           "humidity": 80, "rain_chance": 55},
        {"month": 7,  "avg_high": 32, "avg_low": 25, "condition": "Hot & Humid",            "humidity": 85, "rain_chance": 40},
        {"month": 8,  "avg_high": 33, "avg_low": 26, "condition": "Hot & Humid",            "humidity": 85, "rain_chance": 35},
        {"month": 9,  "avg_high": 29, "avg_low": 22, "condition": "Warm, Typhoon Risk",     "humidity": 75, "rain_chance": 45},
        {"month": 10, "avg_high": 23, "avg_low": 16, "condition": "Pleasant Autumn",        "humidity": 65, "rain_chance": 30},
        {"month": 11, "avg_high": 17, "avg_low": 9,  "condition": "Cool & Clear",           "humidity": 60, "rain_chance": 25},
        {"month": 12, "avg_high": 12, "avg_low": 4,  "condition": "Cold & Clear",           "humidity": 55, "rain_chance": 18},
    ],
    "paris": [
        {"month": 1,  "avg_high": 7,  "avg_low": 3,  "condition": "Cold & Overcast",  "humidity": 82, "rain_chance": 45},
        {"month": 2,  "avg_high": 8,  "avg_low": 3,  "condition": "Cold & Cloudy",    "humidity": 78, "rain_chance": 40},
        {"month": 3,  "avg_high": 12, "avg_low": 6,  "condition": "Cool & Variable",  "humidity": 75, "rain_chance": 38},
        {"month": 4,  "avg_high": 16, "avg_low": 9,  "condition": "Mild & Showery",   "humidity": 72, "rain_chance": 40},
        {"month": 5,  "avg_high": 20, "avg_low": 13, "condition": "Warm & Sunny",     "humidity": 68, "rain_chance": 35},
        {"month": 6,  "avg_high": 24, "avg_low": 16, "condition": "Warm & Sunny",     "humidity": 65, "rain_chance": 30},
        {"month": 7,  "avg_high": 26, "avg_low": 18, "condition": "Hot & Sunny",      "humidity": 62, "rain_chance": 25},
        {"month": 8,  "avg_high": 26, "avg_low": 18, "condition": "Hot & Sunny",      "humidity": 63, "rain_chance": 25},
        {"month": 9,  "avg_high": 22, "avg_low": 14, "condition": "Pleasant",         "humidity": 68, "rain_chance": 30},
        {"month": 10, "avg_high": 16, "avg_low": 10, "condition": "Cool & Rainy",     "humidity": 78, "rain_chance": 42},
        {"month": 11, "avg_high": 10, "avg_low": 6,  "condition": "Cold & Overcast",  "humidity": 83, "rain_chance": 48},
        {"month": 12, "avg_high": 7,  "avg_low": 3,  "condition": "Cold & Grey",      "humidity": 84, "rain_chance": 50},
    ],
    "london": [
        {"month": 1,  "avg_high": 8,  "avg_low": 3,  "condition": "Cold & Overcast",  "humidity": 80, "rain_chance": 50},
        {"month": 2,  "avg_high": 9,  "avg_low": 3,  "condition": "Cold & Grey",      "humidity": 77, "rain_chance": 45},
        {"month": 3,  "avg_high": 12, "avg_low": 5,  "condition": "Cool & Changeable","humidity": 74, "rain_chance": 40},
        {"month": 4,  "avg_high": 15, "avg_low": 7,  "condition": "Mild & Showery",   "humidity": 70, "rain_chance": 42},
        {"month": 5,  "avg_high": 19, "avg_low": 10, "condition": "Mild & Sunny",     "humidity": 65, "rain_chance": 35},
        {"month": 6,  "avg_high": 22, "avg_low": 13, "condition": "Warm & Sunny",     "humidity": 63, "rain_chance": 30},
        {"month": 7,  "avg_high": 24, "avg_low": 15, "condition": "Warm & Sunny",     "humidity": 60, "rain_chance": 28},
        {"month": 8,  "avg_high": 24, "avg_low": 15, "condition": "Warm & Sunny",     "humidity": 62, "rain_chance": 30},
        {"month": 9,  "avg_high": 20, "avg_low": 12, "condition": "Pleasant",         "humidity": 68, "rain_chance": 35},
        {"month": 10, "avg_high": 15, "avg_low": 8,  "condition": "Cool & Rainy",     "humidity": 76, "rain_chance": 48},
        {"month": 11, "avg_high": 11, "avg_low": 5,  "condition": "Cold & Wet",       "humidity": 82, "rain_chance": 52},
        {"month": 12, "avg_high": 8,  "avg_low": 3,  "condition": "Cold & Overcast",  "humidity": 83, "rain_chance": 55},
    ],
    "barcelona": [
        {"month": 1,  "avg_high": 13, "avg_low": 6,  "condition": "Cool & Sunny",     "humidity": 65, "rain_chance": 25},
        {"month": 2,  "avg_high": 14, "avg_low": 7,  "condition": "Cool & Sunny",     "humidity": 63, "rain_chance": 22},
        {"month": 3,  "avg_high": 16, "avg_low": 9,  "condition": "Mild & Variable",  "humidity": 65, "rain_chance": 30},
        {"month": 4,  "avg_high": 18, "avg_low": 11, "condition": "Mild & Pleasant",  "humidity": 62, "rain_chance": 32},
        {"month": 5,  "avg_high": 22, "avg_low": 15, "condition": "Warm & Sunny",     "humidity": 65, "rain_chance": 28},
        {"month": 6,  "avg_high": 26, "avg_low": 19, "condition": "Hot & Sunny",      "humidity": 65, "rain_chance": 20},
        {"month": 7,  "avg_high": 29, "avg_low": 22, "condition": "Very Hot & Sunny", "humidity": 65, "rain_chance": 10},
        {"month": 8,  "avg_high": 29, "avg_low": 22, "condition": "Very Hot & Sunny", "humidity": 68, "rain_chance": 15},
        {"month": 9,  "avg_high": 26, "avg_low": 19, "condition": "Warm & Sunny",     "humidity": 68, "rain_chance": 25},
        {"month": 10, "avg_high": 21, "avg_low": 15, "condition": "Mild & Sunny",     "humidity": 68, "rain_chance": 35},
        {"month": 11, "avg_high": 17, "avg_low": 11, "condition": "Cool & Variable",  "humidity": 68, "rain_chance": 32},
        {"month": 12, "avg_high": 14, "avg_low": 8,  "condition": "Cool & Sunny",     "humidity": 66, "rain_chance": 25},
    ],
    "bali": [
        {"month": 1,  "avg_high": 30, "avg_low": 24, "condition": "Wet Season",       "humidity": 85, "rain_chance": 70},
        {"month": 2,  "avg_high": 30, "avg_low": 24, "condition": "Wet Season",       "humidity": 85, "rain_chance": 72},
        {"month": 3,  "avg_high": 31, "avg_low": 24, "condition": "Wet Season",       "humidity": 83, "rain_chance": 65},
        {"month": 4,  "avg_high": 31, "avg_low": 24, "condition": "Transitional",     "humidity": 80, "rain_chance": 50},
        {"month": 5,  "avg_high": 31, "avg_low": 23, "condition": "Dry Season Start", "humidity": 75, "rain_chance": 35},
        {"month": 6,  "avg_high": 30, "avg_low": 22, "condition": "Dry & Breezy",     "humidity": 70, "rain_chance": 20},
        {"month": 7,  "avg_high": 29, "avg_low": 21, "condition": "Peak Dry Season",  "humidity": 68, "rain_chance": 12},
        {"month": 8,  "avg_high": 29, "avg_low": 21, "condition": "Peak Dry Season",  "humidity": 68, "rain_chance": 10},
        {"month": 9,  "avg_high": 30, "avg_low": 22, "condition": "Dry & Sunny",      "humidity": 70, "rain_chance": 18},
        {"month": 10, "avg_high": 31, "avg_low": 23, "condition": "Transitional",     "humidity": 75, "rain_chance": 35},
        {"month": 11, "avg_high": 31, "avg_low": 24, "condition": "Wet Season Start", "humidity": 80, "rain_chance": 55},
        {"month": 12, "avg_high": 30, "avg_low": 24, "condition": "Wet Season",       "humidity": 85, "rain_chance": 68},
    ],
    "sydney": [
        {"month": 1,  "avg_high": 26, "avg_low": 19, "condition": "Hot & Sunny",      "humidity": 65, "rain_chance": 35},
        {"month": 2,  "avg_high": 26, "avg_low": 19, "condition": "Hot & Humid",      "humidity": 68, "rain_chance": 38},
        {"month": 3,  "avg_high": 24, "avg_low": 18, "condition": "Warm & Changeable","humidity": 68, "rain_chance": 40},
        {"month": 4,  "avg_high": 22, "avg_low": 15, "condition": "Mild & Sunny",     "humidity": 65, "rain_chance": 32},
        {"month": 5,  "avg_high": 19, "avg_low": 12, "condition": "Cool & Sunny",     "humidity": 62, "rain_chance": 28},
        {"month": 6,  "avg_high": 17, "avg_low": 9,  "condition": "Cool & Rainy",     "humidity": 65, "rain_chance": 35},
        {"month": 7,  "avg_high": 16, "avg_low": 8,  "condition": "Cold & Clear",     "humidity": 62, "rain_chance": 28},
        {"month": 8,  "avg_high": 18, "avg_low": 9,  "condition": "Cool & Sunny",     "humidity": 60, "rain_chance": 25},
        {"month": 9,  "avg_high": 20, "avg_low": 11, "condition": "Warm & Sunny",     "humidity": 62, "rain_chance": 30},
        {"month": 10, "avg_high": 22, "avg_low": 14, "condition": "Warm & Pleasant",  "humidity": 65, "rain_chance": 35},
        {"month": 11, "avg_high": 24, "avg_low": 16, "condition": "Warm & Sunny",     "humidity": 65, "rain_chance": 35},
        {"month": 12, "avg_high": 26, "avg_low": 18, "condition": "Hot & Sunny",      "humidity": 65, "rain_chance": 35},
    ],
    "rome": [
        {"month": 1,  "avg_high": 12, "avg_low": 4,  "condition": "Cool & Rainy",     "humidity": 72, "rain_chance": 40},
        {"month": 2,  "avg_high": 13, "avg_low": 5,  "condition": "Cool & Variable",  "humidity": 68, "rain_chance": 35},
        {"month": 3,  "avg_high": 16, "avg_low": 7,  "condition": "Mild & Sunny",     "humidity": 65, "rain_chance": 32},
        {"month": 4,  "avg_high": 19, "avg_low": 10, "condition": "Warm & Pleasant",  "humidity": 62, "rain_chance": 28},
        {"month": 5,  "avg_high": 24, "avg_low": 14, "condition": "Warm & Sunny",     "humidity": 60, "rain_chance": 20},
        {"month": 6,  "avg_high": 28, "avg_low": 18, "condition": "Hot & Sunny",      "humidity": 55, "rain_chance": 12},
        {"month": 7,  "avg_high": 31, "avg_low": 20, "condition": "Very Hot & Sunny", "humidity": 48, "rain_chance": 8},
        {"month": 8,  "avg_high": 31, "avg_low": 20, "condition": "Very Hot & Sunny", "humidity": 50, "rain_chance": 10},
        {"month": 9,  "avg_high": 27, "avg_low": 17, "condition": "Warm & Pleasant",  "humidity": 58, "rain_chance": 18},
        {"month": 10, "avg_high": 22, "avg_low": 13, "condition": "Mild & Variable",  "humidity": 68, "rain_chance": 32},
        {"month": 11, "avg_high": 16, "avg_low": 9,  "condition": "Cool & Rainy",     "humidity": 74, "rain_chance": 42},
        {"month": 12, "avg_high": 13, "avg_low": 5,  "condition": "Cool & Rainy",     "humidity": 74, "rain_chance": 42},
    ],
    "amsterdam": [
        {"month": 1,  "avg_high": 6,  "avg_low": 1,  "condition": "Cold & Overcast",  "humidity": 86, "rain_chance": 55},
        {"month": 2,  "avg_high": 7,  "avg_low": 1,  "condition": "Cold & Cloudy",    "humidity": 82, "rain_chance": 50},
        {"month": 3,  "avg_high": 10, "avg_low": 4,  "condition": "Cool & Changeable","humidity": 78, "rain_chance": 45},
        {"month": 4,  "avg_high": 14, "avg_low": 6,  "condition": "Mild & Variable",  "humidity": 74, "rain_chance": 40},
        {"month": 5,  "avg_high": 18, "avg_low": 10, "condition": "Warm & Sunny",     "humidity": 70, "rain_chance": 35},
        {"month": 6,  "avg_high": 21, "avg_low": 13, "condition": "Warm & Pleasant",  "humidity": 70, "rain_chance": 32},
        {"month": 7,  "avg_high": 23, "avg_low": 15, "condition": "Warm & Sunny",     "humidity": 70, "rain_chance": 30},
        {"month": 8,  "avg_high": 23, "avg_low": 14, "condition": "Warm & Sunny",     "humidity": 72, "rain_chance": 32},
        {"month": 9,  "avg_high": 19, "avg_low": 11, "condition": "Mild & Sunny",     "humidity": 76, "rain_chance": 38},
        {"month": 10, "avg_high": 14, "avg_low": 8,  "condition": "Cool & Rainy",     "humidity": 82, "rain_chance": 50},
        {"month": 11, "avg_high": 9,  "avg_low": 4,  "condition": "Cold & Overcast",  "humidity": 86, "rain_chance": 55},
        {"month": 12, "avg_high": 7,  "avg_low": 2,  "condition": "Cold & Overcast",  "humidity": 87, "rain_chance": 58},
    ],
    "dubai": [
        {"month": 1,  "avg_high": 24, "avg_low": 14, "condition": "Warm & Sunny",     "humidity": 60, "rain_chance": 5},
        {"month": 2,  "avg_high": 26, "avg_low": 15, "condition": "Warm & Sunny",     "humidity": 58, "rain_chance": 5},
        {"month": 3,  "avg_high": 30, "avg_low": 19, "condition": "Hot & Sunny",      "humidity": 55, "rain_chance": 5},
        {"month": 4,  "avg_high": 35, "avg_low": 22, "condition": "Very Hot & Sunny", "humidity": 50, "rain_chance": 3},
        {"month": 5,  "avg_high": 40, "avg_low": 27, "condition": "Extremely Hot",    "humidity": 45, "rain_chance": 1},
        {"month": 6,  "avg_high": 42, "avg_low": 29, "condition": "Extremely Hot",    "humidity": 55, "rain_chance": 0},
        {"month": 7,  "avg_high": 41, "avg_low": 30, "condition": "Extremely Hot",    "humidity": 60, "rain_chance": 0},
        {"month": 8,  "avg_high": 41, "avg_low": 30, "condition": "Extremely Hot",    "humidity": 62, "rain_chance": 0},
        {"month": 9,  "avg_high": 38, "avg_low": 27, "condition": "Very Hot & Humid", "humidity": 65, "rain_chance": 0},
        {"month": 10, "avg_high": 34, "avg_low": 23, "condition": "Hot & Sunny",      "humidity": 60, "rain_chance": 1},
        {"month": 11, "avg_high": 29, "avg_low": 19, "condition": "Warm & Sunny",     "humidity": 58, "rain_chance": 3},
        {"month": 12, "avg_high": 25, "avg_low": 15, "condition": "Warm & Sunny",     "humidity": 60, "rain_chance": 5},
    ],
}

_DEFAULT_WEATHER = [
    {"month": m, "avg_high": 22, "avg_low": 14, "condition": "Mild & Variable", "humidity": 65, "rain_chance": 30}
    for m in range(1, 13)
]


def query_forecast(destination: str, date_from: str, date_to: str) -> list[dict]:
    city = destination.strip().lower()
    monthly = _MONTHLY.get(city)
    if not monthly:
        for key in _MONTHLY:
            if key in city or city in key:
                monthly = _MONTHLY[key]
                break
    if not monthly:
        monthly = _DEFAULT_WEATHER

    try:
        start = datetime.strptime(date_from, "%Y-%m-%d")
        end = datetime.strptime(date_to, "%Y-%m-%d")
    except ValueError:
        return []

    forecast = []
    current = start
    while current <= end:
        month_data = monthly[current.month - 1]
        # Add slight daily variation
        day_offset = (current - start).days
        high_var = (day_offset % 3) - 1  # -1, 0, +1 cycling
        forecast.append({
            "date": current.strftime("%Y-%m-%d"),
            "day_of_week": current.strftime("%A"),
            "high_celsius": month_data["avg_high"] + high_var,
            "low_celsius": month_data["avg_low"] + high_var,
            "high_fahrenheit": round((month_data["avg_high"] + high_var) * 9 / 5 + 32),
            "low_fahrenheit": round((month_data["avg_low"] + high_var) * 9 / 5 + 32),
            "condition": month_data["condition"],
            "humidity_pct": month_data["humidity"],
            "rain_chance_pct": month_data["rain_chance"],
        })
        current += timedelta(days=1)

    return forecast
