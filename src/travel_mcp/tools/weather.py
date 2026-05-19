from travel_mcp.mock_data.weather import query_forecast


def get_forecast(destination: str, date_from: str, date_to: str) -> list[dict]:
    results = query_forecast(destination, date_from, date_to)
    if not results:
        return [{"message": f"Could not retrieve weather for '{destination}'. Check that dates are in YYYY-MM-DD format."}]
    return results
