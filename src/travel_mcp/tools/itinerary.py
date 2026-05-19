from __future__ import annotations

from datetime import datetime, timedelta

from travel_mcp.mock_data.flights import query_flights
from travel_mcp.mock_data.hotels import query_hotels
from travel_mcp.mock_data.poi import query_poi
from travel_mcp.mock_data.weather import query_forecast
from travel_mcp.tools import budget as budget_module


def _suggest_allocation(total: float, nights: int, flight_price: float, nightly_rate: float) -> dict:
    flight_cost = min(flight_price * 2, total * 0.35)  # round-trip estimate, capped at 35%
    hotel_cost = min(nightly_rate * nights, total * 0.35)
    remaining = max(total - flight_cost - hotel_cost, total * 0.30)
    return {
        "flights": round(flight_cost, 2),
        "hotels": round(hotel_cost, 2),
        "food": round(remaining * 0.38, 2),
        "activities": round(remaining * 0.28, 2),
        "transport": round(remaining * 0.14, 2),
        "shopping": round(remaining * 0.12, 2),
        "misc": round(remaining * 0.08, 2),
    }


def plan(
    destination: str,
    start_date: str,
    end_date: str,
    origin: str,
    total_budget: float | None = None,
    preferences: str | None = None,
) -> dict:
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    days = (end - start).days + 1
    if days < 1:
        return {"error": "end_date must be after start_date."}

    # Gather supporting data
    weather = query_forecast(destination, start_date, end_date)
    attractions = query_poi(destination, "attractions", 10)
    restaurants = query_poi(destination, "restaurants", 10)
    activities = query_poi(destination, "activities", 8)
    nightlife = query_poi(destination, "nightlife", 4)
    flight_opts = query_flights(origin, destination, start_date, end_date, 1)[:3]
    hotel_opts = query_hotels(destination, start_date, end_date, 1, None)[:3]

    pref_tags = [p.strip().lower() for p in preferences.split(",")] if preferences else []

    # Build day-by-day itinerary
    itinerary = []
    for i in range(days):
        date = start + timedelta(days=i)
        day_weather = next((w for w in weather if w["date"] == date.strftime("%Y-%m-%d")), None)

        day: dict = {
            "day": i + 1,
            "date": date.strftime("%Y-%m-%d"),
            "day_of_week": date.strftime("%A"),
        }

        if day_weather:
            day["weather"] = {
                "condition": day_weather["condition"],
                "high": f"{day_weather['high_celsius']}°C / {day_weather['high_fahrenheit']}°F",
                "low": f"{day_weather['low_celsius']}°C / {day_weather['low_fahrenheit']}°F",
                "rain_chance": f"{day_weather['rain_chance_pct']}%",
            }

        if i == 0:
            day["theme"] = "Arrival Day"
            day["morning"] = "Arrive and check into your hotel. Rest and freshen up after the journey."
            day["afternoon"] = attractions[:1] if attractions else []
            day["evening"] = restaurants[:1] if restaurants else []
        elif i == days - 1:
            day["theme"] = "Departure Day"
            day["morning"] = "Final breakfast and last-minute souvenir shopping. Check out of hotel."
            day["afternoon"] = []
            day["evening"] = "Head to the airport for your return flight."
        else:
            inner_day = i - 1
            day["theme"] = f"Explore {destination}"
            attr_slice = attractions[inner_day % max(len(attractions), 1): (inner_day % max(len(attractions), 1)) + 2]
            day["morning"] = attr_slice if attr_slice else (attractions[:2] if attractions else [])
            day["afternoon"] = activities[inner_day % max(len(activities), 1)] if activities else None
            rest_idx = (i * 2) % max(len(restaurants), 1)
            day["evening"] = {
                "dinner": restaurants[rest_idx] if restaurants else None,
                "nightlife": nightlife[inner_day % max(len(nightlife), 1)] if nightlife and i % 2 == 0 else None,
            }

        itinerary.append(day)

    result: dict = {
        "trip": {
            "destination": destination,
            "origin": origin,
            "start_date": start_date,
            "end_date": end_date,
            "duration_days": days,
            "preferences": pref_tags or "general",
        },
        "flight_options": flight_opts or [{"message": f"No direct routes found from {origin} to {destination} in mock data."}],
        "hotel_suggestions": hotel_opts or [{"message": f"No hotels found for {destination} in mock data."}],
        "itinerary": itinerary,
    }

    if total_budget is not None:
        trip_id = f"{destination.lower().replace(' ', '-')}-{start_date}"
        flight_price = flight_opts[0]["price_per_person"] if flight_opts and "price_per_person" in flight_opts[0] else 500
        nightly_rate = hotel_opts[0]["price_per_night"] if hotel_opts and "price_per_night" in hotel_opts[0] else 150
        allocation = _suggest_allocation(total_budget, days - 1, flight_price, nightly_rate)
        budget_module.create(trip_id, total_budget)
        result["budget"] = {
            "trip_id": trip_id,
            "total_budget": total_budget,
            "currency": "USD",
            "suggested_allocation": allocation,
            "note": f"Use trip_id '{trip_id}' with add_expense and get_budget_summary to track spending.",
        }

    return result
