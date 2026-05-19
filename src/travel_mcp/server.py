import os
from typing import Optional, Literal

from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

from travel_mcp.tools import budget, flights, hotels, itinerary, poi, weather

mcp = FastMCP(
    "travel-planner",
    instructions=(
        "An AI-powered travel planning assistant. "
        "Use these tools to search flights, hotels, weather forecasts, and points of interest, "
        "generate complete trip itineraries, and track travel budgets."
    ),
)


@mcp.tool()
def search_flights(
    origin: str,
    destination: str,
    departure_date: str,
    return_date: Optional[str] = None,
    passengers: int = 1,
) -> list:
    """
    Search for available flights between two cities.

    Args:
        origin: Departure city name or airport code (e.g. "New York" or "JFK")
        destination: Arrival city name or airport code (e.g. "Tokyo" or "NRT")
        departure_date: Departure date in YYYY-MM-DD format
        return_date: Return date for round trips in YYYY-MM-DD format (omit for one-way)
        passengers: Number of passengers (default: 1)
    """
    return flights.search(origin, destination, departure_date, return_date, passengers)


@mcp.tool()
def search_hotels(
    destination: str,
    check_in: str,
    check_out: str,
    guests: int = 1,
    max_price: Optional[float] = None,
) -> list:
    """
    Search for available hotels in a destination.

    Args:
        destination: City name (e.g. "Tokyo", "Paris", "London")
        check_in: Check-in date in YYYY-MM-DD format
        check_out: Check-out date in YYYY-MM-DD format
        guests: Number of guests (default: 1)
        max_price: Maximum price per night in USD (optional)
    """
    return hotels.search(destination, check_in, check_out, guests, max_price)


@mcp.tool()
def get_weather(
    destination: str,
    date_from: str,
    date_to: str,
) -> list:
    """
    Get day-by-day weather forecast for a destination over a date range.

    Args:
        destination: City name (e.g. "Tokyo", "Bali", "Sydney")
        date_from: Start date in YYYY-MM-DD format
        date_to: End date in YYYY-MM-DD format
    """
    return weather.get_forecast(destination, date_from, date_to)


@mcp.tool()
def search_poi(
    destination: str,
    category: Literal["restaurants", "attractions", "activities", "nightlife", "shopping", "transport"],
    limit: int = 5,
) -> list:
    """
    Search for points of interest in a destination.

    Args:
        destination: City name (e.g. "Tokyo", "Barcelona", "Rome")
        category: Type of place — restaurants, attractions, activities, nightlife, shopping, or transport
        limit: Maximum number of results to return (default: 5)
    """
    return poi.search(destination, category, limit)


@mcp.tool()
def plan_trip(
    destination: str,
    start_date: str,
    end_date: str,
    origin: str,
    total_budget: Optional[float] = None,
    preferences: Optional[str] = None,
) -> dict:
    """
    Generate a complete day-by-day travel itinerary combining weather, attractions, dining, and travel options.

    Args:
        destination: Travel destination city (e.g. "Tokyo", "Paris")
        start_date: Trip start date in YYYY-MM-DD format
        end_date: Trip end date in YYYY-MM-DD format
        origin: Departure city for flight search (e.g. "New York", "London")
        total_budget: Total trip budget in USD — enables budget planning and suggested allocation (optional)
        preferences: Comma-separated interests to tailor the itinerary (e.g. "food, history, beaches")
    """
    return itinerary.plan(destination, start_date, end_date, origin, total_budget, preferences)


@mcp.tool()
def create_trip_budget(
    trip_id: str,
    total_budget: float,
    currency: str = "USD",
) -> dict:
    """
    Create a budget tracker for a trip.

    Args:
        trip_id: Unique identifier for the trip (e.g. "tokyo-oct-2024")
        total_budget: Total budget amount
        currency: Currency code (default: "USD")
    """
    return budget.create(trip_id, total_budget, currency)


@mcp.tool()
def add_expense(
    trip_id: str,
    category: Literal["flights", "hotels", "food", "activities", "transport", "shopping", "misc"],
    amount: float,
    description: str,
) -> dict:
    """
    Record an expense against a trip budget.

    Args:
        trip_id: The trip identifier used when creating the budget
        category: Expense category — flights, hotels, food, activities, transport, shopping, or misc
        amount: Amount spent
        description: Brief description of the expense (e.g. "ANA flight JFK→NRT")
    """
    return budget.add_expense(trip_id, category, amount, description)


@mcp.tool()
def get_budget_summary(trip_id: str) -> dict:
    """
    Get a full budget summary: total spent, remaining balance, and per-category breakdown.

    Args:
        trip_id: The trip identifier used when creating the budget
    """
    return budget.get_summary(trip_id)


@mcp.custom_route("/", methods=["GET"])
async def root(_: Request) -> JSONResponse:
    return JSONResponse({"status": "ok", "server": "travel-mcp", "sse": "/sse"})


@mcp.custom_route("/api/tools/search_flights", methods=["POST"])
async def api_search_flights(request: Request) -> JSONResponse:
    body = await request.json()
    result = flights.search(
        body["origin"], body["destination"], body["departure_date"],
        body.get("return_date"), body.get("passengers", 1),
    )
    return JSONResponse(result)


@mcp.custom_route("/api/tools/search_hotels", methods=["POST"])
async def api_search_hotels(request: Request) -> JSONResponse:
    body = await request.json()
    result = hotels.search(
        body["destination"], body["check_in"], body["check_out"],
        body.get("guests", 1), body.get("max_price"),
    )
    return JSONResponse(result)


@mcp.custom_route("/api/tools/get_weather", methods=["POST"])
async def api_get_weather(request: Request) -> JSONResponse:
    body = await request.json()
    result = weather.get_forecast(body["destination"], body["date_from"], body["date_to"])
    return JSONResponse(result)


@mcp.custom_route("/api/tools/search_poi", methods=["POST"])
async def api_search_poi(request: Request) -> JSONResponse:
    body = await request.json()
    result = poi.search(body["destination"], body["category"], body.get("limit", 5))
    return JSONResponse(result)


@mcp.custom_route("/api/tools/plan_trip", methods=["POST"])
async def api_plan_trip(request: Request) -> JSONResponse:
    body = await request.json()
    result = itinerary.plan(
        body["destination"], body["start_date"], body["end_date"], body["origin"],
        body.get("total_budget"), body.get("preferences"),
    )
    return JSONResponse(result)


@mcp.custom_route("/api/tools/create_trip_budget", methods=["POST"])
async def api_create_trip_budget(request: Request) -> JSONResponse:
    body = await request.json()
    result = budget.create(body["trip_id"], body["total_budget"], body.get("currency", "USD"))
    return JSONResponse(result)


@mcp.custom_route("/api/tools/add_expense", methods=["POST"])
async def api_add_expense(request: Request) -> JSONResponse:
    body = await request.json()
    result = budget.add_expense(body["trip_id"], body["category"], body["amount"], body["description"])
    return JSONResponse(result)


@mcp.custom_route("/api/tools/get_budget_summary", methods=["POST"])
async def api_get_budget_summary(request: Request) -> JSONResponse:
    body = await request.json()
    result = budget.get_summary(body["trip_id"])
    return JSONResponse(result)


def main() -> None:
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport == "sse":
        mcp.settings.host = os.getenv("HOST", "0.0.0.0")
        mcp.settings.port = int(os.getenv("PORT", "8000"))
        mcp.run(transport="sse")
    else:
        mcp.run()
