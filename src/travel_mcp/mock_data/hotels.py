_HOTELS: dict[str, list[dict]] = {
    "tokyo": [
        {
            "name": "Park Hyatt Tokyo",
            "stars": 5,
            "neighborhood": "Shinjuku",
            "price_per_night": 520,
            "amenities": ["spa", "pool", "gym", "restaurant", "bar", "concierge", "city views"],
            "description": "Iconic luxury hotel atop the Shinjuku Park Tower with panoramic city views.",
        },
        {
            "name": "Andaz Tokyo Toranomon Hills",
            "stars": 5,
            "neighborhood": "Toranomon",
            "price_per_night": 450,
            "amenities": ["spa", "gym", "restaurant", "bar", "rooftop terrace"],
            "description": "Stylish hotel with stunning Tokyo Bay views in a modern skyscraper.",
        },
        {
            "name": "Shinjuku Granbell Hotel",
            "stars": 3,
            "neighborhood": "Shinjuku",
            "price_per_night": 160,
            "amenities": ["bar", "restaurant", "gym"],
            "description": "Trendy design hotel in the heart of Shinjuku's entertainment district.",
        },
        {
            "name": "Tokyo Bay Ariake Washington Hotel",
            "stars": 3,
            "neighborhood": "Ariake",
            "price_per_night": 110,
            "amenities": ["restaurant", "gym"],
            "description": "Comfortable business hotel near the waterfront and convention center.",
        },
        {
            "name": "Khaosan Tokyo Kabuki",
            "stars": 2,
            "neighborhood": "Asakusa",
            "price_per_night": 55,
            "amenities": ["shared lounge", "lockers", "luggage storage"],
            "description": "Budget-friendly hostel near Senso-ji Temple in historic Asakusa.",
        },
    ],
    "paris": [
        {
            "name": "Hotel de Crillon",
            "stars": 5,
            "neighborhood": "Place de la Concorde",
            "price_per_night": 1100,
            "amenities": ["spa", "pool", "gym", "restaurant", "bar", "butler service"],
            "description": "Legendary palace hotel on Place de la Concorde, dating back to 1758.",
        },
        {
            "name": "Le Marais Boutique Hotel",
            "stars": 4,
            "neighborhood": "Le Marais",
            "price_per_night": 280,
            "amenities": ["bar", "concierge", "restaurant"],
            "description": "Charming boutique hotel in the fashionable Marais district.",
        },
        {
            "name": "Hotel Ibis Paris Bastille",
            "stars": 3,
            "neighborhood": "Bastille",
            "price_per_night": 120,
            "amenities": ["bar", "24h reception", "wifi"],
            "description": "Modern and comfortable hotel near the famous Place de la Bastille.",
        },
        {
            "name": "Generator Paris",
            "stars": 2,
            "neighborhood": "Canal Saint-Martin",
            "price_per_night": 45,
            "amenities": ["bar", "rooftop terrace", "shared lounge"],
            "description": "Vibrant hostel near Canal Saint-Martin popular with young travelers.",
        },
    ],
    "london": [
        {
            "name": "The Savoy",
            "stars": 5,
            "neighborhood": "Strand",
            "price_per_night": 750,
            "amenities": ["spa", "pool", "gym", "restaurant", "bar", "afternoon tea"],
            "description": "Iconic luxury hotel on the Strand, steeped in history since 1889.",
        },
        {
            "name": "The Hoxton Shoreditch",
            "stars": 4,
            "neighborhood": "Shoreditch",
            "price_per_night": 220,
            "amenities": ["restaurant", "bar", "gym"],
            "description": "Trendy hotel in East London's creative hub with industrial-chic design.",
        },
        {
            "name": "Premier Inn London City",
            "stars": 3,
            "neighborhood": "Tower Hill",
            "price_per_night": 130,
            "amenities": ["restaurant", "bar"],
            "description": "Reliable mid-range hotel near the Tower of London and financial district.",
        },
        {
            "name": "YHA London Central",
            "stars": 2,
            "neighborhood": "Oxford Street",
            "price_per_night": 40,
            "amenities": ["shared kitchen", "bar", "lounge"],
            "description": "Central hostel within walking distance of major London attractions.",
        },
    ],
    "barcelona": [
        {
            "name": "Hotel Arts Barcelona",
            "stars": 5,
            "neighborhood": "Barceloneta",
            "price_per_night": 480,
            "amenities": ["spa", "pool", "gym", "restaurant", "bar", "beach access"],
            "description": "Luxury skyscraper hotel on the beachfront with incredible Mediterranean views.",
        },
        {
            "name": "Praktik Rambla",
            "stars": 4,
            "neighborhood": "Las Ramblas",
            "price_per_night": 195,
            "amenities": ["rooftop terrace", "bar", "gym"],
            "description": "Boutique hotel on the famous Las Ramblas boulevard.",
        },
        {
            "name": "Hotel Catalonia Diagonal",
            "stars": 3,
            "neighborhood": "Diagonal",
            "price_per_night": 110,
            "amenities": ["pool", "restaurant", "gym"],
            "description": "Modern hotel in the Diagonal business district with rooftop pool.",
        },
        {
            "name": "Barcelona Central Garden Hostel",
            "stars": 2,
            "neighborhood": "El Raval",
            "price_per_night": 35,
            "amenities": ["garden", "bar", "shared kitchen"],
            "description": "Friendly hostel with a beautiful garden patio in central Barcelona.",
        },
    ],
    "bali": [
        {
            "name": "Four Seasons Resort Bali at Jimbaran Bay",
            "stars": 5,
            "neighborhood": "Jimbaran",
            "price_per_night": 900,
            "amenities": ["private pool", "spa", "gym", "restaurant", "bar", "beach access"],
            "description": "Ultra-luxury resort of private villas cascading down to Jimbaran Bay.",
        },
        {
            "name": "Alaya Resort Ubud",
            "stars": 5,
            "neighborhood": "Ubud",
            "price_per_night": 320,
            "amenities": ["infinity pool", "spa", "yoga", "restaurant", "cooking class"],
            "description": "Serene luxury retreat surrounded by tropical jungle in cultural Ubud.",
        },
        {
            "name": "Seminyak Square Hotel",
            "stars": 3,
            "neighborhood": "Seminyak",
            "price_per_night": 95,
            "amenities": ["pool", "restaurant", "bar"],
            "description": "Well-located hotel in the heart of Seminyak's shopping and dining area.",
        },
        {
            "name": "Padi Bali Hostel",
            "stars": 2,
            "neighborhood": "Kuta",
            "price_per_night": 18,
            "amenities": ["pool", "bar", "shared kitchen"],
            "description": "Lively budget hostel in Kuta, popular with surfers and backpackers.",
        },
    ],
    "sydney": [
        {
            "name": "Park Hyatt Sydney",
            "stars": 5,
            "neighborhood": "The Rocks",
            "price_per_night": 680,
            "amenities": ["spa", "pool", "gym", "restaurant", "bar", "Opera House views"],
            "description": "Iconic harbour-front hotel with unmatched views of the Opera House.",
        },
        {
            "name": "QT Sydney",
            "stars": 5,
            "neighborhood": "CBD",
            "price_per_night": 350,
            "amenities": ["gym", "spa", "restaurant", "rooftop bar"],
            "description": "Fashionable boutique hotel housed in a heritage building in the CBD.",
        },
        {
            "name": "Meriton Suites Sussex Street",
            "stars": 4,
            "neighborhood": "Darling Harbour",
            "price_per_night": 185,
            "amenities": ["pool", "gym", "self-catering kitchenette"],
            "description": "Spacious apartment-style suites near Darling Harbour.",
        },
        {
            "name": "Wake Up! Sydney",
            "stars": 2,
            "neighborhood": "Chinatown",
            "price_per_night": 38,
            "amenities": ["bar", "shared kitchen", "social events"],
            "description": "Award-winning hostel in Chinatown, minutes from Central Station.",
        },
    ],
    "rome": [
        {
            "name": "Hotel de Russie",
            "stars": 5,
            "neighborhood": "Piazza del Popolo",
            "price_per_night": 720,
            "amenities": ["spa", "pool", "gym", "restaurant", "bar", "garden"],
            "description": "Refined luxury hotel near Piazza del Popolo with a magical terraced garden.",
        },
        {
            "name": "Hotel Artemide",
            "stars": 4,
            "neighborhood": "Via Nazionale",
            "price_per_night": 200,
            "amenities": ["spa", "gym", "restaurant", "bar"],
            "description": "Elegant Art Nouveau hotel on Via Nazionale near Termini station.",
        },
        {
            "name": "Hotel Navona",
            "stars": 3,
            "neighborhood": "Piazza Navona",
            "price_per_night": 120,
            "amenities": ["bar", "concierge"],
            "description": "Charming hotel steps from the magnificent Piazza Navona.",
        },
        {
            "name": "The Beehive Hostel",
            "stars": 2,
            "neighborhood": "Termini",
            "price_per_night": 30,
            "amenities": ["garden cafe", "shared kitchen"],
            "description": "Well-loved eco-friendly hostel near Termini station.",
        },
    ],
    "amsterdam": [
        {
            "name": "Waldorf Astoria Amsterdam",
            "stars": 5,
            "neighborhood": "Canal Ring",
            "price_per_night": 650,
            "amenities": ["spa", "pool", "gym", "restaurant", "bar", "canal views"],
            "description": "Grand luxury hotel in six connected 17th-century canal houses.",
        },
        {
            "name": "Hotel V Nesplein",
            "stars": 4,
            "neighborhood": "City Centre",
            "price_per_night": 210,
            "amenities": ["bar", "restaurant", "terrace"],
            "description": "Design hotel in the city centre with a lively social atmosphere.",
        },
        {
            "name": "Hotel Brouwer",
            "stars": 3,
            "neighborhood": "Singel Canal",
            "price_per_night": 130,
            "amenities": ["canal views", "breakfast included"],
            "description": "Cosy family-run hotel on the famous Singel canal since 1917.",
        },
        {
            "name": "Flying Pig Downtown Hostel",
            "stars": 2,
            "neighborhood": "Nieuwmarkt",
            "price_per_night": 35,
            "amenities": ["bar", "lounge", "lockers"],
            "description": "One of Amsterdam's most famous hostels, open since 1983.",
        },
    ],
    "dubai": [
        {
            "name": "Burj Al Arab Jumeirah",
            "stars": 5,
            "neighborhood": "Jumeirah Beach",
            "price_per_night": 2500,
            "amenities": ["private beach", "pool", "spa", "helipad", "butler service", "michelin restaurants"],
            "description": "The world's most iconic hotel, shaped like a sail on its own island.",
        },
        {
            "name": "Atlantis The Palm",
            "stars": 5,
            "neighborhood": "Palm Jumeirah",
            "price_per_night": 480,
            "amenities": ["waterpark", "private beach", "spa", "multiple pools", "casino"],
            "description": "Mega-resort on the Palm with an attached waterpark and aquarium.",
        },
        {
            "name": "Premier Inn Dubai International Airport",
            "stars": 3,
            "neighborhood": "Deira",
            "price_per_night": 95,
            "amenities": ["pool", "gym", "restaurant"],
            "description": "Comfortable and affordable hotel with easy airport access.",
        },
    ],
}


def _normalize(city: str) -> str:
    return city.strip().lower()


def query_hotels(
    destination: str,
    check_in: str,
    check_out: str,
    guests: int,
    max_price: float | None,
) -> list[dict]:
    from datetime import datetime

    city = _normalize(destination)
    hotels = _HOTELS.get(city, [])

    if not hotels:
        for key in _HOTELS:
            if key in city or city in key:
                hotels = _HOTELS[key]
                break

    try:
        nights = (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
        if nights <= 0:
            nights = 1
    except ValueError:
        nights = 1

    results = []
    for hotel in hotels:
        if max_price and hotel["price_per_night"] > max_price:
            continue
        results.append({
            **hotel,
            "check_in": check_in,
            "check_out": check_out,
            "nights": nights,
            "guests": guests,
            "total_price": hotel["price_per_night"] * nights,
            "currency": "USD",
        })

    return sorted(results, key=lambda x: x["price_per_night"])
