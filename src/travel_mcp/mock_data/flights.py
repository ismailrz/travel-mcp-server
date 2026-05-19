_ROUTES = [
    {
        "origin": "New York", "origin_code": "JFK",
        "destination": "Tokyo", "destination_code": "NRT",
        "options": [
            {"airline": "ANA", "flight": "NH010", "duration": 14.0, "stops": 0, "price": 850},
            {"airline": "JAL", "flight": "JL004", "duration": 13.5, "stops": 0, "price": 920},
            {"airline": "Delta", "flight": "DL169", "duration": 15.5, "stops": 1, "price": 680},
            {"airline": "United", "flight": "UA837", "duration": 16.0, "stops": 1, "price": 620},
        ],
    },
    {
        "origin": "New York", "origin_code": "JFK",
        "destination": "Paris", "destination_code": "CDG",
        "options": [
            {"airline": "Air France", "flight": "AF011", "duration": 7.5, "stops": 0, "price": 520},
            {"airline": "Delta", "flight": "DL263", "duration": 7.5, "stops": 0, "price": 490},
            {"airline": "United", "flight": "UA57", "duration": 8.5, "stops": 1, "price": 380},
            {"airline": "Norse Atlantic", "flight": "N0701", "duration": 8.0, "stops": 0, "price": 310},
        ],
    },
    {
        "origin": "New York", "origin_code": "JFK",
        "destination": "London", "destination_code": "LHR",
        "options": [
            {"airline": "British Airways", "flight": "BA178", "duration": 7.0, "stops": 0, "price": 480},
            {"airline": "American", "flight": "AA100", "duration": 7.0, "stops": 0, "price": 460},
            {"airline": "Virgin Atlantic", "flight": "VS004", "duration": 7.0, "stops": 0, "price": 445},
            {"airline": "Norse Atlantic", "flight": "N0001", "duration": 7.5, "stops": 0, "price": 290},
        ],
    },
    {
        "origin": "New York", "origin_code": "JFK",
        "destination": "Barcelona", "destination_code": "BCN",
        "options": [
            {"airline": "Iberia", "flight": "IB6251", "duration": 8.0, "stops": 0, "price": 510},
            {"airline": "Level", "flight": "IB2671", "duration": 8.5, "stops": 0, "price": 350},
            {"airline": "American", "flight": "AA068", "duration": 9.5, "stops": 1, "price": 430},
        ],
    },
    {
        "origin": "New York", "origin_code": "JFK",
        "destination": "Sydney", "destination_code": "SYD",
        "options": [
            {"airline": "Qantas", "flight": "QF12", "duration": 21.5, "stops": 1, "price": 1250},
            {"airline": "United", "flight": "UA870", "duration": 22.0, "stops": 1, "price": 1100},
            {"airline": "Air New Zealand", "flight": "NZ6", "duration": 23.0, "stops": 1, "price": 1050},
        ],
    },
    {
        "origin": "New York", "origin_code": "JFK",
        "destination": "Bali", "destination_code": "DPS",
        "options": [
            {"airline": "Singapore Airlines", "flight": "SQ026", "duration": 22.0, "stops": 1, "price": 1100},
            {"airline": "Cathay Pacific", "flight": "CX830", "duration": 23.5, "stops": 1, "price": 980},
            {"airline": "Qatar Airways", "flight": "QR706", "duration": 24.0, "stops": 1, "price": 950},
        ],
    },
    {
        "origin": "London", "origin_code": "LHR",
        "destination": "Paris", "destination_code": "CDG",
        "options": [
            {"airline": "Air France", "flight": "AF1681", "duration": 1.5, "stops": 0, "price": 120},
            {"airline": "British Airways", "flight": "BA308", "duration": 1.5, "stops": 0, "price": 135},
            {"airline": "EasyJet", "flight": "EZY8872", "duration": 1.5, "stops": 0, "price": 65},
        ],
    },
    {
        "origin": "London", "origin_code": "LHR",
        "destination": "Barcelona", "destination_code": "BCN",
        "options": [
            {"airline": "Vueling", "flight": "VY7822", "duration": 2.5, "stops": 0, "price": 95},
            {"airline": "British Airways", "flight": "BA482", "duration": 2.5, "stops": 0, "price": 145},
            {"airline": "Ryanair", "flight": "FR4476", "duration": 2.5, "stops": 0, "price": 55},
        ],
    },
    {
        "origin": "Sydney", "origin_code": "SYD",
        "destination": "Bali", "destination_code": "DPS",
        "options": [
            {"airline": "Jetstar", "flight": "JQ37", "duration": 6.0, "stops": 0, "price": 220},
            {"airline": "Qantas", "flight": "QF43", "duration": 6.0, "stops": 0, "price": 310},
            {"airline": "Air Asia", "flight": "D7237", "duration": 8.5, "stops": 1, "price": 180},
        ],
    },
    {
        "origin": "Paris", "origin_code": "CDG",
        "destination": "Rome", "destination_code": "FCO",
        "options": [
            {"airline": "Air France", "flight": "AF1010", "duration": 2.0, "stops": 0, "price": 110},
            {"airline": "Alitalia", "flight": "AZ319", "duration": 2.0, "stops": 0, "price": 130},
            {"airline": "EasyJet", "flight": "EZY6920", "duration": 2.0, "stops": 0, "price": 75},
        ],
    },
]


def _matches(query: str, city: str, code: str) -> bool:
    q = query.strip().lower()
    return q in city.lower() or q == code.lower()


def query_flights(
    origin: str,
    destination: str,
    departure_date: str,
    return_date: str | None,
    passengers: int,
) -> list[dict]:
    results = []
    for route in _ROUTES:
        orig_match = _matches(origin, route["origin"], route["origin_code"])
        dest_match = _matches(destination, route["destination"], route["destination_code"])
        if not (orig_match and dest_match):
            # Also try reverse (for flexibility, but mark as reverse)
            continue
        for opt in route["options"]:
            outbound_price = opt["price"] * passengers
            total = outbound_price * (2 if return_date else 1)
            results.append({
                "airline": opt["airline"],
                "flight_number": opt["flight"],
                "origin": f"{route['origin']} ({route['origin_code']})",
                "destination": f"{route['destination']} ({route['destination_code']})",
                "departure_date": departure_date,
                "return_date": return_date,
                "duration": f"{opt['duration']:.1f}h",
                "stops": opt["stops"],
                "trip_type": "round-trip" if return_date else "one-way",
                "price_per_person": opt["price"],
                "total_price": total,
                "currency": "USD",
            })
    return sorted(results, key=lambda x: x["total_price"])
