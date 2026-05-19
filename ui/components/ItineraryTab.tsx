"use client";

import { useState } from "react";
import { Card, Field, Input, RunButton, ResultBox } from "./ui";

export default function ItineraryTab() {
  const [destination, setDestination] = useState("Tokyo");
  const [origin, setOrigin] = useState("New York");
  const [start, setStart] = useState("2026-07-01");
  const [end, setEnd] = useState("2026-07-10");
  const [budget, setBudget] = useState("");
  const [prefs, setPrefs] = useState("food, history");
  const [result, setResult] = useState<unknown>();
  const [error, setError] = useState<string>();
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    setError(undefined);
    try {
      const res = await fetch("/api/tools/plan_trip", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          destination,
          origin,
          start_date: start,
          end_date: end,
          ...(budget && { total_budget: Number(budget) }),
          ...(prefs && { preferences: prefs }),
        }),
      });
      const data = await res.json();
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
      <h2 className="text-base font-semibold mb-4">Plan Trip Itinerary</h2>
      <div className="grid grid-cols-2 gap-4">
        <Field label="Destination">
          <Input value={destination} onChange={(e) => setDestination(e.target.value)} />
        </Field>
        <Field label="Origin">
          <Input value={origin} onChange={(e) => setOrigin(e.target.value)} />
        </Field>
        <Field label="Start date">
          <Input type="date" value={start} onChange={(e) => setStart(e.target.value)} />
        </Field>
        <Field label="End date">
          <Input type="date" value={end} onChange={(e) => setEnd(e.target.value)} />
        </Field>
        <Field label="Total budget USD (optional)">
          <Input type="number" value={budget} onChange={(e) => setBudget(e.target.value)} placeholder="e.g. 5000" />
        </Field>
        <Field label="Preferences (optional)">
          <Input value={prefs} onChange={(e) => setPrefs(e.target.value)} placeholder="food, history, beaches" />
        </Field>
      </div>
      <RunButton loading={loading} onClick={submit} />
      <ResultBox data={result} error={error} />
    </Card>
  );
}
