from travel_mcp.mock_data.hotels import query_hotels


def search(
    destination: str,
    check_in: str,
    check_out: str,
    guests: int,
    max_price: float | None,
) -> list[dict]:
    results = query_hotels(destination, check_in, check_out, guests, max_price)
    if not results:
        return [{"message": f"No hotels found in '{destination}'" + (f" under ${max_price}/night." if max_price else ".")}]
    return results
