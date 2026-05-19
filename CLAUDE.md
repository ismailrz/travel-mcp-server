# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
uv sync

# Run the MCP server (stdio transport — for Claude Desktop / Claude Code)
uv run python -m travel_mcp

# Inspect tools interactively
npx @modelcontextprotocol/inspector uv run python -m travel_mcp
```

### Docker

```bash
# Build the image
docker build -t travel-mcp-server .

# Run locally (SSE transport on port 8000)
docker compose up

# Override transport back to stdio
docker run --rm -e MCP_TRANSPORT=stdio -i travel-mcp-server
```

### Kubernetes

```bash
# Apply all manifests
kubectl apply -f k8s/

# Check rollout
kubectl rollout status deployment/travel-mcp-server -n travel-mcp

# Port-forward for local testing
kubectl port-forward svc/travel-mcp-server 8000:80 -n travel-mcp

# Tear down
kubectl delete -f k8s/
```

## Architecture

A Python MCP server exposing 8 tools for AI-powered travel planning. Uses `FastMCP` from the `mcp[cli]` SDK with a two-layer structure:

```
src/travel_mcp/
├── server.py          # FastMCP instance + all @mcp.tool() registrations (single entry point)
├── tools/             # Business logic — one file per domain
│   ├── flights.py     # search()
│   ├── hotels.py      # search()
│   ├── weather.py     # get_forecast()
│   ├── poi.py         # search()
│   ├── itinerary.py   # plan() — calls mock_data directly, also initialises budgets
│   └── budget.py      # create(), add_expense(), get_summary() — in-memory state (_budgets dict)
└── mock_data/         # Static fixtures + query functions (swap these to wire real APIs)
    ├── flights.py     # query_flights()
    ├── hotels.py      # query_hotels()
    ├── weather.py     # query_forecast() — generates daily entries from monthly averages
    └── poi.py         # query_poi() — 6 categories × 8 cities
```

**Data flow:** `server.py` → `tools/*.py` → `mock_data/*.py`. `itinerary.plan()` imports directly from `mock_data/` (not through other tool modules) to avoid circular imports.

## Tools

| Tool | Key inputs | Notes |
|------|-----------|-------|
| `search_flights` | origin, destination, departure_date | Matches by city name or IATA code |
| `search_hotels` | destination, check_in, check_out | Supports `max_price` filter |
| `get_weather` | destination, date_from, date_to | Daily forecast from monthly averages |
| `search_poi` | destination, category, limit | 6 categories; see `Literal` in server.py |
| `plan_trip` | destination, start/end dates, origin | Auto-creates budget if `total_budget` given |
| `create_trip_budget` | trip_id, total_budget | Budget state lives in `budget._budgets` dict |
| `add_expense` | trip_id, category, amount | Returns full summary after adding |
| `get_budget_summary` | trip_id | total_spent, remaining_balance, category_breakdown |

## Supported destinations (mock data)

Flights: New York ↔ Tokyo/Paris/London/Barcelona/Sydney/Bali; London ↔ Paris/Barcelona/Bali; Sydney ↔ Bali; Paris ↔ Rome.

Hotels + Weather + POI: Tokyo, Paris, London, Barcelona, Bali, Sydney, Rome, Amsterdam, Dubai.

## Transport modes

`MCP_TRANSPORT` env var controls transport (default: `stdio`):
- **`stdio`** — used by Claude Desktop and Claude Code (local process)
- **`sse`** — HTTP/SSE server, used by Docker and Kubernetes deployments

`server.py:main()` reads `MCP_TRANSPORT`, `HOST`, and `PORT` to configure the FastMCP run mode.

## Adding a real API

Replace the `query_*` function in the relevant `mock_data/` file. The tool layer and server registration stay unchanged.

## Kubernetes notes

- **1 replica only** — budget state is in-memory (`tools/budget._budgets`). Scale to multiple replicas only after adding external storage (Redis, Postgres).
- **Image tag** — `k8s/deployment.yaml` uses `travel-mcp-server:latest`. For production, push to a registry and pin a version tag.
- **Exposing externally** — the Service is ClusterIP. Add a `k8s/ingress.yaml` or change `type: LoadBalancer` to expose outside the cluster.

## Claude Desktop config

```json
{
  "mcpServers": {
    "travel-planner": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/travel-mcp-server", "python", "-m", "travel_mcp"]
    }
  }
}
```
