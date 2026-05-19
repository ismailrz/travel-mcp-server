# Travel MCP Server

An AI-powered travel planner built as a [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server. Connect it to Claude and get a full travel assistant — search flights, hotels, weather, and points of interest, generate day-by-day itineraries, and track your trip budget.

## Tools

| Tool | Description |
|------|-------------|
| `search_flights` | Search flights between two cities by name or IATA code |
| `search_hotels` | Search hotels with optional price filter |
| `get_weather` | Day-by-day weather forecast for a destination |
| `search_poi` | Points of interest by category (restaurants, attractions, activities, nightlife, shopping, transport) |
| `plan_trip` | Generate a complete itinerary with weather, POI, flight & hotel options, and optional budget allocation |
| `create_trip_budget` | Create a budget tracker for a trip |
| `add_expense` | Record an expense against a budget category |
| `get_budget_summary` | Total spent, remaining balance, and per-category breakdown |

### Supported destinations (mock data)

**Flights:** New York ↔ Tokyo / Paris / London / Barcelona / Sydney / Bali · London ↔ Paris / Barcelona / Bali · Sydney ↔ Bali · Paris ↔ Rome

**Hotels, weather & POI:** Tokyo, Paris, London, Barcelona, Bali, Sydney, Rome, Amsterdam, Dubai

## Quickstart

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) — `brew install uv`

### Run locally (stdio — for Claude Desktop / Claude Code)

```bash
git clone <repo-url> travel-mcp-server
cd travel-mcp-server
uv sync
uv run python -m travel_mcp
```

### Inspect tools interactively

```bash
npx @modelcontextprotocol/inspector uv run python -m travel_mcp
```

## Connect to Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "travel-planner": {
      "command": "uv",
      "args": ["run", "--directory", "/absolute/path/to/travel-mcp-server", "python", "-m", "travel_mcp"]
    }
  }
}
```

Restart Claude Desktop. The 8 travel tools will appear automatically.

## Docker

```bash
# Build
docker build -t travel-mcp-server .

# Run (SSE transport on port 8000)
docker compose up
```

The server listens on `http://localhost:8000` in SSE mode when running via Docker.

## Kubernetes

```bash
# Deploy
kubectl apply -f k8s/

# Verify
kubectl rollout status deployment/travel-mcp-server -n travel-mcp

# Test locally via port-forward
kubectl port-forward svc/travel-mcp-server 8000:80 -n travel-mcp

# Tear down
kubectl delete -f k8s/
```

> **Note:** The Deployment runs a single replica because budget state is held in memory. Scale to multiple replicas only after adding external storage (Redis, Postgres, etc.).

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `MCP_TRANSPORT` | `stdio` | Transport mode: `stdio` (local) or `sse` (HTTP) |
| `HOST` | `0.0.0.0` | Bind address (SSE mode only) |
| `PORT` | `8000` | Port (SSE mode only) |

## Project structure

```
src/travel_mcp/
├── server.py          # FastMCP instance + tool registrations
├── tools/             # Business logic (one file per domain)
│   ├── flights.py
│   ├── hotels.py
│   ├── weather.py
│   ├── poi.py
│   ├── itinerary.py   # Composes other tools into a full itinerary
│   └── budget.py      # In-memory budget tracker
└── mock_data/         # Static fixtures — replace query_* functions to wire real APIs
    ├── flights.py
    ├── hotels.py
    ├── weather.py
    └── poi.py
```

## Swapping in real APIs

Each `mock_data/` file exposes a single `query_*` function. Replace just that function with an HTTP call to a real provider and everything else stays the same.

| Mock file | Suggested real API |
|-----------|-------------------|
| `mock_data/flights.py` | [Amadeus Flight Offers](https://developers.amadeus.com) |
| `mock_data/hotels.py` | [Amadeus Hotel Search](https://developers.amadeus.com) |
| `mock_data/weather.py` | [OpenWeatherMap](https://openweathermap.org/api) |
| `mock_data/poi.py` | [Google Places API](https://developers.google.com/maps/documentation/places/web-service) |

## Example prompts

- *"Plan a 7-day trip to Tokyo from New York in October with a $4,000 budget."*
- *"Find me flights from London to Barcelona for next Friday, 2 passengers."*
- *"What's the weather like in Bali in July?"*
- *"Show me the top attractions in Rome."*
- *"I spent $850 on flights for my Tokyo trip — log it and show my remaining budget."*

## License

MIT
