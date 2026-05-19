_POI: dict[str, dict[str, list[dict]]] = {
    "tokyo": {
        "attractions": [
            {"name": "Senso-ji Temple", "address": "2-3-1 Asakusa, Taito City", "rating": 4.7, "estimated_cost": 0, "description": "Tokyo's oldest and most significant Buddhist temple, dating to 645 AD."},
            {"name": "Shinjuku Gyoen National Garden", "address": "11 Naito-cho, Shinjuku City", "rating": 4.6, "estimated_cost": 5, "description": "Stunning 144-acre garden combining Japanese, French, and English landscape styles."},
            {"name": "teamLab Planets", "address": "6-1-16 Toyosu, Koto City", "rating": 4.8, "estimated_cost": 32, "description": "Immersive digital art museum where you walk through water and light installations."},
            {"name": "Tokyo Skytree", "address": "1-1-2 Oshiage, Sumida City", "rating": 4.5, "estimated_cost": 22, "description": "Japan's tallest structure with observation decks offering panoramic city views."},
            {"name": "Meiji Shrine", "address": "1-1 Yoyogikamizonocho, Shibuya City", "rating": 4.6, "estimated_cost": 0, "description": "Serene Shinto shrine set in a forested area dedicated to Emperor Meiji."},
            {"name": "Shibuya Crossing", "address": "Shibuya Station, Shibuya City", "rating": 4.5, "estimated_cost": 0, "description": "The world's busiest pedestrian crossing — a true Tokyo icon."},
        ],
        "restaurants": [
            {"name": "Sukiyabashi Jiro Honten", "address": "4-2-15 Ginza, Chuo City", "rating": 4.9, "estimated_cost": 300, "description": "Three Michelin-starred sushi restaurant featured in Jiro Dreams of Sushi."},
            {"name": "Ichiran Shibuya", "address": "1-22-7 Jinnan, Shibuya City", "rating": 4.4, "estimated_cost": 15, "description": "Famous solo-booth ramen chain known for its rich tonkotsu broth."},
            {"name": "Gonpachi Nishi-Azabu", "address": "1-13-11 Nishi-Azabu, Minato City", "rating": 4.3, "estimated_cost": 35, "description": "Traditional Japanese tavern-style restaurant that inspired the Kill Bill movie set."},
            {"name": "Tsukiji Outer Market", "address": "4-16-2 Tsukiji, Chuo City", "rating": 4.5, "estimated_cost": 20, "description": "Historic fish market area with dozens of sushi and seafood stalls."},
            {"name": "Torikizoku", "address": "Various locations", "rating": 4.3, "estimated_cost": 12, "description": "Beloved yakitori chain with every skewer priced at just ¥330."},
        ],
        "activities": [
            {"name": "Sumo Tournament at Ryogoku Kokugikan", "address": "1-3-28 Yokoami, Sumida City", "rating": 4.8, "estimated_cost": 50, "description": "Watch Japan's ancient sport live at the country's premier sumo arena (seasonal)."},
            {"name": "Cooking Class: Sushi & Tempura", "address": "Shinjuku, Tokyo", "rating": 4.7, "estimated_cost": 85, "description": "Hands-on Japanese cooking class learning to make sushi, tempura, and miso soup."},
            {"name": "Day Trip to Mt. Fuji & Hakone", "address": "Hakone, Kanagawa", "rating": 4.8, "estimated_cost": 120, "description": "Full-day guided tour to Mt. Fuji's 5th Station and Hakone's hot springs."},
            {"name": "Tokyo Bay Cruise", "address": "Hinode Pier, Minato City", "rating": 4.3, "estimated_cost": 18, "description": "Scenic evening cruise around Tokyo Bay with views of the Rainbow Bridge."},
            {"name": "Anime Pilgrimage in Akihabara", "address": "Akihabara, Chiyoda City", "rating": 4.5, "estimated_cost": 0, "description": "Explore Tokyo's electronics and anime district packed with manga shops and arcades."},
        ],
        "nightlife": [
            {"name": "New York Bar (Park Hyatt)", "address": "3-7-1-2 Nishi-Shinjuku, Shinjuku", "rating": 4.6, "estimated_cost": 40, "description": "Iconic jazz bar on the 52nd floor made famous by Lost in Translation."},
            {"name": "Womb Club", "address": "2-16 Maruyama-cho, Shibuya City", "rating": 4.3, "estimated_cost": 25, "description": "One of Tokyo's most legendary techno and electronic music clubs."},
            {"name": "Golden Gai", "address": "1-1-6 Kabukicho, Shinjuku City", "rating": 4.5, "estimated_cost": 20, "description": "Maze of over 200 tiny themed bars in Shinjuku — a must-visit for bar-hopping."},
            {"name": "Omoide Yokocho (Memory Lane)", "address": "1-2 Nishishinjuku, Shinjuku City", "rating": 4.5, "estimated_cost": 18, "description": "Atmospheric alley of tiny yakitori izakayas steaming with grilled skewers."},
        ],
        "shopping": [
            {"name": "Takeshita Street, Harajuku", "address": "Takeshita St, Harajuku, Shibuya", "rating": 4.4, "estimated_cost": 50, "description": "Eccentric fashion street with quirky boutiques, crepe stalls, and kawaii culture."},
            {"name": "Shibuya 109", "address": "2-29-1 Dogenzaka, Shibuya City", "rating": 4.3, "estimated_cost": 80, "description": "Iconic 10-story fashion mall packed with trendy Japanese clothing brands."},
            {"name": "Tsukiji Fish Market (Outer)", "address": "4-16 Tsukiji, Chuo City", "rating": 4.5, "estimated_cost": 30, "description": "Browse the freshest seafood, Japanese knives, and kitchen goods."},
            {"name": "Akihabara Electronics District", "address": "Akihabara, Chiyoda City", "rating": 4.4, "estimated_cost": 100, "description": "Tokyo's tech mecca — ideal for cameras, electronics, and anime merchandise."},
        ],
        "transport": [
            {"name": "IC Card (Suica or Pasmo)", "address": "Any JR station", "rating": 4.9, "estimated_cost": 15, "description": "Rechargeable smart card for all trains, subways, and buses in greater Tokyo."},
            {"name": "Tokyo Metro Day Pass", "address": "Tokyo Metro stations", "rating": 4.7, "estimated_cost": 10, "description": "Unlimited rides on Tokyo Metro lines for one day — great value for sightseers."},
            {"name": "JR Pass (7-day)", "address": "JR offices at major stations", "rating": 4.8, "estimated_cost": 280, "description": "Unlimited JR trains including Shinkansen across Japan — essential for multi-city trips."},
        ],
    },
    "paris": {
        "attractions": [
            {"name": "Eiffel Tower", "address": "Champ de Mars, 5 Av. Anatole France", "rating": 4.7, "estimated_cost": 28, "description": "Paris's iron lattice icon offering stunning city views from three levels."},
            {"name": "Louvre Museum", "address": "Rue de Rivoli, 75001 Paris", "rating": 4.8, "estimated_cost": 17, "description": "The world's largest art museum, home to the Mona Lisa and over 380,000 objects."},
            {"name": "Palace of Versailles", "address": "Place d'Armes, 78000 Versailles", "rating": 4.7, "estimated_cost": 20, "description": "Opulent royal palace with magnificent Hall of Mirrors and vast formal gardens."},
            {"name": "Musée d'Orsay", "address": "1 Rue de la Légion d'Honneur", "rating": 4.8, "estimated_cost": 16, "description": "Impressionist art museum in a converted railway station with works by Monet and Van Gogh."},
            {"name": "Notre-Dame Cathedral", "address": "6 Parvis Notre-Dame, Île de la Cité", "rating": 4.7, "estimated_cost": 0, "description": "Iconic Gothic cathedral currently undergoing restoration after the 2019 fire."},
            {"name": "Sacré-Cœur Basilica", "address": "35 Rue du Chevalier de la Barre, Montmartre", "rating": 4.7, "estimated_cost": 0, "description": "White-domed basilica atop Montmartre hill with sweeping Paris panoramas."},
        ],
        "restaurants": [
            {"name": "Le Jules Verne", "address": "Eiffel Tower, Champ de Mars", "rating": 4.5, "estimated_cost": 180, "description": "Michelin-starred restaurant on the second floor of the Eiffel Tower."},
            {"name": "L'As du Fallafel", "address": "34 Rue des Rosiers, Le Marais", "rating": 4.5, "estimated_cost": 8, "description": "Legendary falafel spot in the Marais Jewish Quarter — perpetually queued."},
            {"name": "Café de Flore", "address": "172 Bd Saint-Germain, Saint-Germain-des-Prés", "rating": 4.3, "estimated_cost": 25, "description": "Iconic Left Bank café where Sartre and Simone de Beauvoir once held court."},
            {"name": "Bouillon Chartier", "address": "7 Rue du Faubourg Montmartre", "rating": 4.4, "estimated_cost": 20, "description": "Historic 1896 brasserie serving classic French cuisine at extremely affordable prices."},
            {"name": "Septime", "address": "80 Rue de Charonne, Bastille", "rating": 4.7, "estimated_cost": 95, "description": "Celebrated neo-bistro with market-driven tasting menus; book well in advance."},
        ],
        "activities": [
            {"name": "Seine River Cruise (Bateaux Mouches)", "address": "Port de la Conférence, Pont de l'Alma", "rating": 4.5, "estimated_cost": 17, "description": "Classic 1-hour boat tour passing all of Paris's major monuments from the river."},
            {"name": "Wine & Cheese Tasting", "address": "Various wine bars, Saint-Germain", "rating": 4.7, "estimated_cost": 50, "description": "Guided tasting of French wines paired with artisanal cheeses and charcuterie."},
            {"name": "Montmartre Art Walking Tour", "address": "Place du Tertre, Montmartre", "rating": 4.6, "estimated_cost": 20, "description": "Guided walk through bohemian Montmartre's artist studios and hidden stairways."},
            {"name": "Cooking Class: Croissants & Macarons", "address": "Le Cordon Bleu, 13 Quai André Citroën", "rating": 4.8, "estimated_cost": 110, "description": "Half-day pastry class at the world-famous culinary school."},
        ],
        "nightlife": [
            {"name": "Moulin Rouge", "address": "82 Bd de Clichy, Pigalle", "rating": 4.5, "estimated_cost": 115, "description": "The original cabaret show combining dance, acrobatics, and spectacular costumes."},
            {"name": "Le Baron", "address": "6 Av. de Marigny, Champs-Élysées", "rating": 4.2, "estimated_cost": 30, "description": "Intimate, celebrity-loved nightclub in the 8th arrondissement."},
            {"name": "Barrio Latino", "address": "46-48 Rue du Faubourg Saint-Antoine", "rating": 4.2, "estimated_cost": 25, "description": "Multi-floor Latin music bar in a stunning Gustave Eiffel-designed building."},
            {"name": "Le Comptoir Général", "address": "80 Quai de Jemmapes, Canal Saint-Martin", "rating": 4.4, "estimated_cost": 15, "description": "Eclectic bar and cultural space in a converted 19th-century coach house."},
        ],
        "shopping": [
            {"name": "Galeries Lafayette", "address": "40 Bd Haussmann, Opéra", "rating": 4.5, "estimated_cost": 150, "description": "Paris's most iconic department store under a spectacular Art Nouveau glass dome."},
            {"name": "Marché aux Puces de Saint-Ouen", "address": "Rue des Rosiers, Saint-Ouen", "rating": 4.4, "estimated_cost": 30, "description": "Europe's largest flea market with antiques, vintage fashion, and curiosities."},
            {"name": "Le Marais boutiques", "address": "Rue des Francs Bourgeois, Le Marais", "rating": 4.5, "estimated_cost": 80, "description": "Stylish shopping street lined with designer boutiques, galleries, and concept stores."},
        ],
        "transport": [
            {"name": "Paris Visite Pass (2 days)", "address": "Major Metro/RER stations", "rating": 4.6, "estimated_cost": 24, "description": "Unlimited Metro, RER, and bus travel within Paris zones 1–3."},
            {"name": "Vélib' Bike Share", "address": "Vélib' stations across the city", "rating": 4.4, "estimated_cost": 5, "description": "Paris's public bike-sharing system — perfect for cycling along the Seine."},
        ],
    },
    "london": {
        "attractions": [
            {"name": "British Museum", "address": "Great Russell St, Bloomsbury", "rating": 4.7, "estimated_cost": 0, "description": "World-class museum housing 8 million artifacts including the Rosetta Stone."},
            {"name": "Tower of London", "address": "Tower Hill, London EC3N 4AB", "rating": 4.6, "estimated_cost": 32, "description": "Historic castle on the Thames housing the Crown Jewels and centuries of history."},
            {"name": "Tate Modern", "address": "Bankside, London SE1 9TG", "rating": 4.5, "estimated_cost": 0, "description": "World-renowned modern art museum in a converted Bankside Power Station."},
            {"name": "Buckingham Palace", "address": "London SW1A 1AA", "rating": 4.4, "estimated_cost": 0, "description": "The official London residence of the monarch — catch the Changing of the Guard."},
            {"name": "The Shard", "address": "32 London Bridge St, SE1 9SG", "rating": 4.4, "estimated_cost": 32, "description": "Western Europe's tallest building with a 360° viewing platform on level 72."},
        ],
        "restaurants": [
            {"name": "Dishoom Shoreditch", "address": "7 Boundary St, Shoreditch", "rating": 4.7, "estimated_cost": 30, "description": "Celebrated Bombay-style café with legendary black daal and keema pau."},
            {"name": "St. John Restaurant", "address": "26 St John St, Clerkenwell", "rating": 4.5, "estimated_cost": 60, "description": "Fergus Henderson's iconic nose-to-tail eating institution in a former smokehouse."},
            {"name": "Borough Market", "address": "8 Southwark St, SE1 1TL", "rating": 4.7, "estimated_cost": 15, "description": "London's oldest and most renowned food market — brilliant for lunch grazing."},
            {"name": "Bao Soho", "address": "53 Lexington St, Soho", "rating": 4.5, "estimated_cost": 25, "description": "Taiwanese bao buns and small plates in a minimalist space — perpetually queued."},
        ],
        "activities": [
            {"name": "Thames River Cruise", "address": "Westminster Pier, Victoria Embankment", "rating": 4.4, "estimated_cost": 18, "description": "Scenic boat ride past Tower Bridge, the Globe Theatre, and Greenwich."},
            {"name": "Harry Potter Studio Tour", "address": "Studio Tour Drive, Leavesden, Hertfordshire", "rating": 4.9, "estimated_cost": 55, "description": "Behind-the-scenes tour of authentic sets, costumes, and props from the films."},
            {"name": "West End Musical", "address": "Theatre District, West End", "rating": 4.8, "estimated_cost": 75, "description": "Catch a world-class show in the heart of London's theatre district."},
            {"name": "Jack the Ripper Walking Tour", "address": "Aldgate East Station, E1", "rating": 4.4, "estimated_cost": 15, "description": "Evening guided walk through Victorian Whitechapel's atmospheric East End."},
        ],
        "nightlife": [
            {"name": "Ronnie Scott's Jazz Club", "address": "47 Frith St, Soho", "rating": 4.7, "estimated_cost": 35, "description": "Legendary jazz venue open since 1959, hosting world-class musicians nightly."},
            {"name": "Fabric", "address": "77a Charterhouse St, Clerkenwell", "rating": 4.5, "estimated_cost": 25, "description": "World-famous nightclub with three floors of house, techno, and drum & bass."},
            {"name": "Sketch Bar", "address": "9 Conduit St, Mayfair", "rating": 4.4, "estimated_cost": 30, "description": "Surrealist bar and gallery space with eccentric egg-pod toilets and cocktails."},
        ],
        "shopping": [
            {"name": "Oxford Street", "address": "Oxford St, London W1", "rating": 4.2, "estimated_cost": 100, "description": "Europe's busiest shopping street with flagship stores of every major brand."},
            {"name": "Portobello Road Market", "address": "Portobello Rd, Notting Hill", "rating": 4.5, "estimated_cost": 40, "description": "Famous antique and vintage market in colourful Notting Hill — best on Saturdays."},
            {"name": "Covent Garden", "address": "Covent Garden, WC2E 8RF", "rating": 4.5, "estimated_cost": 60, "description": "Vibrant shopping and entertainment piazza with street performers and boutiques."},
        ],
        "transport": [
            {"name": "Oyster Card", "address": "Any Tube, bus, or rail station", "rating": 4.8, "estimated_cost": 10, "description": "Contactless smartcard for all TfL modes — always cheaper than paper tickets."},
            {"name": "London Day Travelcard", "address": "Tube/Rail stations", "rating": 4.5, "estimated_cost": 15, "description": "Unlimited off-peak travel within zones 1–2 on Tube, bus, DLR, and Overground."},
        ],
    },
    "barcelona": {
        "attractions": [
            {"name": "Sagrada Família", "address": "Carrer de Mallorca, 401", "rating": 4.8, "estimated_cost": 26, "description": "Gaudí's unfinished masterpiece — the world's most visited unfinished building."},
            {"name": "Park Güell", "address": "08024 Barcelona", "rating": 4.6, "estimated_cost": 10, "description": "Fantastical hilltop park filled with Gaudí's mosaic sculptures and terraces."},
            {"name": "Casa Batlló", "address": "Passeig de Gràcia, 43", "rating": 4.7, "estimated_cost": 35, "description": "Gaudí's surreal masterpiece on the famous Block of Discord in the Eixample."},
            {"name": "Gothic Quarter", "address": "Barri Gòtic, Barcelona", "rating": 4.6, "estimated_cost": 0, "description": "Labyrinthine medieval neighborhood with Roman ruins and Gothic architecture."},
            {"name": "Picasso Museum", "address": "Carrer Montcada, 15-23, El Born", "rating": 4.5, "estimated_cost": 14, "description": "Impressive collection of Picasso's early works in five connected medieval palaces."},
        ],
        "restaurants": [
            {"name": "La Boqueria Market", "address": "La Rambla, 91", "rating": 4.4, "estimated_cost": 15, "description": "Barcelona's legendary market overflowing with fresh produce, jamón, and seafood."},
            {"name": "El Xampanyet", "address": "Carrer de Montcada, 22, El Born", "rating": 4.5, "estimated_cost": 20, "description": "Classic cava bar serving house-made sparkling wine and excellent tapas."},
            {"name": "Quimet & Quimet", "address": "Carrer del Poeta Cabanyes, 25, Poble Sec", "rating": 4.6, "estimated_cost": 18, "description": "Legendary standing-room-only bodega famous for its creative montaditos."},
            {"name": "Tickets", "address": "Avinguda del Paral·lel, 164, Sant Antoni", "rating": 4.7, "estimated_cost": 80, "description": "Albert Adrià's playful tapas bar — Barcelona's most creative dining experience."},
        ],
        "activities": [
            {"name": "Flamenco Show at Palau Dalmases", "address": "Carrer de Montcada, 20, El Born", "rating": 4.5, "estimated_cost": 25, "description": "Passionate flamenco performance in a stunning 17th-century baroque palace."},
            {"name": "Barceloneta Beach", "address": "Barceloneta, Barcelona", "rating": 4.4, "estimated_cost": 0, "description": "The city's most popular urban beach — swim, sunbathe, or play beach volleyball."},
            {"name": "Day Trip to Montserrat", "address": "Montserrat, Barcelona Province", "rating": 4.8, "estimated_cost": 30, "description": "Awe-inspiring mountain monastery with dramatic serrated peaks and hiking trails."},
            {"name": "Cooking Class: Paella & Tapas", "address": "El Born, Barcelona", "rating": 4.7, "estimated_cost": 75, "description": "Learn to cook authentic paella and classic tapas with a professional chef."},
        ],
        "nightlife": [
            {"name": "Razzmatazz", "address": "Carrer dels Almogàvers, 122, Poblenou", "rating": 4.4, "estimated_cost": 20, "description": "Five-room club in a warehouse spanning everything from indie rock to techno."},
            {"name": "Bar Marsella", "address": "Carrer de Sant Pau, 65, Raval", "rating": 4.5, "estimated_cost": 15, "description": "Barcelona's oldest bar (since 1820), still serving absinthe amid antique clutter."},
            {"name": "Opium Barcelona", "address": "Passeig Marítim de la Barceloneta, 34", "rating": 4.2, "estimated_cost": 25, "description": "Beach club and nightclub with sea views and international DJs."},
        ],
        "shopping": [
            {"name": "Passeig de Gràcia", "address": "Passeig de Gràcia, Eixample", "rating": 4.5, "estimated_cost": 100, "description": "Barcelona's most elegant boulevard lined with luxury boutiques and Gaudí architecture."},
            {"name": "El Born district boutiques", "address": "El Born, Barcelona", "rating": 4.5, "estimated_cost": 60, "description": "Trendy boutiques, independent designers, and vintage shops in a charming medieval area."},
        ],
        "transport": [
            {"name": "T-Casual (10-trip Metro card)", "address": "Metro stations", "rating": 4.7, "estimated_cost": 12, "description": "10-journey card valid on Metro, buses, and trams — shareable among groups."},
            {"name": "Barcelona Card (3 days)", "address": "Tourist offices", "rating": 4.4, "estimated_cost": 45, "description": "Unlimited public transport plus free/discounted entry to major attractions."},
        ],
    },
    "bali": {
        "attractions": [
            {"name": "Tanah Lot Temple", "address": "Beraban, Kediri, Tabanan Regency", "rating": 4.6, "estimated_cost": 5, "description": "Spectacular Hindu sea temple perched on a rocky outcrop, especially magical at sunset."},
            {"name": "Ubud Monkey Forest", "address": "Jl. Monkey Forest, Padangtegal, Ubud", "rating": 4.5, "estimated_cost": 5, "description": "Natural sanctuary home to 700+ Balinese macaques among ancient temple ruins."},
            {"name": "Tegallalang Rice Terraces", "address": "Tegallalang, Gianyar Regency", "rating": 4.6, "estimated_cost": 3, "description": "UNESCO-listed cascading rice paddies — an iconic symbol of Balinese culture."},
            {"name": "Uluwatu Temple", "address": "Pecatu, South Kuta, Badung Regency", "rating": 4.7, "estimated_cost": 3, "description": "Clifftop sea temple at the southern tip of Bali with nightly Kecak fire dance."},
            {"name": "Mount Batur Sunrise Trek", "address": "Kintamani, Bangli Regency", "rating": 4.8, "estimated_cost": 45, "description": "Pre-dawn hike to an active volcano's summit for a breathtaking sunrise view."},
        ],
        "restaurants": [
            {"name": "Locavore", "address": "Jl. Dewisita No.10, Ubud", "rating": 4.7, "estimated_cost": 80, "description": "Asia's Best Restaurant 2017 — hyper-local tasting menus celebrating Indonesian ingredients."},
            {"name": "Warung Babi Guling Ibu Oka", "address": "Jl. Tegal Sari No.2, Ubud", "rating": 4.5, "estimated_cost": 5, "description": "Famous warung serving Bali's iconic suckling pig — a must-try local institution."},
            {"name": "La Lucciola", "address": "Jl. Petitenget No.Beach, Seminyak", "rating": 4.4, "estimated_cost": 30, "description": "Romantic beachfront Italian restaurant with stunning sunset views."},
            {"name": "Naughty Nuri's", "address": "Jl. Raya Sanggingan, Ubud", "rating": 4.4, "estimated_cost": 12, "description": "Legendary ribs shack beloved by locals and travellers since 1995."},
        ],
        "activities": [
            {"name": "White Water Rafting on Ayung River", "address": "Ayung River, Ubud", "rating": 4.6, "estimated_cost": 35, "description": "Thrilling 2-hour rafting through lush jungle gorges and rice paddy valleys."},
            {"name": "Traditional Balinese Healing (Balian)", "address": "Ubud area", "rating": 4.5, "estimated_cost": 30, "description": "Authentic healing session with a traditional Balinese medicine man."},
            {"name": "Surf Lesson in Kuta", "address": "Kuta Beach, Badung Regency", "rating": 4.4, "estimated_cost": 25, "description": "2-hour beginner surf lesson with experienced local instructors on Kuta's famous waves."},
            {"name": "Cooking Class in Ubud", "address": "Ubud, Gianyar Regency", "rating": 4.8, "estimated_cost": 40, "description": "Morning market visit followed by a hands-on Balinese cooking class."},
        ],
        "nightlife": [
            {"name": "Ku De Ta", "address": "Jl. Kayu Aya No.9, Seminyak", "rating": 4.3, "estimated_cost": 25, "description": "Bali's most famous beach club — sundowners here are a rite of passage."},
            {"name": "Potato Head Beach Club", "address": "Jl. Petitenget No.51B, Seminyak", "rating": 4.4, "estimated_cost": 30, "description": "Stunning amphitheatre-style beach club with a famous infinity pool."},
            {"name": "Sky Garden Rooftop Club", "address": "Jl. Legian No.61, Kuta", "rating": 4.2, "estimated_cost": 15, "description": "Multi-level rooftop venue in Kuta, popular with backpackers and party-goers."},
        ],
        "shopping": [
            {"name": "Ubud Art Market", "address": "Jl. Raya Ubud, Ubud", "rating": 4.3, "estimated_cost": 20, "description": "Vibrant market selling Balinese handicrafts, textiles, wood carvings, and silver."},
            {"name": "Seminyak Square", "address": "Jl. Raya Seminyak, Seminyak", "rating": 4.2, "estimated_cost": 50, "description": "Upscale open-air mall with designer boutiques, spas, and trendy cafes."},
        ],
        "transport": [
            {"name": "GoJek or Grab (ride-hailing)", "address": "Island-wide", "rating": 4.7, "estimated_cost": 3, "description": "The easiest and cheapest way to get around Bali — always use the app for fair pricing."},
            {"name": "Scooter Rental", "address": "Most tourist areas", "rating": 4.4, "estimated_cost": 7, "description": "Rent a scooter for the day to explore Bali at your own pace (per day, with helmet)."},
        ],
    },
    "sydney": {
        "attractions": [
            {"name": "Sydney Opera House", "address": "Bennelong Point, Sydney NSW 2000", "rating": 4.7, "estimated_cost": 0, "description": "UNESCO-listed masterpiece — tour the interior or catch a world-class performance."},
            {"name": "Sydney Harbour Bridge Climb", "address": "3 Cumberland St, The Rocks", "rating": 4.9, "estimated_cost": 175, "description": "Exhilarating guided climb to the summit of the iconic coat-hanger bridge."},
            {"name": "Bondi Beach", "address": "Queen Elizabeth Drive, Bondi Beach", "rating": 4.7, "estimated_cost": 0, "description": "Australia's most famous beach — surf, swim, or walk the stunning coastal trail."},
            {"name": "Taronga Zoo", "address": "Bradleys Head Rd, Mosman", "rating": 4.6, "estimated_cost": 47, "description": "World-class zoo with 4,000 native and exotic animals overlooking Sydney Harbour."},
            {"name": "Royal Botanic Garden", "address": "Mrs Macquaries Rd, Sydney", "rating": 4.7, "estimated_cost": 0, "description": "Beautiful 74-acre harbour-front garden with sweeping views of the Opera House."},
        ],
        "restaurants": [
            {"name": "Quay Restaurant", "address": "Upper Level, Overseas Passenger Terminal", "rating": 4.7, "estimated_cost": 200, "description": "One of Australia's finest restaurants with harbour views and exceptional modern cuisine."},
            {"name": "Icebergs Dining Room", "address": "1 Notts Ave, Bondi Beach", "rating": 4.5, "estimated_cost": 80, "description": "Iconic oceanfront restaurant above the famous Bondi Icebergs Pool."},
            {"name": "The Rocks Markets", "address": "George St, The Rocks", "rating": 4.4, "estimated_cost": 15, "description": "Weekend market with artisan food stalls serving gourmet street food."},
            {"name": "Momofuku Seiobo", "address": "Star Casino, 80 Pyrmont St", "rating": 4.6, "estimated_cost": 250, "description": "David Chang's flagship Sydney restaurant with a renowned chef's tasting menu."},
        ],
        "activities": [
            {"name": "Bondi to Coogee Coastal Walk", "address": "Starts at Bondi Beach, ends Coogee Beach", "rating": 4.8, "estimated_cost": 0, "description": "Stunning 6km clifftop walk past tidal pools, parks, and ocean vistas."},
            {"name": "Blue Mountains Day Trip", "address": "Katoomba, Blue Mountains NSW", "rating": 4.8, "estimated_cost": 45, "description": "Day trip to see the Three Sisters rock formation and cascading waterfalls."},
            {"name": "Sydney Harbour Ferry Tour", "address": "Circular Quay, Sydney", "rating": 4.6, "estimated_cost": 10, "description": "Scenic ferry ride to Manly — best way to see the harbour's iconic landmarks."},
            {"name": "Learn to Surf at Manly", "address": "Manly Beach, Sydney", "rating": 4.5, "estimated_cost": 60, "description": "2-hour surf lesson on one of Sydney's most beautiful northern beaches."},
        ],
        "nightlife": [
            {"name": "The Ivy", "address": "330 George St, CBD", "rating": 4.3, "estimated_cost": 30, "description": "Sydney's most glamorous multi-venue complex with rooftop pool and multiple bars."},
            {"name": "Shady Pines Saloon", "address": "4 Darlinghurst Rd, Darlinghurst", "rating": 4.4, "estimated_cost": 20, "description": "Beloved dive bar with a Tennessee honky-tonk theme serving excellent whisky."},
            {"name": "Stonewall Hotel", "address": "175 Oxford St, Darlinghurst", "rating": 4.3, "estimated_cost": 15, "description": "Sydney's iconic LGBTQ+ venue on Oxford Street with multiple floors of entertainment."},
        ],
        "shopping": [
            {"name": "Queen Victoria Building (QVB)", "address": "455 George St, CBD", "rating": 4.7, "estimated_cost": 80, "description": "Stunning Victorian-era building housing 200 specialty boutiques across five levels."},
            {"name": "Paddington Markets", "address": "395 Oxford St, Paddington", "rating": 4.4, "estimated_cost": 40, "description": "Saturday market showcasing local designers, artisans, and handmade goods."},
        ],
        "transport": [
            {"name": "Opal Card", "address": "Train/bus/ferry stations and retailers", "rating": 4.7, "estimated_cost": 10, "description": "Reloadable card for trains, buses, ferries, and light rail across Sydney."},
            {"name": "Sydney Ferries", "address": "Circular Quay, Sydney", "rating": 4.8, "estimated_cost": 4, "description": "Scenic public ferries across the harbour — cheap and with incredible views."},
        ],
    },
    "rome": {
        "attractions": [
            {"name": "Colosseum", "address": "Piazza del Colosseo, 1", "rating": 4.8, "estimated_cost": 18, "description": "The world's largest ancient amphitheatre — once held 80,000 spectators for gladiatorial combat."},
            {"name": "Vatican Museums & Sistine Chapel", "address": "Viale Vaticano, Vatican City", "rating": 4.8, "estimated_cost": 20, "description": "Vast collection culminating in Michelangelo's breathtaking Sistine Chapel ceiling."},
            {"name": "Trevi Fountain", "address": "Piazza di Trevi, 00187 Roma", "rating": 4.7, "estimated_cost": 0, "description": "Rome's most spectacular baroque fountain — toss a coin to ensure your return."},
            {"name": "Roman Forum", "address": "Via Sacra, 00186 Roma", "rating": 4.7, "estimated_cost": 12, "description": "The heart of ancient Rome — ruins of temples, arches, and government buildings."},
            {"name": "Borghese Gallery", "address": "Piazzale Scipione Borghese, 5", "rating": 4.8, "estimated_cost": 15, "description": "Stunning collection of Bernini sculptures and Caravaggio paintings in a baroque villa."},
        ],
        "restaurants": [
            {"name": "Da Enzo al 29", "address": "Via dei Vascellari, 29, Trastevere", "rating": 4.7, "estimated_cost": 28, "description": "Beloved neighbourhood trattoria in Trastevere serving classic Roman pastas."},
            {"name": "Pizzarium Bonci", "address": "Via della Meloria, 43, Prati", "rating": 4.6, "estimated_cost": 10, "description": "Giacomo Bonci's legendary pizza al taglio (by the slice) — a Roman institution."},
            {"name": "Flavio al Velavevodetto", "address": "Via di Monte Testaccio, 97", "rating": 4.5, "estimated_cost": 30, "description": "Classic Roman cuisine built into the ancient Monte Testaccio rubbish hill."},
            {"name": "Supplì Roma", "address": "Via di San Francesco a Ripa, 137, Trastevere", "rating": 4.5, "estimated_cost": 5, "description": "Crispy fried rice balls stuffed with tomato sauce and mozzarella — Rome's best street food."},
        ],
        "activities": [
            {"name": "Gladiator School", "address": "Via Appia Antica, Roma", "rating": 4.6, "estimated_cost": 65, "description": "Train like a Roman gladiator with certified instructors near the ancient Appian Way."},
            {"name": "Pasta & Gelato Making Class", "address": "Various locations, Roma Centro", "rating": 4.7, "estimated_cost": 75, "description": "Hands-on class making fresh egg pasta from scratch followed by homemade gelato."},
            {"name": "Appian Way Cycling Tour", "address": "Via Appia Antica, 58", "rating": 4.5, "estimated_cost": 35, "description": "Cycle along the ancient road past Roman tombs, catacombs, and aqueducts."},
        ],
        "nightlife": [
            {"name": "Pigneto neighbourhood bars", "address": "Via del Pigneto, Roma", "rating": 4.4, "estimated_cost": 15, "description": "Rome's coolest neighbourhood for aperitivo hour and late-night bars."},
            {"name": "Freni e Frizioni", "address": "Via del Politeama, 4, Trastevere", "rating": 4.5, "estimated_cost": 12, "description": "Iconic aperitivo bar in Trastevere known for its lavish free-snack spread."},
        ],
        "shopping": [
            {"name": "Via Condotti", "address": "Via Condotti, 00187 Roma", "rating": 4.5, "estimated_cost": 200, "description": "Rome's most exclusive shopping street with Gucci, Prada, and Valentino flagship stores."},
            {"name": "Campo de' Fiori Market", "address": "Piazza Campo de' Fiori", "rating": 4.4, "estimated_cost": 20, "description": "Lively morning market for fresh produce, flowers, and Roman street food."},
        ],
        "transport": [
            {"name": "Roma Pass (48h)", "address": "Airports, tourist offices, major stations", "rating": 4.4, "estimated_cost": 32, "description": "Unlimited public transit plus free entry to 2 museums within 48 hours."},
            {"name": "ATAC 24h Bus & Metro Pass", "address": "Metro stations and tobacco shops", "rating": 4.3, "estimated_cost": 7, "description": "Unlimited rides on Rome's metro, buses, and trams for 24 hours."},
        ],
    },
}


def _normalize(city: str) -> str:
    return city.strip().lower()


def query_poi(destination: str, category: str, limit: int) -> list[dict]:
    city = _normalize(destination)
    city_data = _POI.get(city)

    if not city_data:
        for key in _POI:
            if key in city or city in key:
                city_data = _POI[key]
                break

    if not city_data:
        return []

    places = city_data.get(category.lower(), [])
    return places[:limit]
