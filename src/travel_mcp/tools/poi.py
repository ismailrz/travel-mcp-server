from travel_mcp.mock_data.poi import query_poi


def search(destination: str, category: str, limit: int) -> list[dict]:
    results = query_poi(destination, category, limit)
    if not results:
        return [{"message": f"No {category} found in '{destination}'. Try a major city name."}]
    return results
