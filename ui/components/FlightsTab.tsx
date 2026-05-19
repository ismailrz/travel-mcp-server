"use client";

import { useState } from "react";
import { Card, Field, Input, RunButton, ResultBox } from "./ui";

async function run(args: Record<string, unknown>) {
  const res = await fetch("/api/tools/search_flights", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(args),
  });
  return res.json();
}

export default function FlightsTab() {
  const [origin, setOrigin] = useState("New York");
  const [destination, setDestination] = useState("Tokyo");
  const [departure, setDeparture] = useState("2026-07-01");
  const [returnDate, setReturnDate] = useState("");
  const [passengers, setPassengers] = useState("1");
  const [result, setResult] = useState<unknown>();
  const [error, setError] = useState<string>();
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    setError(undefined);
    try {
      const data = await run({
        origin,
        destination,
        departure_date: departure,
        ...(returnDate && { return_date: returnDate }),
        passengers: Number(passengers),
      });
      if (data.error) setError(data.error);
      else setResult(data.data);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card>
      <h2 className="text-base font-semibold mb-4">Search Flights</h2>
      <div className="grid grid-cols-2 gap-4">
        <Field label="Origin">
          <Input value={origin} onChange={(e) => setOrigin(e.target.value)} placeholder="New York / JFK" />
        </Field>
        <Field label="Destination">
          <Input value={destination} onChange={(e) => setDestination(e.target.value)} placeholder="Tokyo / NRT" />
        </Field>
        <Field label="Departure date">
          <Input type="date" value={departure} onChange={(e) => setDeparture(e.target.value)} />
        </Field>
        <Field label="Return date (optional)">
          <Input type="date" value={returnDate} onChange={(e) => setReturnDate(e.target.value)} />
        </Field>
        <Field label="Passengers">
          <Input type="number" min={1} value={passengers} onChange={(e) => setPassengers(e.target.value)} />
        </Field>
      </div>
      <RunButton loading={loading} onClick={submit} />
      <ResultBox data={result} error={error} />
    </Card>
  );
}
