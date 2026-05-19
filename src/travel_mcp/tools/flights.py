from travel_mcp.mock_data.flights import query_flights


def search(
    origin: str,
    destination: str,
    departure_date: str,
    return_date: str | None,
    passengers: int,
) -> list[dict]:
    results = query_flights(origin, destination, departure_date, return_date, passengers)
    if not results:
        return [{"message": f"No flights found from '{origin}' to '{destination}'. Try major city names or airport codes (e.g. 'New York', 'JFK')."}]
    return results
